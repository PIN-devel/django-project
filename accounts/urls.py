from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/follow', views.follow, name='follow'),
]
