"""untitled13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from mysite import views
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('test/', views.test),
                  path('test_t/', views.test_1, name='test'),
                  path('', views.index),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('form_project/', views.project_form),
                  path('form_work_order/', views.work_order),
                  path('form_measure_tool/', views.measure_tool),
                  path('form_measure_item/', views.measure_item),
                  path('project_display/project/', views.project_display_project),
                  path('project_display/work_order/', views.project_display_work_order),
                  path('project_display/tool/', views.project_display_tool),
                  path('project_display/item/', views.project_display_item),
                  # path('delet/<str:id>', views.delet),
                  path('delet/project/<str:id>', views.delet_project, name='project_delet'),
                  path('update/project/<str:id>', views.update_project, name='update_project'),
                  path('delet/work_order/<str:id>', views.delet_work_order, name='work_order_delet'),
                  path('update/work_order/<str:id>', views.update_work_order, name='update_work_order'),
                  path('delet/measure_tool/<str:id>', views.delet_tool, name='tool_delet'),
                  path('update/measure_tool/<str:id>', views.update_tool, name='update_tool'),
                  path('delet/measure_item/<str:id>', views.delet_item, name='item_delet'),
                  path('update/v/<str:id>', views.update_item, name='update_item'),
                  path('item_image/<str:id>', views.measure_item_image_show, name='items_image_show'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
