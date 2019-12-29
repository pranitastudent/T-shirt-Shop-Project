from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    posts = Feedback.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    return render (request, "feedback/feedback.html", {"posts":posts})

# Single View of feedback post
@login_required()
def detail_feedback(request, pk):
    """
    This view allows users to see there only feedback
    post
    """
    post = get_object_or_404(Feedback, pk=pk)
    post.save()
    return render(request, "feedback/detail_feedback.html", {"post":post})

# Add Feedback post - logged in

@login_required()
def add_feedback(request):
    """
    This View allows logged in users
    to post there feedback about the product
    """
    
    if request.method=="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail_feedback', pk=post.pk)
    else:
        form=FeedbackForm()
    return render(request, "feedback/feedbackform.html", {"form":form})
        
# Edit Feedback post - logged in
@login_required()
def edit_feedback(request, pk):    
    post = get_object_or_404(Feedback, pk=pk)
    if request.user == post.author:
        if request.method == "POST":
            form = FeedbackForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect(get_feedback)
        else:
            form = FeedbackForm(instance=post)
        return render(request,"feedback/feedbackform.html", {"form":form}) 
    else:
        messages.info(request, "You don't have permission to edit this feedback")
        form = FeedbackForm() 
    return redirect ('add_feedback')     


        
    
# Votes- anyone can vote

# def votes(request, pk):
#     """
#     A view that allows all users to votes on a feedback
#     """
#     if request.method == "POST":
#         votes =get_object_or_404(Feedback, pk=pk)
#         votes.votes += 1
#         votes.save()
#         return redirect ("feedback/feedback.html")
        
    
       
