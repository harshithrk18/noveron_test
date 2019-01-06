from django.urls import path
from . import views

app_name = 'tenant_test'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('table', views.table, name='table'),
    path('create', views.TenantCreate.as_view(), name='create'),
    path('update/<pk>', views.TenantUpdate.as_view(), name='update'),
    path('delete/<pk>', views.TenantDelete.as_view(), name='delete'),


]