from django import froms
from .models import Topic

class TopicForm(forms.ModelForm):
    class meta:
        model = Topic
        field = ['text']
        label = {'text':''}
        