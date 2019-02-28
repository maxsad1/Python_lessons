from django.shortcuts import render
from .models import Message
from .forms import NewMessageForm
from django.http import HttpResponseRedirect, HttpResponse
import json
from random import choice

# from django.contrib.auth.models import User
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


def random_view(request):
    return render(request, "random.html")


def get_phrase(request):
    phrases = [
        "Привет!",
        "Пока!",
        "Как оно?",
        "Ок"
    ]
    phrase = choice(phrases)
    data = {"phrase": phrase}
    return HttpResponse(json.dumps(data))
