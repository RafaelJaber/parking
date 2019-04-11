from django.contrib import admin
from .models import (
    Brand, 
    Vehicle, 
    Person, 
    Parameters, 
    MoveRotary,
    MoveMonthly,
    Monthly
)

class MoveRotaryAdmin(admin.ModelAdmin):
    list_display = (
        'checkin', 
        'checkout', 
        'value_our', 
        'total',
        'paid',
        'total_hours',
        'vehicle'
        )


class MonthlyAdmin(admin.ModelAdmin):
    list_display = (
        'moveMonthly',
        'date_paid',
        'total',
    )


admin.site.register(Brand)
admin.site.register(Vehicle)
admin.site.register(Person)
admin.site.register(Parameters)
admin.site.register(MoveRotary, MoveRotaryAdmin)
admin.site.register(MoveMonthly)
admin.site.register(Monthly, MonthlyAdmin)
