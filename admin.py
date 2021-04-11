from django.contrib import admin
from .models import Role, Volunteer, Membership, Participant, ParticipantStatus, Payment, \
    Donation, Donator, Activity, Delivery
from django.db.models import Value
from django.db.models.functions import Concat


# Register your models here.
@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    date_hierarchy = 'ActivityDate'
    fieldsets = (
            (None, {
                'fields': (("ActivityDate", "ActivityType"), "HoursWorked")
            }),

        )

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    pass


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'Email', 'PhoneNumber')
    list_filter = ('Faculty', 'Major')
    search_fields = ['FirstName']

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'Email', 'PhoneNumber', 'ForeignStudent', 'Status')
    list_filter = ('Faculty', 'Major', 'ForeignStudent')
    search_fields = ['FirstName']


@admin.register(ParticipantStatus)
class ParticipantStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Donator)
class DonatorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'Email', 'PhoneNumber')
    search_fields = ['FirstName']


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_filter = ('DonationType',)

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    pass