from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy
from . import forms
from . import models
# Create your views here.

class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'pk'
    template_name = 'car_detail.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context