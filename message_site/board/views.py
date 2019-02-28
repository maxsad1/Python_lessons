from django.shortcuts import render
from .models import Message
from .forms import NewMessageForm, LoginForm
from django.http import HttpResponseRedirect

# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def main(request):
    messages = Message.objects.order_by("-post_date")
    context = {
        "messages": messages,
    }
    return render(request, "main.html", context)


@login_required(login_url="/admin/login/")
def new_message(request):
    if request.method == "POST":
        form = NewMessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            msg = Message(user=request.user, text=text)
            msg.save()
            return HttpResponseRedirect("/")
    else:
        form = NewMessageForm()

    context = {
        "form": form,
    }
    return render(request, "new_message.html", context)


def login_view(request):
    bad = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            new_user = authenticate(username=username, password=password)
            if new_user:
                login(request, new_user)
                return HttpResponseRedirect("/")
            else:
                bad = True
    else:
        form = LoginForm()
    context = {
        "form": form,
        "bad": bad,
    }
    return render(request, "login.html", context)


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect("/")
