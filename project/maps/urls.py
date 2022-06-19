"""maps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from myapp import views
from rest_framework import routers

router = routers.DefaultRouter()
 
# define the router path and viewset to be used
router.register(r'user', views.UserViewset)
router.register(r'data',views.TodoListApiView)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('data/', views.TodoListApiView.as_view(), name='data'),
    # path('user/',views.UserViewset.as_view(),name='user'),
    path('', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

# from django.urls import path
# from rest_framework_simplejwt import views as jwt_views

# urlpatterns = [
#     # Your URLs...
#     path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
# ]