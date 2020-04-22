"""dnt company URL Configuration
"""
from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'main' 

urlpatterns = [
    path('accounts/password/change/', views.DNTPasswordChangeView.as_view(), name='password_change'),
    path('acoounta/change/', views.ChangeUserinfoView.as_view(), name='profile_change'),
    path('accounts/logout/', views.DNTLogoutView.as_view(), name='logout' ),
    path('accounts/login/', views.DNTLoginView.as_view(), name='login'),
    path('index/', views.index, name='index'),
#    path('', views.index, name='index'),
]

urlpatterns += [
    path('', RedirectView.as_view(url='accounts/login/', permanent=True)),
]
