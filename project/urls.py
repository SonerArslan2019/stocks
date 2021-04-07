from django.urls import path
from . import views

urlpatterns = [
    path('accounts/role/', views.RoleView.as_view(), name='role-list'),
]
