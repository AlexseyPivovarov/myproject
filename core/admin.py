from django.contrib import admin
from .models import Category, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_name']
    list_display = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['product_category', 'product_name', 'product_image',
              'product_info', 'product_price', 'product_status', 'product_vip',
              'product_vip_moderation']
    list_display = ('product_name', 'product_category', 'product_image',
                    'product_price', 'product_status', 'product_vip', 'product_vip_moderation',
                    'product_datatime_creation')
    list_filter = ('product_status', 'product_vip_moderation')
    actions = ['make_active', 'make_deleted', 'make_vip']
    list_editable = ('product_status', 'product_vip', 'product_vip_moderation')

    def make_active(self, request, queryset):
        queryset.update(product_status=Product.ACTIVE)

    def make_vip(self, request, queryset):
        queryset.update(product_vip=Product.VIP, product_vip_moderation=Product.STANDART)

    def make_deleted(self, request, queryset):
        queryset.update(product_status=Product.DELETED)

    make_active.short_description = "Mark selected as Active"
    make_deleted.short_description = "Mark selected as Delete"
    make_vip.short_description = "Mark selected as VIP"

# admin.site.register(Category)
# admin.site.register(Product)