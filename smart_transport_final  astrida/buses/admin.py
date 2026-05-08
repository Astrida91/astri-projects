import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Bus

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'route', 'plate_number', 'capacity', 'is_active','driver')  # Updated fields
    list_filter = ('is_active', 'route', 'plate_number')  # Filter by status and route
    search_fields = ('name', 'route', 'plate_number')  # Search by these fields

    # Optional: Add ordering
    ordering = ('name',)

    # Optional: Configure fieldsets for a better detail view
    fieldsets = (
        (None, {
            'fields': ('name', 'route', 'plate_number', 'capacity', 'is_active','driver')
        }),
    )

    # Add the CSV export action
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        # Create a response object and set the content type to CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=buses.csv'
        writer = csv.writer(response)

        # Write the header row
        writer.writerow(['Name', 'Route', 'Plate Number', 'Capacity', 'Is Active','Driver'])

        # Write data rows
        for bus in queryset:
            writer.writerow([bus.name, bus.route, bus.plate_number, bus.capacity, bus.is_active, bus.driver])

        return response

    # Set the title for the action
    export_as_csv.short_description = "Export selected buses as CSV"
