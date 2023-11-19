from django.contrib import admin
from .models import Book,Author,Review


class BookAdmin(admin.ModelAdmin):
    list_display=['title',]
    search_fields=['title']
   
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name',]
    search_fields=['name']


admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Review)


# Register your models here.
