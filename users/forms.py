from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import all_users

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email', 'password1', 'password2')

        labels = {
        'password1':'Password',
        'password2':'Confirm Password'
        }


class all_users(forms.ModelForm):
    bio = forms.CharField(required=False)
    class5 = 'class5'
    class6 = 'class6'
    class7 = 'class7'
    class8 = 'class8'
    class9 = 'class9'
    class10 = 'class10'
    class_list = [
        (class5,'Class-5'),
        (class6,'Class-6'),
        (class7,'Class-7'),
        (class8,'Class-8'),
        (class9,'Class-9'),
        (class10,'Class-10'),
    ]
    class_list = forms.ChoiceField(required=True, choices=class_list)
    

    class Meta():
        model = all_users
        fields = ('bio', 'profile_pic')

