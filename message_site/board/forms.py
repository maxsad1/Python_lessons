from django import forms


class NewMessageForm(forms.Form):
    author_name = forms.CharField(label="Ваше имя", max_length="100")
    author_mail = forms.EmailField(label="Ваш e-mail")
    text = forms.CharField(label="Текс", max_length="1024", widget=forms.Textarea)
