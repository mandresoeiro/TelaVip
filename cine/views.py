from django.shortcuts import render
from cine.forms import CineModelForm
from django.urls import reverse_lazy
from django.views.generic import (
    
    CreateView, 
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .models import Cine

class CineListView(ListView):
    model = Cine   
    template_name = "cine.html"
    context_object_name = "cine"

     
    def get_queryset(self):
        cine = (
            super().get_queryset().order_by("title")
        )  
        search = self.request.GET.get("search")
        if search:
            cine = cine.filter(title__icontains=search)
        return cine

class CineDetailView(DetailView):
    model = Cine
    template_name = "cine_detail.html"
    context_object_name = ""

class NewCineCreateView(CreateView):
    model = Cine
    form_class = CineModelForm
    template_name = "new_cine.html"
    success_url = ""

class CineUpdateView(UpdateView):
    model = Cine
    form_class = CineModelForm
    template_name = "cine_update.html"

    def get_success_url(self):
        return reverse_lazy("cine_detail", kwargs={"pk": self.object.pk})

    # TODO Redireciona meu usuario p/ cine_detail onde o id do registro vai ser passado pk.


# TODO Utilizando DeleteView (Generic Views)


class CineDeleteView(DeleteView):
    model = Cine
    template_name = "cine_delete.html"
    success_url = "/"