from django import forms
from accounts.models import User

class LoginForm(forms.Form):
    name = forms.CharField()
    passwd = forms.CharField(widget = forms.PasswordInput)


user = User()
class RegisterForm(forms.ModelForm):
    user_pass = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = '__all__' 

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        qs = User.objects.filter(user_name=user_name)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return user_name

    def clean_user_email(self):
        user_email = self.cleaned_data.get('user_email')
        qs = User.objects.filter(user_email = user_email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return user_email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('user_pass')
        password2 = self.cleaned_data.get('password2')
        if password2 != password :
            raise forms.ValidationError("Password must match")  
        return data               
    