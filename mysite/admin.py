from django.contrib import admin
from .models import measurement_work_order,project,measuring_tool,measure_items,measure_values,work_order_measure_items

admin.site.register(measurement_work_order)
admin.site.register(project)
admin.site.register(measuring_tool)
admin.site.register(measure_items)
admin.site.register(measure_values)
admin.site.register(work_order_measure_items)
# admin.site.register(measure_image)
# admin.site.register(measure_image)
# Register your models here.
