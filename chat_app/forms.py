from django import forms
from chat_app.models import Message, Answer


class MessengerForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver','content']

class Answer_message(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

class Create_a_new_message(forms.Form):
    content = forms.CharField(widget=forms.TextInput)