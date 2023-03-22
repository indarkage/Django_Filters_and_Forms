from django.urls import path
from .views import News, NewDetailView, NewCreateView, NewUpdateView, NewDeleteView, Search

urlpatterns = [
    path('', News.as_view()),
    path('<int:pk>', NewDetailView.as_view(), name='new_detail'),
    path('create', NewCreateView.as_view(), name='new_create'),
    path('update/<int:pk>', NewUpdateView.as_view(), name='new_update'),
    path('delete/<int:pk>', NewDeleteView.as_view(), name='new_delete'),
    path('search', Search.as_view(), name='search'),
]