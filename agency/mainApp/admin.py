from django.contrib import admin
from .models import *


class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [
        CommentInline,
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'date')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Review, ReviewAdmin)

