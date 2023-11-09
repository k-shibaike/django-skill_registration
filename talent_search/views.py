from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from introduction_app.models import Skill, Product


class IndexView(generic.ListView): 
  model = User
  template_name = 'talent_search/index.html'

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートに渡すデータを追加
        context['product_list'] = Product.objects.all()
        context['skill_list'] = Skill.objects.all()
        return context
  
class DetailView(generic.DetailView):
    model=User
    template_name = 'talent_search/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートに渡すデータを追加
        context['product_list'] = Product.objects.all()
        context['skill_list'] = Skill.objects.all()
        return context


