from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        """
        Renders a single blog post page
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Enables to leave a comment
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.comment_author = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """
    Enables to like a blog post
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# My own code


@login_required
def edit_comment(request, pk):
    """
    Enables to edit the approved comment
    """
    comment = get_object_or_404(Comment, id=pk)
    comment_form = CommentForm(instance=comment)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('post_detail', comment.post.slug)

    context = {
        'post_title': comment.post.title,
        'comment_form': comment_form,
    }

    return render(request, "edit_comment.html", context)


@login_required
def delete_comment(request, pk):
    """
    Enables to delete the approved comment
    """
    comment = get_object_or_404(Comment, id=pk)
    comment_form = CommentForm(instance=comment)
    if request.method == 'POST':
        comment.delete()
        return redirect('post_detail', comment.post.slug)
           
    context = {
        'post_title': comment.post.title,
        'comment_form': comment_form,
    }

    return render(request, "delete_comment.html", context)


def about(request):
    return render(request, 'about.html')


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def internal_server_error_view(request):
    return render(request, '500.html', status=500)
