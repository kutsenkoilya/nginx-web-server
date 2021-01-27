from django import forms
from qa.views import Answer,Question

class AskForm(forms.Form):
    title = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    def clean_title(self):
        title = self.clean_data['title']
        if len(title) == 0:
            raise forms.ValidationError(u'Empty Title', code='eTitle')
        return title
    def clean_text(self):
        text = self.clean_data['text']
        if len(text) == 0:
            raise forms.ValidationError(u'Empty text', code='eText')
        return text
    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q

class AnswerForm(forms.Form):
    title = forms.CharField(max_length=255)
    question = forms.ModelChoiceField(queryset=Question.objects.all(), empty_label=None)
    def clean_title(self):
        title = self.clean_data['title']
        if len(title) == 0:
            raise forms.ValidationError(u'Empty Title', code='eTitle')
        return title
    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a.question
