"""
URL configuration for catalogAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from catalogApp.views import ShowCategoryView, ShowProductView, CategoryView, ProductView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_category', ShowCategoryView.as_view(), name='show_category'),
    path('show_product', ShowProductView.as_view(), name='show_product'),
    path('product', ProductView.as_view(), name='product'),
    path('category', CategoryView.as_view(), name='category'),



]
