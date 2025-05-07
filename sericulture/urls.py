from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('add-farmer/', views.add_farmer, name='add_farmer'),
    path('market-trends/', views.market_trends, name='market_trends'),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('mulberry-farms/', views.list_mulberry_farm, name='list_mulberry_farm'),
    path('mulberry-farms/add/', views.create_mulberry_farm, name='add_mulberry_farm'),
    path('mulberry-farms/edit/<int:pk>/', views.edit_mulberry_farm, name='edit_mulberry_farm'),
    path('mulberry-farms/delete/<int:pk>/', views.delete_mulberry_farm, name='delete_mulberry_farm'),

    path('silkworm-batches/', views.list_silkworm_batches, name='list_silkworm_batches'),
    path('silkworm-batches/add/', views.create_silkworm_batch, name='add_silkworm_batch'),
    path('silkworm-batches/edit/<int:pk>/', views.edit_silkworm_batch, name='edit_silkworm_batch'),
    path('silkworm-batches/delete/<int:pk>/', views.delete_silkworm_batch, name='delete_silkworm_batch'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.CustomPasswordResetDoneView.as_view(), name='password_reset_done'),



]
