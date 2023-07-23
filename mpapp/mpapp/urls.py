from django.contrib import admin
from django.urls import path
from contact_us.views import Mycontactform

urlpatterns = [
    path('', Mycontactform.as_view(), name='contactme'),
    
    path('admin/', admin.site.urls),
]
