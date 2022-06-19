from django.views import generic as views
from django.contrib.auth import views as auth_view
from django.urls import reverse_lazy

from petstagram.accounts.forms import CreateProfileForm
from petstagram.accounts.models import Profile
from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.main.models import Pet, PetPhoto


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_view.LoginView):
    template_name = 'accounts/change_password_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView:
    pass


class ChangeUserPasswordView(auth_view.PasswordChangeView):
    template_name = 'accounts/change_password_page.html'


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_object_name = 'profile'
        pets = list(Pet.objects.filter(user_id=self.object.user_id))
        total_pet_photos = len(PetPhoto.objects.filter(tagged_pets__user_id=self.object.user_id).distinct())
        total_likes_count = sum(
            pp.likes for pp in PetPhoto.objects.filter(tagged_pets__user_id=self.object.user_id).distinct())

        context.update({

            'total_likes_count': total_likes_count,
            'total_pet_photos': total_pet_photos,
            'pets': pets,
            'is_owner': self.object.user_id == self.request.user.id,

        })
        return context




#
# def show_profile(request):
#     profile = get_profile()
#     pets = list(Pet.objects.filter(user_profile=profile))
#     total_pet_photos = len(PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
#     total_likes_count = sum(pp.likes for pp in PetPhoto.objects.filter(tagged_pets__user_profile=profile).distinct())
#
#     context = {
#         'profile': profile,
#         'total_likes_count': total_likes_count,
#         'total_pet_photos': total_pet_photos,
#         'pets': pets,
#
#     }
#     return render(request, 'main/profile_details.html', context)


# def profile_action(request, form_class, success_url, instance, template_name):
#     if request.method == "POST":
#         form = form_class(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     else:
#         form = form_class(instance=instance)
#
#     context = {
#         'form': form,
#     }
#     return render(request, template_name, context)
#
#
# def create_profile(request):
#     return profile_action(request, CreateProfileForm, 'index', Profile(), 'main/profile_create.html')
#
#
# def edit_profile(request):
#     return profile_action(request, EditProfileForm, 'profile', get_profile(), 'main/profile_edit.html')
#
#
# def delete_profile(request):
#     return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'main/profile_delete.html')

# def create_profile(request):
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = CreateProfileForm()
#
#     context = {
#         'form': form,
#
#     }
#     return render(request, 'profile_create.html', context)
#
#
# def edit_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = EditProfileForm(instance=profile)
#
#     context = {
#         'form': form,
#
#     }
#     return render(request, 'profile_edit.html', context)
