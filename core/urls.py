from django.contrib import admin
from django.urls import path, include
from accounts.views import home as account_home

urlpatterns = [
    path('', account_home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]

