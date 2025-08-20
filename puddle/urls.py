

from django.contrib import admin
from django.urls import include, path

from core.views import index, contact

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]
