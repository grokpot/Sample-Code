from blog.models import Post
from django.shortcuts import render_to_response, RequestContext, get_object_or_404

def blog(request, template='blog.html'):
    all_posts = Post.objects.all()
    data = {'posts': all_posts}
    return render_to_response(template, data, context_instance=RequestContext(request))

def post(request, post, template='post.html'):
    post = get_object_or_404(Post, id=post)
    data = {'post': post}
    return render_to_response(template, data, context_instance=RequestContext(request))

def about(request, template='about.html'):
    all_posts = Post.objects.all()
    data = {'posts': all_posts}
    return render_to_response(template, data, context_instance=RequestContext(request))