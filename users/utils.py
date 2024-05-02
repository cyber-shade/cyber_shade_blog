from urllib.parse import urlencode
def url_message(request,message,type):
    previous_page = request.META.get('HTTP_REFERER')
    redirect_message = urlencode({'message': message, 'type' : type})
    url = '{}?{}'.format(previous_page, redirect_message)
    return url