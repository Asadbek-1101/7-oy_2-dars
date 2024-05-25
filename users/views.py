from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth.models import User


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {"form":form})

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("data")

        form = LoginForm()
        return render(request, 'users/login.html', {"form": form})


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {"form":form})

    def post(self, request):
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            user = User()

            user.username = username
            user.first_name = first_name
            user.last_name = lastname
            user.email = email
            user.set_password(password)
            user.save()
            return redirect("data")

        form = RegisterForm
        return render(request, 'users/register.html', {"form": form})


def data(request):
    data = User.objects.all()
    return render(request, 'users/data.html', {"data":data})


def read_data(request, id):
    data = get_object_or_404(User, id=id)
    return render(request, 'users/read_data.html', {"data":data})


from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from .forms import RegisterForm

class UpdateView(View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        form = RegisterForm()
        return render(request, 'users/register.html', {"form": form})

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        form = RegisterForm(request.POST, initial=user)

        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            if password and password == confirm_password:
                user.set_password(password)
            elif password:
                form.add_error('confirm_password', "Passwords do not match.")
                return render(request, 'users/register.html', {"form": form})
            user.save()
            return redirect("data")

        return render(request, 'users/register.html', {"form": form})




def delete_data(request, id):
    data = get_object_or_404(User, id=id)
    data.delete()
    return redirect("data")




