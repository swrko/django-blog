from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Author, Blog
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from blog.forms import UserForm, LoginUserForm
from django.contrib.auth import authenticate, login, logout
from django.http.response import Http404


# Create your views here.
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list_w3.html'


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list_w3.html'


class AuthorBlogListView(ListView):
    model = Blog
    template_name = 'blog_list_w3.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        author = get_object_or_404(Author, slug=slug)
        return author.blogs.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'author': Author.objects.filter(slug=self.kwargs.get('slug')).first()
        })
        return context


class BlogView(DetailView):
    model = Blog
    template_name = 'blog_w3.html'
    slug_field = 'headline'


class HomeView(TemplateView):
    template_name = 'home_w3.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'authors': Author.objects.all(),
            'blogs': Blog.objects.all()
        })
        return context


# createview
class RegistrationView(FormView):
    template_name = 'registration_w3.html'
    form_class = UserForm
    success_url = '/login'

    def form_valid(self, form):
        user_model = form.save(commit=False)  # neukladaj do databay ale ako formular
        user_model.set_password(form.cleaned_data.get('password'))
        user_model.save()
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login_w3.html'
    form_class = LoginUserForm

    def get_success_url(self):
        if self.request.method == 'POST' and not self.request.user.is_authenticated:
            return '/login'
        return '/home'

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'home'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super().get_redirect_url(*args, **kwargs)


'''
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context.update({
            'blog': Blog.objects.filter(headline=self.kwargs.get('headline')).first()
        })
        return context
'''

'''
get context data mi vrati context pre renderovanie template html  
na zaklade kluca si viem najst object v html
'''
