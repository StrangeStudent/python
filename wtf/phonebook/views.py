from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from . import froms
from . import models


class HomePage(TemplateView):
    template_name = 'phonebook/home.html'


class CreatePersonForm(CreateView):
    template_name = 'phonebook/add_person.html'
    form_class = froms.CreatePersonForm
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()
