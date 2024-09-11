from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from budget.models import Category, SubCategory, Period
#from headquarter.forms import SignupForm, CreateFluxForm fichier déplacé vers budget
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from budget.models import Flux
from budget.forms import FluxModelForm, SignupForm #,CreateFluxForm




# Create your views here.
class FluxListView(ListView):
  model = Flux
  #template_name = flux_list.html / context_object_name = object_list




class FluxDetailView(DetailView):
  model = Flux
  #template_name = flux_detail.html / context_object_name = object




class FluxCreateView(CreateView):
  model = Flux
  form_class = FluxModelForm
  #template_name = flux_form.html / context_object_name = object
  success_url = reverse_lazy("flux-list")

  #La validation de l'instance après quelques modifications ...
  def form_valid(self, form) :
    #if request.user.is_authenticated :
    #  form.instance.author = requester.user
    form.instance.annual_amount = form.instance.period.multiplier * form.instance.amount
    return super().form_valid(form)
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["text_submit_button"] = "Créer"
    return context



class FluxUpdateView(UpdateView):
  model = Flux
  form_class = FluxModelForm
  #template_name = flux_form.html / context_object_name = object
  success_url = reverse_lazy("flux/<int:flux.pk>/")

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["text_submit_button"] = "Modifier"
    return context
  
  #La validation de l'instance après quelques modifications ...
  def form_valid(self, form) :
    #if request.user.is_authenticated :
    #  form.instance.author = requester.user
    form.instance.annual_amount = form.instance.period.multiplier * form.instance.amount
    return super().form_valid(form)
  
  def get_success_url(self) :
    return reverse_lazy('flux-detail', args=[self.object.pk])



class FluxDeleteView(DeleteView):
  model = Flux
  #template_name = flux_confirm_delete.html / context_object_name = object
  success_url = reverse_lazy('flux-list')




def all_stuffs(request):
  all_categories = Category.objects.all()
  all_subcategories = SubCategory.objects.all()
  all_periods = Period.objects.all()
  #return HttpResponse("hello")
  return render(request, 'budget/index.html', {"all_categories" : all_categories,"all_subcategories" : all_subcategories,
                                              "all_periods" : all_periods})



def all_categories(request):
  all_categories = Category.objects.all()
  return render(request, 'budget/all_categories.html', {"all_categories" : all_categories})


def all_subcategories(request):
  all_subcategories = SubCategory.objects.all()
  return render(request, 'budget/all_subcategories.html', {"all_subcategories" : all_subcategories})





def all_periods(request):
  all_periods = Period.objects.all()
  return render(request, 'budget/all_periods.html', {"all_periods" : all_periods})



def signup(request):
  if request.method == "POST":
    form = SignupForm(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
  else :
    form = SignupForm()
  return render(request, "budget/signup.html", {"form" : form})

"""
def create_flux(request):
  if request.method == "POST":
    form = CreateFluxForm(request.POST)
    if form.is_valid():
      print(form.cleaned_data)
      flux=form.save(commit=False)
      flux.annual_amount = flux.period.multiplier * flux.amount
      print(flux.annual_amount)
      flux.save()
      return HttpResponseRedirect(request.path)
  else :
    form=CreateFluxForm()
  return render(request, "budget/create_flux.html", {"form":form})
"""