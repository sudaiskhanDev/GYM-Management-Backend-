 
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('Members.urls')),
    path('payments/', include('Fee.urls')),

    
]
