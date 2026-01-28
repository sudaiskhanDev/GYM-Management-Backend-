# payments/urls.py
from django.urls import path
from .views import PayFeeView

urlpatterns = [
    path('pay-fee/', PayFeeView.as_view()),
]
