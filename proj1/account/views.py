from django.contrib.auth import login
from django.shortcuts import render

from account.models import User
from userProfile.models import UserProfile

    
def account(request):
    if not User.objects.all().exists():
        admin = User.objects.create_superuser(username='admin',
                                              password='admin',
                                              email='admin@gmail.com',
                                              fullName='admin')
        UserProfile.objects.create(user=admin, height=170)
        user = User.objects.create(username='user',
                                   password='user',
                                   email='user@gmail.com',
                                   fullName='user')
        UserProfile.objects.create(user=user, height=175)
        
    login(request, User.objects.get(username='admin'))
    return render(request,
                  'account/account.html',
                  {'admin':User.objects.get(username='admin'),
                   'users':User.objects.all()})
