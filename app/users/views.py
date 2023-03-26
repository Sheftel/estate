from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import SignUpForm, QuestionsForm
from .models import Client


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('users:signin')
    template_name = 'users/registration.html'


class QuestionsView(UpdateView):
    form_class = QuestionsForm
    template_name = 'users/questions.html'
    success_url = reverse_lazy('property:list')
    model = Client

    def get_object(self, queryset=None):
        try:
            return self.model.objects.first()
        except AttributeError:
            return None

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
