# from django.views.generic import ListView, DetailView
# from .models import Product, Category
# from datetime import datetime

# class ProductsList(ListView):
#     model = Product  # указываем модель, объекты которой мы будем выводить
#     template_name = 'products.html'  # указываем имя шаблона, в котором будет лежать HTML, в нём будут все инструкции о том, как именно пользователю должны вывестись наши объекты
#     context_object_name = 'products'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
#     queryset = Product.objects.order_by('-id')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['time_now'] = datetime.utcnow()
#         return context

# # создаём представление, в котором будут детали конкретного отдельного товара
# class ProductDetail(DetailView):
#     model = Product # модель всё та же, но мы хотим получать детали конкретно отдельного товара
#     template_name = 'product.html' # название шаблона будет product.html
#     context_object_name = 'product' # название объекта

from django.shortcuts import render
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView # импортируем уже знакомый generic 
from django.core.paginator import Paginator # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from datetime import datetime
 
from .models import New, Category
from .filters import NewFilter # импортируем недавно написанный фильтр
from .form import NewForm
 
# Create your views here.
 
class News(ListView):
    model = New
    template_name = 'new_list.html'
    context_object_name = 'news'
    # ordering = ['']
    paginate_by = 1 # поставим постраничный вывод в один элемент
    form_class = NewForm
 
 
    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        context['time_now'] = datetime.utcnow()
        return context
    
    # дженерик для получения деталей о товаре
class NewDetailView(DetailView):
    template_name = 'simpleapp/new_detail.html'
    queryset = New.objects.all()
 
 
# дженерик для создания объекта. Надо указать только имя шаблона и класс формы который мы написали в прошлом юните. Остальное он сделает за вас
class NewCreateView(CreateView):
    template_name = 'simpleapp/new_create.html'
    form_class = NewForm

class NewUpdateView(UpdateView):
    template_name = 'simpleapp/new_create.html'
    form_class = NewForm
 
    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return New.objects.get(pk=id)
 
# дженерик для удаления товара
class NewDeleteView(DeleteView):
    template_name = 'simpleapp/new_delete.html'
    queryset = New.objects.all()
    success_url = '/news/'

class Search(ListView):
    model = New
    template_name = 'simpleapp/search.html'
    context_object_name = 'news'
    # ordering = ['']
    paginate_by = 1 # поставим постраничный вывод в один элемент
    form_class = NewForm
 
 
    def get_context_data(self, **kwargs): # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = NewFilter(self.request.GET, queryset=self.get_queryset()) # вписываем наш фильтр в контекст
        return context