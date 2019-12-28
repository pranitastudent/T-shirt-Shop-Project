from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Feedback
from .forms import FeedbackForm
# All Views adapated from Code Institute Lectures on Blog in Fullstack Framework Module

# All users can see feedback

def get_feedback(request):
    """
    Create view all users can view feedback
    """
    posts = Feedback.objects.filter(published_date__lte=timezone()
                                    ).order_by('-published_date')
    return render (request, "feedback.feedback.html", {"posts":posts})


# Single View of feedback post

def detail_feedback(request, pk):
    """
    This view allows users to see there only feedback
    post
    """
    post = get_object_or_404(Feedback, pk=pk)
    post.save()
    return render(request, "feedback/detail_feedback.html", {"post":post})

# Create a feedback post - only logged in users

def add_feedback(request):
    """
    Allows logged in user to add feedback
    post
    """
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feedback/detail_feedback', pk=post.pk)
    else:
        form = FeedbackForm()
    return render(request, "feedback/feedback.html", {"form":form})            
