from django.contrib import admin

from applications.movie.models import Movie

@admin.register(Movie)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "owner", "like_count"]
    list_filter = ["owner"]
    search_fields = ["title"]

    def like_count(self, obj):
        return obj.likes.filter(is_like=True).count()