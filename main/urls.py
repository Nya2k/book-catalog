from django.urls import path
from main.views import register, login_user, logout_user, show_main, add_item, add_amount, subtract_amount, delete_item, show_html, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add-item/', add_item, name='add_item'),
    path('add-amount/<int:id>/<int:amount>', add_amount, name='add_amount'),
    path('subtract-amount/<int:id>/<int:amount>', subtract_amount, name='subtract_amount'),
    path('delete-item/<int:id>', delete_item, name='delete_item'),
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]