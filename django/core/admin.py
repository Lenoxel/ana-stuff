from django.contrib import admin

from .models import Product, Category, Evaluation, SendMessage

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Evaluation)
admin.site.register(SendMessage)