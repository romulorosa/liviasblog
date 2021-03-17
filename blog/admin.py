from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'author')
    list_filter = ("status",)
    search_fields = [
        'title', 'content', 'author__first_name', 'author__last_name', 'author__username'
    ]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
