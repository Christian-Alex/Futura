from django.urls import path

from .views.categories_view import categories_view, categories_edit
from .views.documents_view import document_view, documents_edit
from .views.clients_view import clients_view, clients_edit
from .views.delivery_view import deliverys_view, deliverys_edit
from .views.products_view import products_view, products_edit
from .views.invoce_view import invoces_view, invoces_edit
from .views.order_view import orders_view, orders_edit
from .views.for_login_view import verifyClient

urlpatterns = [
    path('categorias/', categories_view),
    path('categorie_info/<int:id>', categories_edit, name= "edit_categories"),

    path('documentos/', document_view),
    path('document_info/<int:id>', documents_edit, name= "edit_categories"),

    path('clientes/', clients_view, name= "view_clients"),
    path('client_info/<int:id>', clients_edit, name= "edit_clients"),

    path('repartidores/', deliverys_view, name= "view_deliveryes"),
    path('deliveryes_info/<int:id>', deliverys_edit, name= "edit_deliveryes"),

    path('productos/', products_view, name= "view_products"),
    path('product_info/<int:id>', products_edit, name= "edit_products"),

    path('facturas/', invoces_view, name= "view_invoces"),
    path('invoce_info/<int:id>', invoces_edit, name= "edit_invoces"),

    path('entregas/', orders_view, name= "view_orders"),
    path('order_info/<int:id>', orders_edit, name= "edit_orders"),

    ######################################################
    path('client/<int:id>', verifyClient, name= "verifyExist"),
]
