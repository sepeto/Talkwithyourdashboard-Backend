from flask import request, jsonify
from utils.check_db import check_db
from utils.generate_description import generate_description

def analyze_db(decoded_data):
    decoded_data
    prompt = request.args.get('prompt')
    print({prompt})
    db_structure = check_db(decoded_data['data']["db_config"])

    if db_structure:
        gpt_description = generate_description(decoded_data['data']["openai_api_key"], db_structure, prompt)
        
        response = {
            "db_structure": db_structure,
            "gpt_description": gpt_description,
        }

        return jsonify(response) , 200
    else:
        print("Error analyzing the database")
        return jsonify({"error": "Error analyzing the database"}), 500