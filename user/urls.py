from django.urls import path
from .views import DepositMoneyView, SignupView, UserLoginView, UserLogoutView, ProfileView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', UserLoginView.as_view(), name='signin'),
    path('logout/', UserLogoutView.as_view(), name='signout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('deposit_money/', DepositMoneyView.as_view(), name='deposit_money'),
]