from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from petstagram.accounts.views import UserLoginView, ProfileDetailsView, UserRegisterView, ChangeUserPasswordView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),

    path('edit-password/', ChangeUserPasswordView.as_view(), name='change password'),

    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile details'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),
    # path('profile/edit/', edit_profile, name='edit profile'),
    # path('profile/delete/', delete_profile, name='delete profile'),
)