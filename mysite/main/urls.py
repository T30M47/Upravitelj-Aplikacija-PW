from django.urls import path
from . import views
from main.views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', AplikacijaList.as_view()),
    path('<aplikacija_naziv>', AplikacijaPregledList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)