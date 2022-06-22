from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path(r'^signin/$', views.signin, name="signin"),
    path('signout', views.signout, name='signout'),
    path('settings', views.settings, name='setting'),
    path('settings/add', views.setting_create_view, name='setting_add'),    # tried in another way
    # path('<int:pk>/setting', views.setting_update_view, name='setting_change'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]