from django.contrib import admin
from django.urls import path
from Djangoku import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('addnew',views.addnew),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]