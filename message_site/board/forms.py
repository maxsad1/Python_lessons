from django import forms


class NewMessageForm(forms.Form):
    text = forms.CharField(label="Текст", max_length="1024", widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(label="Логин", max_length="200")
    password = forms.CharField(label="Пароль", max_length="200", widget=forms.PasswordInput)
