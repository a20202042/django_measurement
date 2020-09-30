from django.contrib import admin
from .models import measurement_work_order_create,project,measuring_tool,measure_items,measure_values,measure_image
admin.site.register(measurement_work_order_create)
admin.site.register(project)
admin.site.register(measuring_tool)
admin.site.register(measure_items)
admin.site.register(measure_values)
admin.site.register(measure_image)
# Register your models here.
