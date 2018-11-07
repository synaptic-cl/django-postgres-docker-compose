# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.html import format_html
from .models import Product, Family, Location#, Transaction

admin.site.register(Family)
admin.site.register(Location)
# admin.site.register(Transaction)

admin.site.site_header = 'Tiendapp header'
admin.site.site_title = 'Tiendapp title'


class ProductAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ("my_styles.css"),
        }
        js = ("my_code.js",)
    list_display = ['sku', 'title', 'unit', 'unitCost', 'quantity', 'created_at', 'account_actions']
    list_filter = ('sku', 'title', 'unit', 'unitCost', 'quantity', 'created_at', 'updated_at')
    # fields = [('family','location'),('sku','barcode'), ('title','description'),('unit', 'unitCost'), ('quantity','minQuantity')]
    fieldsets = (
        ('Section 1', {
            'fields': ('family','location')
        }),
        ('Section 2', {
            'fields': ('title','description')
        }),        
        ('Section 3', {
            'fields': ('sku','barcode','unit', 'unitCost','quantity','minQuantity')
        }),
    )
    actions = ['deposit', 'withdraw']

    def account_actions(self, obj):
        #return render_a_template('alksdjkl/qwhd/actions.html')
        return format_html(
            '<a class="button" href="">Deposit</a>&nbsp<a class="button" href="">Withdraw</a>'
        )
    account_actions.short_description = 'Account Actions'
    account_actions.allow_tags = True


class CSSAdminMixin(object):
    class Media:
        css = {
            'all': ('dashboard_solo.css'),
        }


admin.site.register(Product, ProductAdmin)
