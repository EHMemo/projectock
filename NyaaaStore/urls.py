from django.urls import path
from .views import home,cat_figuras,cat_poleras,cat_accesorios,\
    agregar_producto,listar_productos,modificar_producto,detalle_producto,eliminar_producto,\
    home_adm,listar_anime,agregar_anime,listar_marca,agregar_marca,listar_serie,agregar_serie

urlpatterns = [
    path('', home, name='home'),
    path('catalogo_figuras', cat_figuras, name='catalogo_figuras'),
    path('catalogo_poleras', cat_poleras, name='catalogo_poleras'),
    path('catalogo_accesorios', cat_accesorios, name='catalogo_accesorios'),
    # URLS VISTA ADMIN
    path('vista-amd/', home_adm, name='vista-adm'),
    # FIN URLS VISTA ADMIN
    # URLS FORMULARIO ANIME
    path('listar-anime/', listar_anime, name='listar_anime'),
    path('agregar-anime/', agregar_anime, name='agregar_anime'),
    # FIN URLS FORMULARIO ANIME
    # URLS FORMULARIO MARCA
    path('listar-marca/', listar_marca, name='listar_marca'),
    path('agregar-marca/', agregar_marca, name='agregar_marca'),
    # FIN URLS FORMULARIO MARCA
    # URLS FORMULARIO SERIE
    path('listar-serie/', listar_serie, name='listar_serie'),
    path('agregar-serie/', agregar_serie, name='agregar_serie'),
    # FIN URLS FORMULARIO SERIE
    # URLS CRUD PRODUCTO DESDE ADMIN

    path('agregar-producto/', agregar_producto, name='agregar_producto'),
    path('listar-producto/', listar_productos, name='listar_producto'),
    path('modificar-producto/<id>/', modificar_producto, name='modificar_producto'),
    path('detalle-producto/<id>/', detalle_producto, name='detalle_producto'),
    path('eliminar-producto/<id>/', eliminar_producto, name='eliminar_producto'),
    # FIN URLS CRUD PRODUCTO DESDE ADMIN
]