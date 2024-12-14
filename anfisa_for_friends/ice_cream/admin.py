from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Category
# ...и регистрируем её в админке: 
# admin.site.register(Category)
from .models import IceCream, Topping, Wrapper

admin.site.empty_value_display = 'Не задано' 


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)

class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )

# Регистрируем кастомное представление админ-зоны
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)

