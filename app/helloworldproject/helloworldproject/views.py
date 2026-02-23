from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunc( request ):
    responseObject = HttpResponse('<h1>hello world</h1>')
    return responseObject

class helloWorldClass( TemplateView ):
    template_name = 'hello.html'
