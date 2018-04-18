from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from accounts.models import User
from . import forms
from django.contrib.auth import  get_user_model, logout

def login_page(request):
    if User.objects.exists():
        
        #user_pass = User.objects.order_by('user_pass')[0].user_pass
        form = forms.LoginForm(request.POST  or None, request.FILES)
        context = {'form': form,'a':None}
        if form.is_valid():
            #print(form.cleaned_data)
            username = form.cleaned_data.get('name')
            password = form.cleaned_data.get('passwd')
            user = User.objects.get(user_name=username)
            if username == user.user_name and password == user.user_pass:
                return render(request, 'accounts/userpage.html',{'name':username,'profile_image':user.user_image})
            else:
                context['a']='a'
                print('Error')
        return render(request,'accounts/login.html',context) 
    else:
           return HttpResponse("User doesn't exits")


def logout(request):
    context = RequestContext(request)
    logout(request)
    return render(request,'home_page/home.html',{})    

user = User()
def register_page(request):
    form =  forms.RegisterForm(request.POST or None, request.FILES or None)
    context = {
        "form":form
    }
    if form.is_valid() and request.method == "POST":
        print(form.cleaned_data)
        username = form.cleaned_data.get("name")
        password = form.cleaned_data.get("passwd")
        first_name = form.cleaned_data.get("user_first_name")
        last_name = form.cleaned_data.get("user_last_name")
        contact = form.cleaned_data.get("user_contact")
        email = form.cleaned_data.get("user_email")
        city = form.cleaned_data.get("user_city")
        state = form.cleaned_data.get("user_state")
        new_user = form.save(commit=True)
        print(new_user.user_name)
        return render(request, 'accounts/userpage.html',{'name':new_user.user_name,'profile_image':new_user.user_image})

    return render(request, "accounts/register.html",context)
