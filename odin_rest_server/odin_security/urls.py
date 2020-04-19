from django.urls import path

from rest_framework_simplejwt import views as jwt_views
from . import views

app_name = 'odin_security'

urlpatterns = [
	path('menu/', views.MenuList.as_view(), name='menu-list'),
	path('token/', jwt_views.TokenObtainPairView.as_view(), name='get_token'),
	path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='get_token'),
]
