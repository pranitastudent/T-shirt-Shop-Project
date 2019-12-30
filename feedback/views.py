from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    posts = Feedback.objects.order_by('-published_date').all()
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    return render (request, "feedback/feedback.html", {"posts":paged_posts})

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
            messages.info(request, "Your Feedback has been successfully been added!")
            return redirect('detail_feedback', pk=post.pk)
    else:
        form=FeedbackForm()
    return render(request, "feedback/feedbackform.html", {"form":form})
        
# Edit Feedback post - logged in

@login_required()
def edit_feedback(request, pk=None):
    """
    This view allows users to edit only there
    own feedback if logged in
    """    
    post = get_object_or_404(Feedback, pk=pk)
    if request.user == post.author:
        if request.method == "POST":
            form = FeedbackForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('detail_feedback', pk=post.pk)
        else:
            form = FeedbackForm(instance=post)
        return render(request,"feedback/feedbackform.html", {"form":form}) 
    else:
        messages.info(request, "You don't have permission to edit this feedback")
        form = FeedbackForm() 
    return ('add_feedback') 

 
 # Delete Feedback - only logged in user
 
@login_required()
def delete_feedback(request, pk):
    """
    This view allows users to delete there own
    feedback if logged in
    """
    post=get_object_or_404(Feedback, pk=pk)
    if request.user == post.author:
        post.delete()
        messages.info(request, "Your Feedback has been successfully deleted!")
        return redirect(get_feedback)
    else:
        messages.info(request, "You don't have permission to delete this feedback")
    return ('get_feedback')    
    
    

# Votes - All Allowed to vote

def upvote(request,pk):
    if request.method == "POST":
        upvote = get_object_or_404(Feedback, pk=pk)
        upvote.upvote +=1
        upvote.save()
        return redirect ('get_feedback')  
         