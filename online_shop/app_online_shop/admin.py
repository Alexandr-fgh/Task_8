from django.contrib import admin
from .models import OnlineShop


# Register your models here


class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discription', 'price', 'created_time', 'auction']
    list_filter = ['auction', 'created_time']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    
    fieldsets = (
        ('Общее', {
            'fields':('title', 'discription')
        }),
        ('Финансы', {
            'fields':('price','auction'), 
            'classes': ['collapse']
        }),
    )



    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction =  True)
    
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction =  False)
admin.site.register(OnlineShop, OnlineShopAdmin)
