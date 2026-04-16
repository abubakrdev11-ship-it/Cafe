from django.urls import path
from .views import CreateOrderView, OrderListView, AcceptOrderView, CloseOrderView

urlpatterns = [
    path('orders/create/', CreateOrderView.as_view()),
    path('orders/', OrderListView.as_view()),
    path('orders/accept/', AcceptOrderView.as_view()),
    path('orders/close/', CloseOrderView.as_view()),
]