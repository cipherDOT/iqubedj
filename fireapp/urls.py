from django.urls import path
from .views import index, post_form


urlpatterns = [
    path('',        index,      name = 'index'),
    path('create/', post_form,  name = 'create')
]