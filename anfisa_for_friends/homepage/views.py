from django.shortcuts import render
from ice_cream.models import IceCream
from django.db.models import Q

def index(request):
    template_name = 'homepage/index.html'
    # Запрос:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
        # Верни только те объекты, у которых ...
        ).filter(
            is_published=True, is_on_main=True
        # Сортировка в модуле по титлу 
        # [1:4] - означает количество записей, которые будут выведены. 
        # Всего количество записей: (4 - 1)
        ).order_by('title')[1:4] 
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)
