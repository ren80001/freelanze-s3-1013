from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.AistView.as_view(), name='top'),
    path('<int:pk>/', views.DetailView.as_view(), name='datail_view'),
    path('login/', views.Login.as_view(), name='login'),
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', views.UserUpdate.as_view(), name='user_update'),
    path('search/', views.ListView.as_view(), name='search'),
    path('test_login/', views.TestCreate.as_view(), name='test_login'),
]