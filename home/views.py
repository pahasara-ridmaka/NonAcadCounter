from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, render,redirect
from .models import Event, Comment
from .forms import CommentForm

def countdown_timer(request):
    event = Event.objects.first()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid(): # added condition to check if form valid
            comment = form.save(commit=False) # save the comment without commit
            comment.event = event
            comment.save()
            return redirect('countdown_timer') # redirect to home after saving the comment
    else:
        form = CommentForm()
    comments = Comment.objects.filter(event=event)

    if event:

        time_remaining = timezone.now() - event.date
        days = time_remaining.days
        hours = (time_remaining.seconds // 3600 )
        

        data = {
            'name' : event.name,
            'days' : days,
            'hours' : hours,
            'comments' : comments,
            'form' : form,

        }
    else:
        data = {
            'name' : "No Event",
            'days' : 0,
            'hours' : 0,
            'comments' : [],
            'form' : form,
        }
    return render(request, 'myapp.html', {'data': data})



def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id= comment_id)
    
    if request.method == "POST":
        if request.session.get(f'{comment_id}button_pressed', False):
            comment.likes_count -= 1
            request.session[f'{comment_id}button_pressed'] = False
            
        else:
            comment.likes_count += 1
            request.session[f'{comment_id}button_pressed'] = True
        comment.save()
    return JsonResponse({'likes': comment.likes_count})

