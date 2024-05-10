from .models import Comment
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms

class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    class Meta:
        model = Comment
        fields = ('writer', 'content','blog', 'reply_to')
        labels = {
            'writer': ('نام'),
            'content': ('نظر'),
        }
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="default"
            )
        }
        error_messages = {
            'writer': {
                'max_length': ("نام وارد شده طولانی است"),
            },
            'content': {
                'max_length': ("متن نظر طولانی است."),
            },

        }
            
