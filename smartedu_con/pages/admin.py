from django.contrib import admin
from . models import Contact

#admin.site.register(Contact)

@admin.register(Contact)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'date')
    search_fields = ('first_name', 'last_name', 'phone')