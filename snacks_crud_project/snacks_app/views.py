from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Snack
# Create your views here.


class SnackListView(ListView):
    model = Snack
    template_name = 'home.html'


class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snack_detail.html'


class SnackAddNew(CreateView):
    model = Snack
    template_name = "snack_new.html"
    fields = ['title', 'description', 'purchaser']


class SnackUpdateView(UpdateView):
    model = Snack
    template_name = "snack_update.html"
    fields = ['title', 'description', 'purchaser']


class SnackDeleteView(DeleteView):
    model = Snack
    template_name = "snack_delete.html"
    success_url = reverse_lazy('home')
