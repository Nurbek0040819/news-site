from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='base.html')),
    path('accounts/register/', TemplateView.as_view(template_name='registration/register.html'), name='register'),
    path('news/', include('app_news.urls')),
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
]
