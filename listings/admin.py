from django.contrib import admin
from .models import Listing

# showing more information in the admin panel
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    # Adding a link to the title so it also brings you to the Listings
    list_display_links = ('id', 'title')
    # makes the is_published a checkbox in the admin/listings
    list_editable = ('is_published'),
    # adds in a filter
    list_filter = ('realtor',)
    # adding a search bar
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # adds pegenation
    list_per_page = 25

# Register your models here.
admin.site.register(Listing, ListingAdmin)
