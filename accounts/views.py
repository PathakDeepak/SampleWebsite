from django.shortcuts import render

# Create your views here.

from accounts.models import User
from . import forms

def login(request):
    user_name = User.objects.order_by('user_name')[0].user_name
    user_pass = User.objects.order_by('user_pass')[0].user_pass

    form = forms.LoginForm()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            passwd = form.cleaned_data['passwd']


            # print('form name '+name)
            # print('form pass '+passwd)
            # print(user_name[0].user_name)
            # print(user_pass[0].user_pass)
            if user_name == name and user_pass == passwd:
                return render(request, 'accounts/userpage.html',{'name':name})       

    return render(request, 'accounts/login.html',{'form':form})    


def logout(request):
    return render(request,'home_page/home.html',{})    
