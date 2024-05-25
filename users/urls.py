from django.urls import path
from .views import LoginView, RegisterView, data, read_data, UpdateView, delete_data

urlpatterns = [
    path('', LoginView.as_view(), name='login_page'),
    path('register-page/', RegisterView.as_view(), name='register_page'),
    path('data/', data, name='data'),
    path('read_data/<int:id>',read_data, name='read_data'),
    path('delete_data/<int:id>',delete_data, name='delete_data'),
    path('update/<int:user_id>/', UpdateView.as_view(), name='user_update'),
]