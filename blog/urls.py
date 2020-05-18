from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:item>/',
        views.item_detail, name='item_detail'),
]