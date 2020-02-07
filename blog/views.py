from django.shortcuts import render
from django.views.generic.list import ListView
from blog.models import Author, Blog
from django.shortcuts import get_object_or_404
from django.http.response import Http404


# Create your views here.
class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'


class AuthorBlogListView(ListView):
    model = Blog
    template_name = 'blog_list.html'

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

'''
get context data mi vrati context pre renderovanie template html  
na zaklade kluca si viem najst object v html
'''



