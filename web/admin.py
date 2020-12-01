from django.contrib import admin

from .models import Category, Item, Owner, Restaurant, Order


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'user', 'company_name', 'address')
    search_fields = ['company_name']

    def fullname(self, obj):
        return "{} {}".format(obj.user.first_name, obj.user.last_name)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'website')
    search_fields = ['name', 'phone']


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'restaurant', 'price')
    search_fields = ['title']
    list_filter = ['category']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_no', 'restaurant', 'item', 'price',
                    'status', 'created_at', 'updated_at')
    search_fields = ['order_no']
    list_filter = ['status']


admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Owner, OwnerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
