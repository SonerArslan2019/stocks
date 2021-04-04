from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    # fields = ('name', 'content',)
    # readonly_fields = ('content',)
    # fields = (('name', 'content'), ('price', 'stock_count', 'author', 'active'))

    fieldsets = (
        ('Zorunlu', {
            'fields': ('name', 'content')
        }),
        ('Opsiyonel', {
            'fields': ('price', 'stock_count'),
            'classes' : ('collapse', )
        })
    )

    exclude = ('slug',)
    list_display = ('name', 'created', 'author')
    list_filter = ('created', 'author')


admin.site.site_header = 'STOK YONETIM PANELI'
admin.site.site_title = 'Stok Yonetim Paneli'
admin.site.index_title = 'STOK YONETIMI'
admin.site.register(Product, ProductAdmin)

# Register your models here.
