from django.urls import include, path
from django.contrib.auth.views import LoginView as SignInView, LogoutView as SignOutView
from .views import SignUpView

app_name = 'property'


urlpatterns = [
    path('signin/', SignInView.as_view(template_name='users/login.html'), name='signin'),
    path('signout/', SignOutView.as_view(), name='signout'),
    path('signup/', SignUpView.as_view(), name='signup')
]
