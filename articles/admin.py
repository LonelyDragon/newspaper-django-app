from django.contrib import admin
from django.urls.base import clear_script_prefix


from .models import Article, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)