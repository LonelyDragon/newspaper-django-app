from django.contrib import admin
from django.urls.base import clear_script_prefix


from .models import Article, Comment


class CommentInLine(admin.StackedInline):
    model = Comment
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)