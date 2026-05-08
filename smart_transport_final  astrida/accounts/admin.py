import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    # Add custom fields to the user list display
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'role')
    ordering = ('username',)

    # Specify the fields to display on the user detail page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'birth_date', 'profile_picture')}),  # Add custom fields here
    )

    # Add role and other custom fields to the user creation page
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'birth_date', 'profile_picture')}),  # Add custom fields here
    )

    # Custom action for exporting users as CSV
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        # Create the HTTP response object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="custom_users.csv"'

        # Create the CSV writer.
        writer = csv.writer(response)

        # Write the header row.
        writer.writerow(['Username', 'Email', 'Role', 'Is Staff', 'Is Active', 'Date Joined'])

        # Write data rows.
        for user in queryset:
            writer.writerow([user.username, user.email, user.role, user.is_staff, user.is_active, user.date_joined])

        return response

    export_as_csv.short_description = "Export Selected Users as CSV"

# Register the models with the custom admin classes
admin.site.register(CustomUser, CustomUserAdmin)

