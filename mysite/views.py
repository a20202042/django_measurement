from django.shortcuts import render
from mysite import models,forms
from django.http import HttpResponse, HttpResponseRedirect
import base64, os
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Create your views here.

def index(request):
    return render(request, 'index.html', locals())

def project_form(request):
    project_form = forms.Project()
    try:
        if request.method == 'POST':
            project_form = forms.Project(request.POST)
            if project_form.is_valid():
                project_form.save()
                return HttpResponseRedirect('/form_work_order')
            else:
                pass
    except:
        pass
    return render(request, 'form/form_project.html', locals())
def work_order(request):
    work_order_form = forms.Work_order()
    try:
        if request.method == 'POST':
            work_order_form = forms.Work_order(request.POST)
            if work_order_form.is_valid():
                work_order_form.save()
                print('ok')
                return HttpResponseRedirect('/form_work_order')
    except:pass
    return render(request, 'form/from_work_order_create.html', locals())

def measure_tool(request):
    measure_tool_form = forms.measure_tool()
    try:
        if request.method == 'POST':
            measure_tool_form = forms.measure_tool(request.POST)
            measure_tool_form.save()
            print('ok')
            return HttpResponseRedirect('/form_measure_tool')
    except:pass
    return render(request, 'form/form_measure_tool.html', locals())

def measure_item(request):
    measure_item_form = forms.measure_item()
    # try:
    if request.method == 'POST':
        measure_item_form = forms.measure_item(request.POST, request.FILES)
        if measure_item_form.is_valid():
            measure_item_form.save()
            image_url = str(measure_item_form.instance.image.file)
            print(image_url)
            with open(image_url, "rb") as file:
                image = file.read()
                image_base64_data = base64.b64encode(image)
                image_base64_data = str(image_base64_data, "utf-8")
                measure_name = request.POST["measurement_items"]
                measure_item = models.measure_items.objects.get(measurement_items=measure_name)
                measure_item.image_base64_data = image_base64_data
                measure_item.save()
        return HttpResponseRedirect('/form_measure_item')
    # except:pass
    return render(request, 'form/form_measure_item.html', locals())