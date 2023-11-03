from django.urls import path
from . import views

app_name = "introduction_app"

urlpatterns = [
  path("", views.IndexView.as_view(), name="index"),
  path("<int:pk>", views.DetailView.as_view(), name="detail"),
  path("product/create", views.CreateProductView.as_view(), name="create_product"),
  path("product/<int:pk>/update", views.UpdateProductView.as_view(), name="update_product"),
  path("product/<int:pk>/delete", views.DeleteProductView.as_view(), name="delete_product"),
  path("skill/create", views.CreateSkillView.as_view(), name="create_skill"),
  path("skill/<int:pk>/update", views.UpdateSkillView.as_view(), name="update_skill"),
  path("skill/<int:pk>/delete", views.DeleteSkillView.as_view(), name="delete_skill"),
  path("skill/<int:pk>", views.DetailSkillView.as_view(), name="detail_skill"),

]

