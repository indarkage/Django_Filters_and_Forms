from django.forms import ModelForm
from .models import New
 
 
# Создаём модельную форму
class NewForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = New
        fields = ['author', 'category', 'name']