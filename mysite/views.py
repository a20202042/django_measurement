from django.shortcuts import render
from mysite import models, forms
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
import base64, os, json, statistics, numpy
from django.shortcuts import get_object_or_404

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


# Create your views here.

def index(request):
    return render(request, 'index.html', locals())


def project_display_project(requset, x=None):
    projects = models.project.objects.all()
    return render(requset, 'project_display/project_display_project.html', locals())


def project_display_work_order(requset, x=None):
    work_order = models.measurement_work_order_create.objects.all()
    return render(requset, 'project_display/project_display_work_order.html', locals())


def project_display_tool(requset, x=None):
    tool = models.measuring_tool.objects.all()
    return render(requset, 'project_display/project_display_tool.html', locals())


def project_display_item(requset, x=None):
    item = models.measure_items.objects.all()
    return render(requset, 'project_display/project_display_item.html', locals())


#
# def delet(requset, id=None):
#     projects = models.project.objects.all()
#     if id:
#         try:
#             post = models.project.objects.get(id=id)
#             print(post)
#             post.delete()
#             print("刪除資料")
#         except:
#             id = None
#             print("資料未刪除")
#     return redirect('/project_display/project')

def measure_item_image_show(request, id):
    image_file = models.measure_items.objects.get(id=id)
    print(image_file.image)
    data = dict()
    return JsonResponse(data)


def delet_item(request, id):
    item = models.measure_items.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        item.delete()
        data['form_is_valid'] = True
        items = models.measure_items.objects.all()
        data['html_item_list'] = render_to_string(
            'project_display/item_banner.html',
            {'item': items})
    else:
        context = {
            'project_measure': item.project_measure, 'id': item.id,
            'tool_name': item.too_name, 'measure_unit': item.measure_unit,
            'measurement_items': item.measurement_items, 'upper_limit': item.upper_limit,
            'lower_limit': item.lower_limit, 'specification_center': item.specification_center,
            'measure_points': item.measure_points, 'measure_number': item.measure_number,
            'decimal_piaces': item.decimal_piaces, 'image': item.image
        }
        data['html_form'] = render_to_string(
            'project_display/delet/delet_item.html',
            context, request=request)
    return JsonResponse(data)


def delet_tool(request, id):
    tool = models.measuring_tool.objects.get(id=id)
    data = dict()
    if request.method == "POST":
        tool.delete()
        data['form_is_valid'] = True
        tools = models.measuring_tool.objects.all()
        data['html_tool_list'] = render_to_string(
            'project_display/tool_banner.html',
            {'tool': tools})
    else:
        context = {
            'tool_name': tool.toolname, 'id': tool.id,
            'tooltype': tool.tooltype, 'toolprecision': tool.toolprecision,
            'tooltestdata': tool.tooltestdata
        }
        data['html_form'] = render_to_string(
            'project_display/delet/delet_tool.html',
            context, request=request)

    return JsonResponse(data)


def delet_work_order(request, id):
    work_order = models.measurement_work_order_create.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        work_order.delete()
        data['form_is_valid'] = True
        work_orders = models.measurement_work_order_create.objects.all()
        data['html_work_order_list'] = render_to_string(
            'project_display/work_order_banner.html',
            {'work_order': work_orders})
    else:
        context = {
            'project': work_order.project_measure,
            'work_order': work_order.sor_no, 'id': work_order.id,
            'number_of_parts': work_order.part_no, 'materials': work_order.materials,
            'manufacturing_machine': work_order.manufacturing_machine, 'batch_number': work_order.batch_number,
            'Class': work_order.Class, 'inspector': work_order.inspector,
            'remake': work_order.remake
        }
        data['html_form'] = render_to_string(
            'project_display/delet/delet_work_order.html',
            context, request=request)

    return JsonResponse(data)


def delet_project(request, id):
    project = models.project.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        project.delete()
        data['form_is_valid'] = True
        projects = models.project.objects.all()
        data['html_project_list'] = render_to_string(
            'project_display/project_banner.html',
            {'projects': projects})
    else:
        context = {'project': project,
                   'project_name': project.project_name,
                   'founder_name': project.founder_name,
                   'time': project.project_create_date,
                   'remake': project.remake}
        data['html_form'] = render_to_string(
            'project_display/delet/delet_project.html',
            context, request=request)
    return JsonResponse(data)


