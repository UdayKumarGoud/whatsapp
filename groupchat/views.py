from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['POST'])
def create_group(request):
    # Implement group creation logic here
    return Response({"message": "Group created successfully."})

@api_view(['GET'])
def user_status(request, user_id):
    # Implement user status retrieval logic here
    return Response({"status": "online"})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.auth.permissions import IsAuthenticated
from .models import Group
from users.models import AppUser

# @login_required
def chat_room(request, group_name):
    # print(request.META)
    # print(request.META['HTTP_COOKIE'])
    # token_key = request.session.get('token')
    # print("Chatt Room", token_key)
    return render(request, 'gchat.html', {
        'group_name': group_name
    })


@permission_classes(IsAuthenticated,)
def home(request):
    user_id = request.session.get('token')
    if user_id:
        try:
            user = AppUser.objects.get(auth_token=user_id)
            print("User Data", user)
            groups = Group.objects.all()
            # token_key = request.GET.get('token')
            # print("home Page", token_key)
            return render(request, 'home.html', {'groups': groups, 'user': user})
        except AppUser.DoesNotExist:
            pass
    
    # If user not authenticated, redirect to login
    return redirect('login')
    

def group_detail(request, group_id):
    group = Group.objects.get(pk=group_id)
    # token_key = request.GET.get('token')
    return render(request, 'group_detail.html', {'group': group})