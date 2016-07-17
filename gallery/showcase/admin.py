from django.contrib import admin

from .models import ArtPiece


class ArtPieceAdmin(admin.ModelAdmin):
    fields = ['title', 'artist', 'image', 'pub_date']


admin.site.register(ArtPiece, ArtPieceAdmin)
