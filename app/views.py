from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from app.models import *
# Create your views here.
class Home(TemplateView):
    template_name='app/home.html'


class Schoollist(ListView):
    model = School
    context_object_name='schools'

