from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('inscription/', views.inscription, name = 'Incription'),
    path('connexion/', views.connexion, name = 'Connexion'),
    path('acceuil_membre/', views.acceuil_membre, name = 'Acceuil'),

]

if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)