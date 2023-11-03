from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

from . forms import ProductForm, SkillForm
from . models import Skill, Product


class IndexView(generic.ListView):
    model = Skill
    template_name = 'introduction_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートに渡すデータを追加
        context['product_list'] = Product.objects.filter(
            author=self.request.user.id)
        context['skill_list'] = Skill.objects.filter(
            author=self.request.user.id)
        return context


class DetailView(generic.DetailView):
    model = Product

class DetailSkillView(generic.DetailView):
    model = Skill

class CreateProductView(generic.CreateView):
    model = Product
    form_class = ProductForm

    def form_valid(self, form):
        # authorにログインしているユーザー名を代入
        form.instance.author = self.request.user
        return super(CreateProductView, self).form_valid(form)


class CreateSkillView(generic.CreateView):
    model = Skill
    form_class = SkillForm

    def form_valid(self, form):
        # authorにログインしているユーザー名を代入
        form.instance.author = self.request.user
        return super(CreateSkillView, self).form_valid(form)


class UpdateProductView(generic.UpdateView):
    model = Product
    form_class = ProductForm

    def dispatch(self, request, *args, **kwargs):
        # 現在の表示データのデータを取得
        obj = self.get_object()

        # データのauthorを画面を表示しているユーザーと比較
        if obj.author != self.request.user:
            # エラーの場合、以下メッセージを表示
            raise PermissionDenied('You do not have permission to edit.')
        return super(UpdateProductView, self).dispatch(request, *args, **kwargs)


class UpdateSkillView(generic.UpdateView):
    model = Skill
    form_class = SkillForm

    def dispatch(self, request, *args, **kwargs):
        # 現在の表示データのデータを取得
        obj = self.get_object()
        print(obj.author)
        print(self.request.user)
        # データのauthorを画面を表示しているユーザーと比較
        if obj.author != self.request.user:
            # エラーの場合、以下メッセージを表示
            raise PermissionDenied('You do not have permission to edit.')
        return super(UpdateSkillView, self).dispatch(request, *args, **kwargs)


class DeleteProductView(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('introduction_app:index')


class DeleteSkillView(generic.DeleteView):
    model = Skill
    success_url = reverse_lazy('introduction_app:index')
