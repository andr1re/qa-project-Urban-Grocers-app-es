import configuration
import requests
import data

def post_new_user(body): # Envía una solicitud para crear un nuevo usuario
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json = body, # Inserta el cuerpo de la solicitud
                         headers = data.headers) # Inserta los encabezados de la solicitud
response = post_new_user(data.user_body) # Obtener la respuesta
print(response.status_code)
print(response.json())
# Obtener la respuesta y mostrar el cuerpo de respuesta en formato legible.

def get_new_token(): # Obtener el token del nuevo usuario
    user_body = data.user_body.copy()
    user_response = post_new_user(user_body)
    token = user_response.json()["authToken"]
    return token

def post_new_kit(model): # Envía una solicitud para crear un kit para este usuario
    headers = data.headers.copy()
    token = get_new_token()
    headers["Authorization"] = f"Bearer {token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json = model,
                         headers = headers)

