from django.shortcuts import render
from .models import Message
from .forms import NewMessageForm
from django.http import HttpResponseRedirect


def main(request):
    messages = Message.objects.order_by("-post_date")
    context = {
        "messages": messages,
    }
    return render(request, "main.html", context)


def new_message(request):
    if request.method == "POST":
        form = NewMessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["author_name"]
            mail = form.cleaned_data["author_mail"]
            text = form.cleaned_data["text"]
            msg = Message(author_name=name, author_mail=mail, text=text)
            msg.save()
            return HttpResponseRedirect("/")
    else:
        form = NewMessageForm()

    context = {
        "form": form,
    }
    return render(request, "new_message.html", context)
