from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

class ChatListView(LoginRequiredMixin, ListView):
    template_name = 'chat_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.exclude(pk=self.request.user.pk)


# myapp/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Message

@login_required
def chat(request, recipient_username):
    messages = Message.objects.filter(sender=request.user, recipient__username=recipient_username) | \
               Message.objects.filter(sender__username=recipient_username, recipient=request.user).order_by('timestamp')[:50]
    print("Message",messages)
    return render(request, 'chat.html', {
        'recipient_username': recipient_username,
        'messages': messages
    })

