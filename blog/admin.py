from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from django.utils.safestring import mark_safe


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):  # перевод транслитом
    form = BlogAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'time_created', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')  # ссылка
    search_fields = ('title', 'content')  # поиск
    list_filter = ('is_published', 'time_created')
    list_editable = ('is_published',)
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_created', 'time_update')
    readonly_fields = ('get_html_photo', 'time_created', 'time_update') # только чтение поле
    save_on_top = True # кнопка сохранить наверху


    def get_html_photo(self, object): # чтобы картинки было видно с главной страницы ( миниатюры)
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50"')

    get_html_photo.short_description = 'Миниатюра'


class Categorydmin(admin.ModelAdmin):  # перевод транслитом
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # поиск


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, Categorydmin)

admin.site.site_header = 'Админ-панель блога'
admin.site.site_title = 'Админ-панель блога'