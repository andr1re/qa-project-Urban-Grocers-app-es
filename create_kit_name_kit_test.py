# Tests a partir de la ista de comprobación de pruebas
import requests
import configuration
import data
import sender_stand_request
from data import one_letter, no_letter, letter_max_limit, letter_limit_exceeded, special_character, string_with_numbers, \
    number_parameter, with_spaces, valid_kit_name
from sender_stand_request import response_new_kit


# El único campo que requiere cambios en todas las comprobaciones es "name"
# Se modifica el cuerpo de solicitud ya existente en data.py con el uso de la función get_kit_body(kit_name)

def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy() # Se copia el diccionario que contiene el cuerpo de
    # la solicitud para conservar datos de origen
    current_kit_body["name"] = kit_name # Se cambia el valor del parámetro "name"
    return current_kit_body # Se devuelve un nuevo diccionario con el valor "name" requerido

# Función de prueba positiva
def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name) # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_response = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                json = kit_body,
                headers = data.headers)
    return kit_response
    # Comprobar el código de estado de la respuesta y campo name
def test_create_kit_with_valid_name():
    response_create_kit = positive_assert(valid_kit_name)
    assert response_create_kit.status_code == 201
    assert response_create_kit.json()["name"] == valid_kit_name

# 1. El número permitido de caracteres en el nombre del kit es 1
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(one_letter)
    assert response_new_kit.status_code == 201 # Comprobar el código de estado de la respuesta

# 2. El número permitido de caracteres (511) en name
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(letter_max_limit)
    assert response_new_kit.status_code == 201 # Comprobar el código de estado de la respuesta

# 3. El campo name es un string vacío
def negative_assert_empty_string(model):
    response_empty_string = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                json = model,
                headers = data.headers)
    return response_empty_string

def test_create_kit_empty_string_get_error_response():
    kit_body = get_kit_body(no_letter)
    response_empty_string = negative_assert_empty_string(kit_body)
    assert response_empty_string.status_code == 400 #Comprobar el código de estado de la respuesta

# 4. El número de caracteres es mayor que la cantidad permitida (512) en name
def negative_assert(model):
    response_limit_exceeded = requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                json = model,
                headers = data.headers)
    return response_limit_exceeded

def test_create_kit_512_letter_in_name_get_error_response():
    kit_body = get_kit_body(letter_limit_exceeded)
    response_limit_exceeded = negative_assert(kit_body)
    assert response_limit_exceeded.status_code == 400 # Comprobar el código de estado de la respuesta

# 5. Se permiten caracteres especiales en name
def test_create_kit_symbol_in_name_get_success_response():
    positive_assert(special_character)
    assert response_new_kit.status_code == 201 # Comprobar el código de estado de la respuesta

# 6. Se permiten espacios en name
def test_create_kit_space_in_name_get_success_response():
    positive_assert(with_spaces)
    assert response_new_kit.status_code == 201 # Comprobar el código de estado de la respuesta

# 7. Se permiten números en name
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(string_with_numbers)
    assert response_new_kit.status_code == 201 # Comprobar el código de estado de la respuesta

# 8. Falta el parámetro name no se pasa en la solicitud
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy() # Se copia el diccionario con el cuerpo de la solicitud de data a kit_body
    kit_body.pop("name") # El parámetro name se elimina de la solicitud
    negative_assert(kit_body) # Comprueba la respuesta
    assert response_new_kit.status_code == 400 # Comprobar el código de estado de la respuesta

# 9. Se ha pasado un tipo de parámetro diferente en name (número)
def test_create_kit_number_get_error_response():
    kit_body = get_kit_body(number_parameter) # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    response_number_parameter = sender_stand_request.post_new_kit(kit_body) # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    assert response_number_parameter.status_code == 400 # Comprobar el código de estado de la respuesta











