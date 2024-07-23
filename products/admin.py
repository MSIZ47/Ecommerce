from django.contrib import admin
from .models import Product, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['product', 'user', 'text', 'score_stars']
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'is_active']
    inlines = [
        CommentInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'text']
