from flask import request, jsonify

from utils.check_db import check_db
from utils.generate_query import generate_query
from utils.execute_query import execute_query

def query(decoded_data):
    user_query = request.args.get('prompt')

    db_structure = check_db(decoded_data['data']["db_config"])  # Obtenemos la estructura para pasarla a GPT
    if not db_structure:
        return jsonify({"result": "Error analyzing the database"}), 500

    # Generar la consulta SQL y almacenar el prompt
    sql_query, prompt = generate_query(decoded_data['data']["openai_api_key"], db_structure, user_query, '')

    print("sql_query: ", sql_query)

    if sql_query:
        # Ejecutar la consulta y devolver el resultado
        result = execute_query( config= decoded_data['data']["db_config"], query= sql_query,api_key=decoded_data['data']["openai_api_key"],  db_structure=db_structure , user_query=user_query )
        print("result: ", result)

        return jsonify({
            "prompt": prompt,
            "sql_query": sql_query,
            "result": result
        })
    else:
        return jsonify({"result": "Error generating SQL query"}), 500
