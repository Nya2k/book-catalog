from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-item/', add_item, name='add_item'),
    path('create-ajax/', add_product_ajax, name='create-ajax'),
    path('add-amount/<int:id>/<int:amount>', add_amount, name='add_amount'),
    path('add-amount-ajax/', add_amount_ajax, name='add_amount_ajax'),
    path('subtract-amount/<int:id>/<int:amount>', subtract_amount, name='subtract_amount'),
    path('subtract-amount-ajax/', subtract_amount_ajax, name='subtract_amount_ajax'),
    path('delete-item/<int:id>', delete_item, name='delete_item'),
    path('delete-item-ajax/', delete_item_ajax, name='delete_item_ajax'),
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('json/user/', show_json_by_user, name='show_json_by_user'), 
]