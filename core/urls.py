from django.contrib import admin
from django.urls import path, include
from . import yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/verify_email/', include('verify_email.urls')),
]

urlpatterns += yasg.urlpatterns
