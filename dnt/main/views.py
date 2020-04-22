from django.shortcuts import render

# Create your views here.

# from main.models import mdCompany #, mdPosition, mdEmployee
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import MyUser
from .forms import ChangeUserinfoForm

class DNTPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'reg/password_change.html'
    success_url = reverse_lazy('main:index')
    success_message = 'Пароль пользователя изменен'

class DNTLoginView(LoginView):
    template_name = 'reg/login.html'

class DNTLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'reg/logout.html'

class ChangeUserinfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = MyUser
    template_name = 'reg/change_user_info.html'
    form_class = ChangeUserinfoForm
    success_url = reverse_lazy('main:index')
    success_message = 'Личные данные пользователя изменены'
    
    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

#@login_required
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_dept=MyUser.objects.all().count()
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_dept':num_dept},
    )





