from django import forms
from qa.models import Answer,Question

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=255,widget=forms.Textarea)
    def clean(self):
        return self.cleaned_data
    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q

class AnswerForm(forms.Form):
    text = forms.CharField(max_length=255)
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    def clean(self):
        return self.cleaned_data
    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a
