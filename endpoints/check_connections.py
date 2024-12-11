from flask import request, jsonify
import jwt
import datetime
import os

from validators.check_openai_token import check_openai_token
from validators.check_mysql_connection import check_mysql_connection




def check_connections():
    SECRET_KEY_JWT = os.getenv('SECRET_KEY_JWT')
    # Obtén el cuerpo de la solicitud
    print(f"SECRET_KEY_JWT: ", SECRET_KEY_JWT)
    data = request.get_json()
    print(f"body: {data}")
    # Valida que los campos necesarios están presentes
    required_fields = ['user', 'password', 'host', 'database', 'port', 'openAiApiKey']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    token_data = {
        'db_config': {
            'user': data['user'],
            'password': data['password'],
            'host': data['host'],
            'database': data['database'],
            'port': data['port']
        },
        'openai_api_key': data['openAiApiKey']
    }
    
    print(f"data formateado: {token_data}")

    # Validar la conexión a MySQL
    if not check_mysql_connection(token_data['db_config']):
        return jsonify({"error": "Error al intentar conectar a la base de datos con las credenciales proveidas."}), 400

    # Validar la clave de OpenAI
    if not check_openai_token(token_data['openai_api_key']):
        return jsonify({"error": "API key de OpenAI inválido."}), 400

    # Genera el token JWT con los datos del cuerpo y una expiración de 1 hora
    token = jwt.encode({
        'data': token_data,  # Aquí guardamos el body completo
        'exp': datetime.datetime.utcnow() + datetime.timedelta(weeks=1)  # Expiración de 1 semana
    }, SECRET_KEY_JWT, algorithm='HS256')

    return jsonify({'token': token})