# from .models import Comment
# from django_ckeditor_5.widgets import CKEditor5Widget
# from django import forms

# class CommentForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["content"].required = False
#     class Meta:
#         model = Comment
#         fields = ('content',  "reply_to")
#         labels = {
#             'content': ('نظر'),
#             'reply_to':('پاسخ به')
#         }
#         error_messages = {
#             'content': {
#                 'max_length': ("متن نظر طولانی است."),
#             },
#         }
            
