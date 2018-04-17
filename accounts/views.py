from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from accounts.models import User
from . import forms
from django.contrib.auth import authenticate, login, get_user_model, logout

def login_page(request):
    # user_name = User.objects.order_by('user_name')[0].user_name
    # user_pass = User.objects.order_by('user_pass')[0].user_pass

    # form = forms.LoginForm()

    # if request.method == 'POST':
    #     form = forms.LoginForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['name']
    #         passwd = form.cleaned_data['passwd']
    #         if user_name == name and user_pass == passwd:
    #             return render(request, 'accounts/userpage.html',{'name':name})       

    # return render(request, 'accounts/login.html',{'form':form})    

    form = forms.LoginForm(request.POST or None)
    context = {'form': form,'a':None}
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('name')
        password = form.cleaned_data.get('passwd')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return render(request, 'accounts/userpage.html',{'name':username})
        else:
            context['a']='a'
            print('Error')
            #return HttpResponse("You're account is disabled.<br/><a href=")
        #print  ("invalid login details " + username + " " + password)
        
    return render(request,'accounts/login.html',context) 


def logout(request):
    context = RequestContext(request)
    logout(request)
    return render(request,'home_page/home.html',{})    

user = User()
def register_page(request):
    form =  forms.RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("name")
        password = form.cleaned_data.get("passwd")
        first_name = form.cleaned_data.get("user_first_name")
        last_name = form.cleaned_data.get("user_last_name")
        contact = form.cleaned_data.get("user_contact")
        email = form.cleaned_data.get("user_email")
        city = form.cleaned_data.get("user_city")
        state = form.cleaned_data.get("user_state")

        new_user = form.save()
        print(new_user.user_name)
        return render(request, 'accounts/userpage.html',{'name':new_user.user_name})

    return render(request, "accounts/register.html",context)    
