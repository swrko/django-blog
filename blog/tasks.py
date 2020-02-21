from my_blog.celery import app
from blog.models import Blog


@app.task(bind=True)
def check_blog_content(self, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    if "smaha" in blog.body:
        blog.hidden = True
        blog.control_requested = False
        # mozem poslat nejaku poznamku k autorovi k blogu/notifikaciu
    else:
        blog.hidden = False
        blog.control_requested = False

    blog.save()
