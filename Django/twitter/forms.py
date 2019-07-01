from django import forms


class AddTweetForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label="tweet")
