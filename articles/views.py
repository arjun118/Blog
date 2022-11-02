from typing import List
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView,FormView
from .models import Article
from django.urls import reverse_lazy, reverse
from .forms import CommentForm
from django.views import View
from django.views.generic.detail import SingleObjectMixin
# Create your views here.
class CommentPost(SingleObjectMixin,FormView):
    model = Article
    form_class = CommentForm
    template_name="article_detail.html"

    def post(self,request,*args,**kwargs):
        self.object=self.get_object()
        return super().post(request,*args,**kwargs)

    def form_valid(self,form):
        comment= form.save(commit=False)
        comment.article=self.object
        comment.author=self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        article=self.get_object()

        return reverse("article_detail",kwargs={"pk":article.pk})

class ArticleListView(ListView):
    model = Article
    template_name= "article_list.html"


class ArticleDetailView(LoginRequiredMixin,DetailView):
    def get(self,request,*args,**kwargs):
        view =CommentGet.as_view()
        return view(request,*args,**kwargs)


    def post(self,request,*args,**kwargs):
        view = CommentPost.as_view()

        return view(request,*args,**kwargs)


class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"
    success_url= reverse_lazy("article_list")
    def test_func(self):
        obj = self.get_object()
        return obj.author==self.request.user


class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url= reverse_lazy("article_list")
    def test_func(self):
        obj = self.get_object()
        return obj.author==self.request.user

    

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model= Article
    fields= (
        "title",
        "body",
        
    )

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # the above method is used for user authorization

    template_name="article_new.html"
    success_url = reverse_lazy("article_list")


class CommentGet(DetailView):
    model = Article
    template_name ="article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=CommentForm()
        return context





