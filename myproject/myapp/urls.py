from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('forgot-password', views.forgot_password, name='forgot_password'),
    path('profile', views.profile, name='profile'),
    path('health-metrics', views.healthmetrics, name='healthmetrics'),
    path('real-time-monitoring', views.realtimemonitoring, name='realtimemonitoring'),
    path('health-advice', views.healthadvice, name='healthadvice'),
    path('alerts', views.alerts, name='alerts'),
    path('settings',views.settings,name='settings'),
]
