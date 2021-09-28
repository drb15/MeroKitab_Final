from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from home import views

urlpatterns = [
   path('', views.home, name='home'),
   path('signup/', views.signup_view, name='signup_view'),
   path('login/', views.login_view, name='login_view'),
   path('logout/', views.logoutUser, name='logout'),


   path('add_product/', views.addproduct, name='add_product'),
   path('contact/', views.contactus, name='contactus'),
   path('contact_seller/<str:pk>', views.contact_seller, name='contact_seller'),
   path('prod_detail/<str:pk>/',views.prod_detail,name = 'prod_detail'),
   path('search',views.search,name = 'search'),
   path('userprofile',views.userprofile,name = 'userprofile'),
   path('category/<str:cats>/',views.category_view,name = 'category_view'),


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