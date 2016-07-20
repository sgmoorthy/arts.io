from django.contrib import admin

from .models import ArtPiece, Gallery


class ArtPieceInline(admin.TabularInline):
    fields = ['title', 'artist', 'image', 'gallery', 'pub_date']
    model = ArtPiece
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Gallery Info', {'fields': ['name', 'artist', 'description', 'pub_date']}),
        ('Gallery Ranking', {'fields': ['rank', 'total_rankers']})
    ]
    inlines = [ArtPieceInline]
    list_display = ('name', 'artist', 'rank')
    search_fields = ['name', 'artist', 'description']

    def get_readonly_fields(self, request, obj=None):
        return ['rank', 'total_rankers']


class ArtPieceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'artist', 'image', 'gallery', 'pub_date']}),
    ]
    list_filter = ['artist', 'pub_date']
    search_fields = ['title', 'artist']


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ArtPiece, ArtPieceAdmin)
