from django.contrib import admin

from .models import ArtPiece, Gallery


class ArtPieceInline(admin.TabularInline):
    fields = ['title', 'artist', 'image', 'gallery', 'pub_date']
    model = ArtPiece
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Gallery Info', {'fields': ['name', 'artist', 'pub_date']}),
    ]
    inlines = [ArtPieceInline]
    list_display = ('name',)
    search_fields = ['name',]


class ArtPieceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'artist', 'image', 'gallery', 'pub_date']}),
    ]
    list_filter = ['artist', 'pub_date']
    search_fields = ['title', 'artist']


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ArtPiece, ArtPieceAdmin)
