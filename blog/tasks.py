from blog.models import Post
from testna_naloga.celery import app
import random

@app.task
def mark_featured():
    """
    Every minute mark random blog post with featured
    """
    posts = Post.objects.all()

    if len(posts) > 0:
        r = random.randint(0, len(posts)-1)

        post = posts[r]
        post.featured = True
        post.save()

        print "Marking featured post: %s" % post.id
