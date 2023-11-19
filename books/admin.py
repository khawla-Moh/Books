from django.contrib import admin
from .models import Book,Author,Review


class BookAdmin(admin.ModelAdmin):
    list_display=['title',]
    search_fields=['title']
   


admin.site.register(Book,BookAdmin)
admin.site.register(Author)
admin.site.register(Review)


# Register your models here.
