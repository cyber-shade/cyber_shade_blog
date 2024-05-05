from django.contrib import messages


def url_message(request, message, type):
    previous_page = request.META.get('HTTP_REFERER')
    if type == 'success':
        message_tag = messages.SUCCESS
    else:
        message_tag = messages.ERROR
    messages.add_message(request, message_tag, message)
    return previous_page
