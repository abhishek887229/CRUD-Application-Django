from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.addnew,name='add_show'),
    path("update/<int:id>/", views.addupdate, name='update_data'),
    path('delete/<int:id>/', views.delete_data, name='delete_data')
]
