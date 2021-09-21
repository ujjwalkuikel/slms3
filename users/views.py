from users.forms import UserForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from users.forms import all_users,UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from courses.models import Standard, Subject, Lesson

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/user_login")
    else:
        # cl = Standard.objects.all()
        # context = {"cl":cl}
        return render(request,'courses/courses.html')

   # return render(request,'courses/courses.html')



def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = all_users(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = all_users()

    return render(request, 'users/register.html',
                            {'registered':registered,
                             'user_form':user_form,
                             'profile_form':profile_form})


#logins
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("Please use correct id and password")
            # return HttpResponseRedirect(reverse('register'))

    else:
        return render(request, 'users/login.html')




##############logoutttttttttttttttt
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))



def viewProfile(request):
    return render(request, 'users/viewProfile.html')