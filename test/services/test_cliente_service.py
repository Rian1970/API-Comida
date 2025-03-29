import pytest
from src.services.cliente_service import (
    obtener_clientes,
    obtener_cliente_por_id,
    crear_cliente,
    actualizar_cliente,
    eliminar_cliente
)
from src.models.cliente import Cliente
from src.schemas.cliente import ClienteSchema, ClienteUpdate

# Obtener todos los clientes (debe retornar una lista vacía al inicio)
def test_obtener_clientes_vacio(db_session):
    clientes = obtener_clientes(db_session)
    assert clientes == []  # No hay clientes en la BD aún

# Crear un cliente correctamente
def test_crear_cliente(db_session):
    cliente_data = ClienteSchema(
        nombre="Juan Pérez",
        telefono="1234567890",
        correo="juan@example.com",
        contrasenia="secreta09"
    )
    response = crear_cliente(cliente_data, db_session)
    
    assert response["message"] == "Cliente creado correctamente"
    assert db_session.query(Cliente).count() == 1

# Obtener cliente por ID
def test_obtener_cliente_por_id(db_session):
    cliente_data = ClienteSchema(
        nombre="Juan Pérez",
        telefono="1234567890",
        correo="juanillo@example.com",
        contrasenia="secreta09"
    )
    crear_cliente(cliente_data, db_session)

    cliente = obtener_cliente_por_id(1, db_session)  # ID 1 porque es el primero
    assert cliente is not None
    assert cliente.nombre == "Juan Pérez"

# No se debe permitir duplicar correos
def test_crear_cliente_correo_duplicado(db_session):
    cliente_data = ClienteSchema(
        nombre="Juan Pérez",
        telefono="1234567890",
        correo="junitobanano@example.com",
        contrasenia="secreta09"
    )

    # Creamos el primer cliente
    crear_cliente(cliente_data, db_session)

    # Intentamos crear otro con el mismo correo
    with pytest.raises(Exception, match="El correo ya esta registrado"):
        crear_cliente(cliente_data, db_session)

# Obtener cliente con ID inexistente
def test_obtener_cliente_no_existente(db_session):
    cliente = obtener_cliente_por_id(99, db_session)  # Un ID que no existe
    assert cliente is None

# Actualizar un cliente existente
def test_actualizar_cliente(db_session):
    cliente_data = ClienteSchema(
        nombre="Juan Pérez",
        telefono="1234567890",
        correo="juanete@example.com",
        contrasenia="secreta09"
    )
    crear_cliente(cliente_data, db_session)

    cliente_update = ClienteUpdate(nombre="Juan Modificado", telefono="0987654321")
    response = actualizar_cliente(1, cliente_update, db_session)

    assert response["message"] == "Cliente actualizado correctamente"
    cliente = obtener_cliente_por_id(1, db_session)
    assert cliente.nombre == "Juan Modificado"

# No se puede actualizar un cliente inexistente
def test_actualizar_cliente_no_existente(db_session):
    cliente_update = ClienteUpdate(nombre="Nuevo Nombre")
    
    with pytest.raises(Exception, match="El cliente no existe"):
        actualizar_cliente(99, cliente_update, db_session)

# Eliminar un cliente existente
def test_eliminar_cliente(db_session):
    cliente_data = ClienteSchema(
        nombre="Juan Pérez",
        telefono="1234567890",
        correo="juaper@example.com",
        contrasenia="secreta09"
    )
    crear_cliente(cliente_data, db_session)

    response = eliminar_cliente(1, db_session)
    assert response["message"] == "Cliente eliminado correctamente"

    cliente = obtener_cliente_por_id(1, db_session)
    assert cliente is None

# No se puede eliminar un cliente inexistente
def test_eliminar_cliente_no_existente(db_session):
    with pytest.raises(Exception, match="El cliente no existe"):
        eliminar_cliente(99, db_session)
