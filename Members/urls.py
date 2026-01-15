from django.urls import path
from .views import MemberCreateView

urlpatterns = [
    path('add_members/', MemberCreateView.as_view(), name='member-create-view'),    
] 