from django.urls import path, reverse_lazy
from . import authviews
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, LoginView, LogoutView
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('sign-in/', LoginView.as_view(template_name='auth/login.html'), name='sign-in'),
    path('sign-up', authviews.SignUpView.as_view(), name='sign-up'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('profile', login_required(authviews.ProfileView.as_view()), name='profile'),

    path('change-password', PasswordChangeView.as_view(template_name='auth/change-password.html'), name='change-password'),
    path('change-password-done', PasswordChangeDoneView.as_view(template_name='auth/done-password.html'), name='password_change_done'),
]