from django.urls import path, include
from . import views
from .views import profile_view
from .views import *
# from .views import RegisterView
from django.urls import path
from . import views

app_name = 'shopapp'
# app_name = 'registration'
urlpatterns = [
    path('', index, name='index'),
    path('accounts/logout/', custom_logout_view, name='logout'),
    # path('login', views.login_view, name='login'),
    path('login', login_view),
    # path('form', form, name='form'),
    path('reg', reg_view, name='reg'),
    path('profile/', profile_view, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('form/', views.form, name='form'),
    # path('add-appointment/', add_appointment, name='add_appointment'),
    path('test', test, name='test'),

]
