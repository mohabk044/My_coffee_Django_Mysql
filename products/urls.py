from django.urls import path
from . import views

urlpatterns = [
    path("", views.products, name="products"),
    # path("products", views.products, name="products"),
    # path("product", views.product, name="product"),
    path("<int:pro_id>", views.product, name="product"),
    path("search", views.search, name="search"),
]
