# /workspaces/ProjectUG/UGweb/lostxfound/urls.py
from django.urls import path
from . import views

app_name = 'lostxfound'

urlpatterns = [
    path('', views.home, name='home'),  # Corrected this line
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('item/<int:id>/<slug:slug>/', views.item_detail, name='item_detail'),
    path('report/<int:id>/', views.report_detail, name='report_detail'),
]
