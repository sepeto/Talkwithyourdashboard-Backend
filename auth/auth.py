from flask import Flask, request, jsonify
from functools import wraps
import jwt
import os


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        SECRET_KEY_JWT = os.getenv('SECRET_KEY_JWT')
        
        token = request.headers.get('token')  # Obtener el token del encabezado
        
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401
        
        try:
            # Decodificar el token
            decoded_data = jwt.decode(token, SECRET_KEY_JWT, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 401
        
        # Almacenar los datos decodificados en kwargs para usarlos en la función
        return f(decoded_data, *args, **kwargs)
    
    return decorated