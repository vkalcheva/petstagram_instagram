from django.urls import path

from petstagram.accounts.views import UserLoginView, ProfileDetailsView, UserRegisterView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile'),
    path('profile/create/', UserRegisterView.as_view(), name='create profile'),
    # path('profile/edit/', edit_profile, name='edit profile'),
    # path('profile/delete/', delete_profile, name='delete profile'),
)