from django.urls import path
from authapp.views import LoginListView,RegisterFormView,Logout,ProfileFormView


app_name = 'authapp'
urlpatterns = [
    path('login/', LoginListView.as_view(), name='login'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('verify/<str:email>/<str:activate_key>/', RegisterFormView.verify, name='verify')
]
