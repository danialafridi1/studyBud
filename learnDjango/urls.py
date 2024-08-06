from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from django.http import HttpResponse as HTTPResponse # type: ignore
def home(request):
    return HTTPResponse('Hello, World!')

def room(request):
    return HTTPResponse("Room")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('room/',room),
]
