"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Item
    path('', views.IndexListView.as_view()), #トップページ
    path('items/<str:pk>/', views.ItemDetailView.as_view()), # アイテム詳細

    # Cart
    path('cart/', views.CartListView.as_view()), #カート一覧
    path('cart/add/', views.AddCartView.as_view()), #カート追加
    path('cart/remove/<str:pk>/', views.remove_from_cart),

    # Pay
    path('pay/checkout/', views.PayWithStripe.as_view()),
    path('pay/success/', views.PaySuccessView.as_view()),
    path('pay/cancel/', views.PayCancelView.as_view()),
]
