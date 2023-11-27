from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.home,name="Home"),
    path('Add/',views.form_view,name="Add"),
    path('certificate/<int:pk>',views.certificate_view,name="certificate_template"),
    path('delete/<int:pk>',views.remove_element,name="remove_element"),
    path('sendMail/<int:pk>',views.Mail_cert,name="Mail_cert")
]