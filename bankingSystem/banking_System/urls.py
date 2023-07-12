from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('personal-registration/', views.personal_registration_view, name='personal-registration'),
    path('business-registration/', views.business_registration_view, name='business-registration'),
    path('investor-registration/', views.investor_registration_view, name='investor-registration'),
    path('personal-login/', views.personal_login_view, name='personal-login'),
    path('business-login/', views.business_login_view, name='business-login'),
    path('investor-login/', views.investor_login_view, name='investor-login'),
    path('admin-login/', views.admin_login_view, name='admin-login'),
    path('admin-mainpage/', views.admin_mainpage_view, name='admin-mainpage'),
    path('customers-list/', views.customers_list_view, name='customers-list'),
    path('single-personal-page/', views.single_personal_page_view, name='single-personal-page'),
    path('single-business-page/', views.single_business_page_view, name='single-business-page'),
    path('single-investor-page/', views.single_investor_page_view, name='single-investor-page'),
    path('personal-dashboard/', views.personal_dashboard_view, name='personal-dashboard'),
    path('business-dashboard/', views.business_dashboard_view, name='business-dashboard'),
    path('investor-dashboard/', views.investor_dashboard_view, name='investor-dashboard'),
    path('personal-password-reset/', views.personal_password_reset_view, name='personal-password-reset'),
    path('business-password-reset/', views.business_password_reset_view, name='business-password-reset'),
    path('investors-password-reset/', views.investors_password_reset_view, name='investors-password-reset'),
]
