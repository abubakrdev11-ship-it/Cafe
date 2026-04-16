from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Order
from .serializers import OrderSerializer


class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.all()


class AcceptOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get('id')

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Не найден'}, status=404)

        if order.customer != request.user:
            return Response({'error': 'Это не ваш заказ'}, status=403)

        if order.status != 'new':
            return Response({'error': 'Уже обработан'}, status=400)

        order.status = 'accepted'
        order.executor = request.user
        order.save()

        return Response({'message': 'Заказ принят'})


class CloseOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        order_id = request.data.get('id')

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({'error': 'Не найден'}, status=404)

        if order.customer != request.user:
            return Response({'error': 'Это не ваш заказ'}, status=403)

        if order.status != 'accepted':
            return Response({'error': 'Сначала принять'}, status=400)

        order.status = 'closed'
        order.save()

        return Response({'message': 'Заказ закрыт'})