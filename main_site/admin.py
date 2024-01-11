from django.contrib import admin
from .models import Review, Zaved, Menu, ZavedImage, Zaved_menu, ZavedSchema, bookingTable, rating, MenuPhotos, Auth

class MenuPhotosInline(admin.TabularInline):
    model = MenuPhotos
    extra = 2

class ZavedImageInline(admin.TabularInline):
    model = ZavedImage
    extra = 1

class BookingInline(admin.TabularInline):  # Renamed to avoid conflict with model name
    model = bookingTable
    extra = 1

class ZavedSchemaInline(admin.TabularInline):
    model = ZavedSchema
    extra = 1

class ZavedMenuInline(admin.TabularInline):
    model = Zaved_menu
    extra = 3

@admin.register(Auth)
class AuthAdmin(admin.ModelAdmin):
    inlines = [BookingInline]

@admin.register(Zaved)
class ZavedAdmin(admin.ModelAdmin):
    inlines = [ZavedSchemaInline, ZavedImageInline, ZavedMenuInline, BookingInline, MenuPhotosInline]

# Register other models here.
admin.site.register(rating)
admin.site.register(bookingTable)
