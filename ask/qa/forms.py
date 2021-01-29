from django import forms
from qa.models import Answer,Question
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=255,widget=forms.Textarea)
    def clean(self):
        return self.cleaned_data
    def save(self):
        self.cleaned_data['author'] = self._user
        q = Question(**self.cleaned_data)
        q.save()
        return q

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=255)
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    def clean(self):
        return self.cleaned_data
    def save(self):
        self.cleaned_data['author'] = self._user
        a = Answer(**self.cleaned_data)
        a.save()
        return a

class UserForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    def clean(self):
        return self.cleaned_data
    #save and login
    def save(self,request):
        u = User.objects.create_user(**self.cleaned_data)
        u.save()
        login(request, u)
        return u

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    def clean(self):
        return self.cleaned_data
    def save(self, request):
        user = authenticate(**self.cleaned_data)
        if user is not None:
            login(request, user)