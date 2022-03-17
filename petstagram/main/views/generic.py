from django.shortcuts import redirect
from django.views import generic as views

from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.main.models import PetPhoto


# def show_home(request):
#     context = {
#         'hide_additional_nav_items': True,
#     }
#     return render(request, 'main/home_page.html', context)

class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'


# def show_dashboard(request):
#     profile = get_profile()
#     pet_photos = set(PetPhoto.objects.prefetch_related('tagged_pets').filter(tagged_pets__user_profile=profile))
#
#     context = {
#         'pet_photos': pet_photos,
#     }
#     return render(request, 'main/dashboard.html', context)