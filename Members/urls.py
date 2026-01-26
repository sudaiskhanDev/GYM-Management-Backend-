from django.urls import path
from .views import MemberCreateView, MemberEditView

urlpatterns = [
    path('add_members/', MemberCreateView.as_view(), name='member-create-view'), 
    path('edit_member/<int:pk>/', MemberEditView.as_view())   
] 