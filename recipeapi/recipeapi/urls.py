"""
URL configuration for recipeapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from recipe import views
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views as rviews

router=SimpleRouter()
router.register('recipe',views.Recipedetail)
router.register('user',views.CreateUser)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    # path('allrecipe/<pk>', views.AllRecipe.as_view()),
    path('Allrecipe/', views.Allrecipe.as_view(), name='allrecipe'),
    path('reviews/',views.Reviewlist.as_view()),
    path('review/<int:pk>',views.Reviewdetail.as_view()),
    path('api-token-auth/',rviews.obtain_auth_token),
    path('search/',views.Search.as_view(),name="search"),
    path('logout', views.user_logout.as_view(), name="logout"),
]
