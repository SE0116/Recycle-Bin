from django.shortcuts import get_object_or_404, redirect, render
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/index.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


@require_safe
def detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment_form = CommentForm()
    comments = review.comment_set.all()
    context = {
        'review': review,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'community/detail.html', context)


@require_POST
def comment_create(requset, review_pk):
    if requset.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        comment_form = CommentForm(requset.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = requset.user
            comment.save()
        return redirect('community:detail', review.pk)
    return redirect('accounts:login')


@require_POST
def like(requset, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if requset.user.is_authenticated:
        if review.like_users.filter(pk=requset.user.pk).exists():
            review.like_users.remove(requset.user)
        else:
            review.like_users.add(requset.user)
        return redirect('community:detail', review.pk)
    return redirect('accounts:login')
    
            