from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('List/',views.list,name="student list"),
    # path('Add/',views.form_view,name="Add")
]