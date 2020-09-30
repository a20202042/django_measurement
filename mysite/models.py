from django.db import models
import django.utils.timezone as timezone
import datetime, uuid,re
class project(models.Model):
    project_name = models.CharField(max_length=200)#專案名稱
    project_create_date = models.DateField(default=timezone.now)#專案建立日期
    # https: // www.itread01.com / content / 1545908112.html
    founder_name = models.CharField(max_length=100)#建立人
    remake = models.TextField(max_length=200, blank=True)#備註
    def __str__(self):
        return self.project_name

class measurement_work_order_create(models.Model):
    project_measure = models.ForeignKey(project, on_delete=models.CASCADE)
    sor_no = models.CharField(max_length=100,)#工單
    part_no = models.CharField(max_length=100,  blank=True)#件號
    number_of_parts = models.CharField(max_length=100, blank=True)#件數
    materials = models.CharField(max_length=100, blank=True)
    manufacturing_machine = models.CharField(max_length=100, blank=True)
    batch_number = models.CharField(max_length=100)
    Class = models.CharField(max_length=100, blank=True)
    inspector = models.CharField(max_length=100,  blank=True)
    remake = models.TextField(max_length=200, blank=True)
    def __str__(self):
        return self.sor_no

class measuring_tool(models.Model):
    toolname = models.CharField(max_length=50)
    tooltype = models.CharField(max_length=50)
    toolprecision = models.FloatField(max_length=50)
    tooltestdata = models.DateField(default=timezone.now)
    def __str__(self):
        return self.toolname

def upload_path_handler(instance, filename):
    name = str(instance.image)
    x = instance
    return "measure_item/{id}/{file}".format(id=instance.project_measure.project_name, file= name)    #儲存路徑和格式

class measure_items(models.Model):
    project_measure = models.ForeignKey(project, on_delete=models.CASCADE)
    too_name = models.ForeignKey(measuring_tool, on_delete=models.CASCADE)
    unit = (('mm', 'mm'), ('in', 'in'),)
    measure_unit = models.CharField(choices=unit, max_length=5)
    measurement_items = models.CharField(max_length=50)#量測項目名稱
    upper_limit = models.FloatField(max_length=20)#量測數值上限
    lower_limit = models.FloatField(max_length=20)#量測數值上限
    specification_center = models.FloatField(max_length=20)#量測數值中心
    number = (("1", "1"), ("3", "3"), ("5", "5"), ("7", "7"))
    measure_number = models.CharField(choices=number, max_length= 5)#量測次數
    Decimal = ((0.01, 0.01), (0.001, 0.001), (0.0001, 0.0001),)#浮點數問題
    decimal_piaces = models.FloatField(choices=Decimal)#量測小數點位數
    image = models.ImageField(upload_to=upload_path_handler)
    image_base64_data = models.TextField(max_length=100000, blank=True)

    def __str__(self):
        return self.measurement_items



class measure_values(models.Model):
    unit = (('mm', 'mm'), ('in', 'in'),)
    measure_project = models.ForeignKey(project, on_delete=models.CASCADE)
    measure_name = models.ForeignKey(measure_items, on_delete=models.CASCADE)
    measure_number = models.CharField(max_length=200)
    measure_value = models.FloatField(max_length=20)
    measure_unit = models.CharField(choices=unit, max_length=5)
    measure_time = models.DateTimeField()

    def __str__(self):
        return str(self.measure_name)

class measure_image(models.Model):
    project_name = models.ForeignKey(project, on_delete=models.CASCADE)
    measure_item = models.ForeignKey(measure_items, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='measure_item/')
    def __str__(self):
        return str(self.measure_item)