# payments/urls.py
from django.urls import path
from .views import PayFeeView,PaymentListView

urlpatterns = [
    path('pay-fee/', PayFeeView.as_view()),
    path('list/', PaymentListView.as_view()),
]
