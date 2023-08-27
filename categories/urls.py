from django.urls import path
from .views import category_upload_view
from .views import category_list
from .views import category_detail
from .views import category_update_view
from .views import delete_category

urlpatterns = [
    path('category/upload',category_upload_view, name='category_upload_view'),
    path("category/list", category_list, name="category_list"),
    path("product/<int:id>/",category_detail, name="category_detail"),
    path("product/edit/<int:id>/", category_update_view, name="category_update_view"),
    path("product/delete/<int:id>/", delete_category , name="delete_category"),
]