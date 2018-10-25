"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, LoginView, LogoutView
from django.contrib.auth import login, logout
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pid>', views.category_list, name='category'),
    path('all/', views.all_list, name='all'),

    path('sign-in/', LoginView.as_view(template_name='login.html'), name='sign-in'),
    path('sign-up', views.sign_up, name='sign-up'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('profile', views.profile, name='profile'),

    path('change-password', PasswordChangeView.as_view(template_name='change-password.html'), name='change-password'),
    path('change-password-done', PasswordChangeDoneView.as_view(template_name='change-password.html'), name='password_change_done'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)