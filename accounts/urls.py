from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
	path('signup/',views.signup,name="signup"),
	path('signin/',views.signin,name="signin"),
	path('logout/',views.logoutUser,name="logout"),

	path('',views.home,name="home"),
	path('user/',views.userPage,name="userPage"),
	path('profile/<str:id>/',views.profile,name="profile"),
	path('about/',views.about,name="about"),
	path('products/',views.products,name="products"),
	path('customer/<str:id>/',views.customer,name="customer"),
	path('create_order/',views.createorder,name="create_order"),
	path('create_order/<str:id>/',views.updateorder,name="create_order"),
	path('delete_order/<str:id>/',views.deleteorder,name="delete_order"),
	path('update_customer/<str:id>/',views.updatecustomer,name="update_customer"),
	path('delete_customer/<str:id>/',views.deletecustomer,name="delete_customer"),
	path('create_customer/',views.createcustomer,name="create_customer"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), 
        name="password_reset_complete"),

]