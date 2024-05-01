from .models import Comment
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    class Meta:
        model = Comment

        fields = ('writer', 'email', 'content', 'reply_to')
        labels = {
            'writer': ('نام'),
            'email': ('ایمیل'),
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
            'email': {
                'max_length': ("ایمیل طولانی است"),
            },
            'name': {
                'max_length': ("متن بسیار طولانی است"),
            },

        }
