from django.shortcuts import render
from .models import Message
from .forms import NewMessageForm
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


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
            name = form.cleaned_data["author_name"]
            mail = form.cleaned_data["author_mail"]
            text = form.cleaned_data["text"]
            msg = Message(user=request.user, author_name=name, author_mail=mail, text=text)
            msg.save()
            return HttpResponseRedirect("/")
    else:
        form = NewMessageForm()

    context = {
        "form": form,
    }
    return render(request, "new_message.html", context)


@login_required(login_url="/admin/login/")
def secret(request):
    user = request.user
    if user.is_authenticated:
        return render(request, "secret.html")
    else:
        return render(request, "forbidden.html")
