from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from app_news.models import News
from django.http import HttpResponseRedirect, HttpResponseForbidden


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class AddNewsView(LoginRequiredMixin, CreateView):
    template_name = 'news/add_news.html'
    model = News
    success_url = reverse_lazy('home')
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category']

    def form_valid(self, form):
        form.instance.news_author = self.request.user
        return super().form_valid(form)


class ListNewsView(ListView):
    template_name = 'news/list_news.html'
    model = News
    paginate_by = 5


class DetailNewsView(DetailView):
    template_name = 'news/show_news.html'
    model = News


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'news/update_news.html'
    model = News
    success_url = reverse_lazy('home')
    fields = ['news_title', 'news_description', 'news_image', 'news_content', 'news_category']

    def test_func(self):
        return self.request.user.is_superuser or self.get_object().news_author == self.request.user

    def handle_no_permission(self):
        return HttpResponseForbidden("Sizda yangilikni o'zgartirish uchun ruxsat yo'q.")


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = reverse_lazy('home')
    template_name = 'news/delete_news.html'

    def test_func(self):
        return self.request.user.is_superuser or self.get_object().news_author == self.request.user

    def handle_no_permission(self):
        return HttpResponseForbidden("Sizda yangilikni o'chirish uchun ruxsat yo'q.")


def superuser_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # print(request.user.is_authenticated)
            try:
                all_users_emails = User.objects.values_list('email', flat=True)
                for email in all_users_emails:
                    send_mail(
                        subject=request.POST['subject'],
                        message=request.POST['message'],
                        from_email="doniyorovnurbek286@gmail.com",
                        recipient_list=[email]
                    )
                return HttpResponse("Successfully sent email to all users")
            except Exception as e:
                return HttpResponse(f"Something went wrong: {e}")
    return render(request, 'superuser.html')