def update_work_order(request, id):
    # work_order = get_object_or_404(models.measurement_work_order_create, id=id)
    work_order = models.measurement_work_order_create.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.Work_order(request.POST, instance=work_order)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            work_orders = models.measurement_work_order_create.objects.all()
            data['html_work_order_list'] = render_to_string(
                'project_display/work_order_banner.html',
                {'work_order': work_orders})
    else:
        form = forms.Work_order(instance=work_order)
    context = {'form': form}
    data['html_form'] = render_to_string(
        'project_display/update/update_work_order.html',
        context, request=request)
    return JsonResponse(data)


def update_project(request, id):
    project = get_object_or_404(models.project, id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.Project(request.POST, instance=project)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            projects = models.project.objects.all()
            data['html_project_list'] = render_to_string(
                'project_display/project_banner.html',
                {'projects': projects})
    else:
        form = forms.Project(instance=project)
    context = {'form': form}
    data['html_form'] = render_to_string(
        'project_display/update/update_project.html',
        context, request=request)
    return JsonResponse(data)


def update_tool(request, id):
    tool = get_object_or_404(models.measuring_tool, id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.measure_tool(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            tools = models.measuring_tool.objects.all()
            data['html_tool_list'] = render_to_string(
                'project_display/tool_banner.html',
                {'tool': tools})
    else:
        form = forms.measure_tool(instance=tool)
    context = {'form': form}
    data['html_form'] = render_to_string(
        'project_display/update/update_tool.html',
        context, request=request)
    return JsonResponse(data)


def update_item(request, id):
    item = models.measure_items.objects.get(id=id)
    data = dict()
    if request.method == 'POST':
        form = forms.measure_item(request.POST, instance=item)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = models.measure_items.objects.all()
            data['html_item_list'] = render_to_string(
                'project_display/item_banner.html',
                {'item': items}
            )
    else:
        form = forms.measure_item(instance=item)
    context = {'form': form}
    data['html_form'] = render_to_string(
        'project_display/update/update_measure.html',
        context, request=request)

    return JsonResponse(data)


def project_form(request):
    project_form = forms.Project()
    if request.method == 'POST':
        project_form = forms.Project(request.POST)
        if project_form.is_valid():
            project_form.save()
            return HttpResponseRedirect('/form_work_order')
    return render(request, 'form/form_project.html', locals())


def work_order(request):
    work_order_form = forms.Work_order()
    if request.method == 'POST':
        work_order_form = forms.Work_order(request.POST)
        if work_order_form.is_valid():
            work_order_form.save()
            print('ok')
            return HttpResponseRedirect('/form_measure_tool')
    return render(request, 'form/from_work_order_create.html', locals())


def measure_tool(request):
    measure_tool_form = forms.measure_tool()
    if request.method == 'POST':
        measure_tool_form = forms.measure_tool(request.POST)
        if measure_tool_form.is_valid():
            measure_tool_form.save()
            print('ok')
        return HttpResponseRedirect('/form_measure_item')
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


def test(requset):
    all_data = models.measure_values.objects.filter(measure_name_id=57).values('measure_number', 'measure_value')
    measure_item_data = models.measure_items.objects.get(id=57)
    x_line = []
    y_line = []
    x_exceed_data = []
    y_exceed_data = []
    upper_limit = measure_item_data.upper_limit
    lower_limit = measure_item_data.lower_limit
    for item in all_data:
        y_line.append(item['measure_value'])
        x_line.append(item['measure_number'])
        if item['measure_value'] > upper_limit or item['measure_value'] < lower_limit:
            x_exceed_data.append(item['measure_number'])
            y_exceed_data.append(item['measure_value'])
    x_max = str(x_line[-1])
    x_min = str(x_line[0])
    y_center = float(float(lower_limit) + ((float(upper_limit) - float(lower_limit)) / 2))
    upper_range = float(float(upper_limit) + ((float(upper_limit) - float(lower_limit)) / 2))
    loewr_range = float(float(lower_limit) - ((float(upper_limit) - float(lower_limit)) / 2))
    y = [1, 1.555, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    x = ['1-1', '1-2', '1-3', '2-1', '2-2', '2-3', '3-1', '3-2', '3-3', '4-1', '4-2', '4-3', '5-1', '5-2', '5-3', '6-1',
         '6-2', '6-3']
    data = {'x_data': json.dumps(x_line), 'y_data': json.dumps(y_line),
            'x_max': json.dumps(x_max), 'x_min': json.dumps(x_min), 'y_center': json.dumps(y_center),
            'upper_limit': json.dumps(upper_limit), 'lower_limit': json.dumps(lower_limit),
            'upper_range': json.dumps(upper_range), 'lower_range': json.dumps(loewr_range),
            'x_exceed_data': json.dumps(x_exceed_data), 'y_exceed_data': json.dumps(y_exceed_data)}
    # print(y_center)
    # print(upper_limit)
    # print(lower_limit)
    # print(y_line)
    # print(x_line)
    # print(x_max)
    # print(x_min)
    # ----------------------------------------------------------------rbar
    print('r')
    n = models.measure_items.objects.get(id=57).measure_number  # 量測次數
    print(n)
    d3_data = {'1': 1, '3': 0, '5': 0, '7': 0.076}
    d4_data = {'1': 1, '3': 2.575, '5': 2.115, '7': 1.924}
    r_all_data = []
    r_old_data = []
    r_r_data = []
    r_x_line = []
    # x軸座標
    r_number = int()
    r_r_cl = float()
    for item in all_data:
        r_old_data.append(item['measure_value'])
        r_number = r_number + 1
        if r_number == int(n):
            r_all_data.append(r_old_data)
            r_old_data = []
            r_number = 0
    print(r_all_data)  # 平均數data
    for item in r_all_data:
        r_r_data.append(numpy.max(item) - numpy.min(item))
    print(r_r_data)
    r_r_cl = statistics.mean(r_r_data)
    print(r_r_cl)  # 平均數
    d4 = d4_data[n]
    d3 = d3_data[n]
    r_ucl = r_r_cl * d4
    r_lcl = r_r_cl * d3
    r_upper_range = r_r_cl * d4 + (r_r_cl * d4) / 3
    r_lower_range = r_r_cl * d3 + (r_r_cl * d3) / 3
    print(r_r_cl, r_ucl, r_lcl)
    for i in range(1, len(r_r_data) + 1):
        r_x_line.append('(%s)' % i)  # x軸
    print(r_x_line)
    data.update({
        'r_x_data': json.dumps(r_x_line), 'r_y_data': json.dumps(r_r_data),
        'r_x_max': json.dumps(r_x_line[-1]), 'r_x_min': json.dumps(r_x_line[0]),
        'r_r_cl': json.dumps(r_r_cl), 'r_ucl': json.dumps(r_ucl),'r_lcl': json.dumps(r_lcl),
        'r_upper_range': json.dumps(r_upper_range), 'r_lower_range': json.dumps(r_lower_range)})

    # ----------------------------------------------------------------xbar
    print('x')
    n = models.measure_items.objects.get(id=57).measure_number  # 量測次數
    print(all_data, n)
    A2_data = {'1': 1, '3': 1.023}
    A2 = A2_data[n]
    print(A2)
    x_all_data = []  # 所有資料
    x_x_line = []  # x軸位數
    average_data = []  # 算數平均數
    number = int()
    x_old_data = []
    for item in all_data:
        x_old_data.append(item['measure_value'])
        number = number + 1
        if number == int(n):
            number = 0
            x_all_data.append(x_old_data)
            x_old_data = []
    print(x_all_data)
    for i in range(1, len(x_all_data) + 1):
        x_x_line.append('(%s)' % i)
    print(x_x_line)  # x軸位數
    for item in x_all_data:
        average_data.append(statistics.mean(item))  # 量測平均值data
    print(average_data)
    # 計算全距 = R
    R = float()
    x_r_data = []  # R全距all_data
    for item in x_all_data:
        x_r_data.append(numpy.max(item) - numpy.min(item))
    R = statistics.mean(x_r_data)
    # 計算總平均 = 中心線 = cl
    x_cl = statistics.mean(average_data)
    x_lcl = x_cl - A2 * R
    x_ucl = x_cl + A2 * R
    print(x_cl, x_lcl, x_ucl)
    x_upper_range = x_cl + A2 * R * 2
    x_lower_range = x_cl - A2 * R * 2
    data.update({
        'x_x_data': json.dumps(x_x_line), 'x_y_data': json.dumps(average_data),
        'x_x_max': json.dumps(x_x_line[-1]), 'x_x_min': json.dumps(x_x_line[0]),
        'x_y_center': json.dumps(x_cl), 'x_ucl': json.dumps(x_ucl),
        'x_lcl': json.dumps(x_lcl), 'x_upper_range': json.dumps(x_upper_range),
        'x_lower_range': json.dumps(x_lower_range)})
    print(data)
    return render(requset, 'test.html', data)


def test_1(requset):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    value = {'x': x, 'y': y}
    print('2')
    return JsonResponse(value)
