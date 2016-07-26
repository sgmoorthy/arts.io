from django.contrib import admin

from .models import ArtPiece, Gallery, ArtistProfile

class ArtistProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Artist Profile', {'fields': ['user', 'avatar', 'bio', 'join_date']})
    ]
    list_display = ('user', 'join_date')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['join_date', 'user']
        return ['join_date']

class ArtPieceInline(admin.TabularInline):
    fields = ['title', 'artist', 'description', 'image', 'stars', 'gallery', 'pub_date']
    model = ArtPiece
    extra = 0

    def get_readonly_fields(self, request, obj=None):
        return ['stars', 'pub_date']

class GalleryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Gallery Info', {'fields': ['name', 'artist', 'description', 'pub_date']}),
        ('Gallery Rating', {'fields': ['rating']})
    ]
    inlines = [ArtPieceInline]
    list_display = ('name', 'artist', 'rating')
    search_fields = ['name', 'description']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['rating', 'pub_date']
        return ['pub_date']


class ArtPieceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Art Info', {'fields': ['title', 'artist', 'description', 'image', 'gallery', 'pub_date']}),
        ('Art Rating', {'fields': ['stars']})
    ]
    list_filter = ['artist', 'pub_date']
    search_fields = ['title', 'artist']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['stars', 'pub_date']
        return ['pub_date']



admin.site.register(Gallery, GalleryAdmin)
admin.site.register(ArtPiece, ArtPieceAdmin)
admin.site.register(ArtistProfile, ArtistProfileAdmin)
