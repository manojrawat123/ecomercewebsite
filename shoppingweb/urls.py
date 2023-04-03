"""shoppingweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from shop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from shop.forms import MyPasswordResetForm , MySetPasswordForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name="home"),
    path("login/", views.login_page, name = "login"),
    path('registration/', views.signup_page, name="signup"),
    path("add-to-cart/", views.add_cart_page, name = "add-to-cart"),
    path("plus-cart/<int:pk>", views.plus_cart, name="plus-cart"),
    path("minus-cart/<int:pk>", views.minus_cart, name="minuscart"),
    path("removeitem/<int:pk>", views.remove_cart, name="remove_cart"),
    path("show-cart/", views.show_cart_page, name = "cart"),
    path("payment/<int:pk>", views.payment_page, name="payment"),
    path("deleteitem/<int:pk>", views.delete_items, name="deletepage"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("checkout/", views.checkout_page, name="checkout"), 
    path("adress/", views.adress_page, name="adress"),
    path("order/", views.order_page, name="order"),
    path("product/<int:pk>", views.product_page, name="product"),
    path("buy/", views.buy_page, name= "buy"),
    path("changepass/", views.change_password, name = "changepass"),
    path("mobile/", views.mobile_details, name="mobile"),
    path("mobile/<slug:data>", views.mobile_details, name="mobiled"),
    path("laptop/", views.laptop_details , name= "laptop"),
    path("laptop/<slug:data>", views.laptop_details, name="laptopd"),
    path("tshirt", views.tshirt_details , name= "tshirt"),
    path("tshirt/<slug:data>", views.tshirt_details, name="tshirtd"),
    path("shoes/", views.shoes_details, name="shoes"),
    path("shoes/<slug:data>", views.shoes_details ,name="shoesd"),
    path("car/", views.car_details, name="car"),
    path("car/<slug:data>", views.car_details, name="card"),
    path("bike/", views.bike_details, name="bike"),
    path("bike/<slug:data>", views.bike_details, name="biked"),
    path("logout/", views.logout_page, name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name = 'shop/password_reset.html', form_class = MyPasswordResetForm),name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name = 'shop/password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(template_name= "shop/password_reset_confirm.html", form_class = MySetPasswordForm ),
        name="password_reset_confirm"),
    path("password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name = 'shop/password_reset_complete.html'), 
        name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
