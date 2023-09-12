from django.contrib import admin
from django.urls import path, include
from accounts.views import home

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]

