from django import forms
from qa.models import Answer,Question
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=255,widget=forms.Textarea)
    def clean(self):
        return self.cleaned_data
    def save(self):
        u = User.objects.get(id=1)
        q = Question(text=self.cleaned_data['text'],title=self.cleaned_data['title'],author=u)
        q.save()
        return q

class AnswerForm(forms.Form):
    title = forms.CharField(max_length=255)
    question = forms.ModelChoiceField(queryset=Question.objects.all(), empty_label=None)
    def clean(self):
        return self.cleaned_data
    def save(self):
        u = User.objects.get(id=1)
        a = Answer(text=self.cleaned_data['text'],question=self.cleaned_data['question'],author=u)
        a.save()
        return a
