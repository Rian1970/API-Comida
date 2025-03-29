import pytest
from src.services.producto_service import (
    obtener_productos,
    obtener_producto_por_categoria,
    crear_producto,
    actualizar_producto,
    eliminar_producto
)
from src.models.producto import Producto
from src.schemas.producto import ProductoSchema, ProductoUpdate

# Obtener todos los productos (debe retornar una lista vacía al inicio)
def test_obtener_productos_vacio(db_session):
    productos = obtener_productos(db_session)
    assert productos == []

# Crea un producto correctamente
def test_crear_producto(db_session):
    producto_data = ProductoSchema(
        nombre = "Coca cola",
        descripcion = "Una bebida refrescante",
        precio = 19.55,
        categoria = "Bebidas"
    )

    response = crear_producto(producto_data, db_session)

    assert response["message"] == "Producto creado correctamente"
    assert db_session.query(Producto).count() == 1

# Obtener un producto por categoría
def test_obtener_producto_por_categoria(db_session):
    producto_data = ProductoSchema(
        nombre = "Coca cola",
        descripcion = "Una bebida refrescante",
        precio = 19.55,
        categoria = "Bebidas"
    )

    crear_producto(producto_data, db_session)

    productos = obtener_producto_por_categoria("Bebidas", db_session)

    assert len(productos) == 1
    assert productos is not None 

# Obtener productos con categoría inexistente
def test_obtener_producto_por_categoria_no_existente(db_session):
    productos = obtener_producto_por_categoria("Pollos", db_session)
    assert productos == []

# Actualizar un producto existente
def test_actualizar_producto(db_session):
    producto_data = ProductoSchema(
        nombre = "Coca cola",
        descripcion = "Una bebida refrescante",
        precio = 19.55,
        categoria = "Bebidas"
    )    

    crear_producto(producto_data, db_session)

    producto_update = ProductoUpdate(
        descripcion = "Una bebida chida",
        precio = 23,
    ) 

    response = actualizar_producto(1, producto_update, db_session)

    assert response["message"] == "Producto actualizado correctamente"
    productos = obtener_productos(db_session)
    assert productos[0].descripcion == "Una bebida chida"

# No se puede actualizar un producto inexistente
def test_actualizar_producto_no_existente(db_session):
    producto_update = ProductoUpdate(
        descripcion = "Una bebida chida",
        precio = 23,
    ) 

    with pytest.raises(Exception, match="Producto no encontrado"):
        actualizar_producto(1, producto_update, db_session)

# Eliminar un proucto existente
def test_eliminar_producto(db_session):
    producto_data = ProductoSchema(
        nombre = "Coca cola",
        descripcion = "Una bebida refrescante",
        precio = 19.55,
        categoria = "Bebidas"
    )    

    crear_producto(producto_data, db_session)

    response = eliminar_producto(1, db_session)
    assert response["message"] == "Producto eliminado correctamente"
    
    productos = obtener_productos(db_session)
    assert productos is not None 

# No se puede eliminar un producto inexistente
def test_eliminar_producto_no_existente(db_session):
    with pytest.raises(Exception, match="Producto no encontrado"):
        eliminar_producto(1, db_session)