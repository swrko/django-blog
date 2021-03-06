from django.contrib import admin
from blog.models import Blog, Author
from django.utils.text import slugify
from blog.tasks import check_blog_content


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'authors_', 'date']

    def authors_(self, blog):
        return ", ".join([x.__str__() for x in blog.authors.all()])

    def save_model(self, request, obj, form, change):
        check_blog_content.apply_async((obj.pk,), countdown=60)
        super().save_model(request, obj, form, change)


# authors_list = lambda self, blog: ", ".join([x.__str__() for x in blog.authors.all()])


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'age', 'count']

    def count(self, author):
        return author.blogs.all().count()

    def save_model(self, request, obj, form, change):
        obj.slug = slugify(f'{obj.name} {obj.surname}')
        super().save_model(request, obj, form, change)
