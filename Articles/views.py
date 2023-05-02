from django.views.generic import ListView, DetailView  
from django.views.generic.edit import UpdateView, DeleteView, CreateView  
from django.urls import reverse_lazy  
from .models import Article
from .form import CommentForm

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):  
    model = Article
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
        


class ArticleUpdateView(UpdateView): 
    model = Article
    fields = (
        "title",
        "body",
    )
    template_name = "article_edit.html"


class ArticleDeleteView(DeleteView): 
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")


class ArticleCreateView(CreateView):  
    model = Article
    template_name = "article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )