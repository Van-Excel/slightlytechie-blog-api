from django.urls import path

from .views import BlogList, BlogDetail


urlpatterns = [
    path('<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('', BlogList.as_view(), name='blog_list'),
]
