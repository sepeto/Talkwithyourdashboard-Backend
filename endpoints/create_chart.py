from flask import request, jsonify
from utils.generate_chart import generate_chart


def create_chart(decoded_data):

    print(decoded_data["data"]["openai_api_key"])
    openai_api_key=decoded_data['data']["openai_api_key"]
    prompt = request.args.get('prompt')
    graph_type = request.args.get('graphType')
    data = request.get_json()


    required_fields = ['json']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    print("inicializar creador de chart")

    print(data["json"])

    build_chart = generate_chart(openai_api_key, data["json"], prompt, graph_type )

    if ( build_chart ):
        return jsonify({"chart": build_chart}), 200

    else:
        return jsonify({"result": "Error generating SQL query"}), 500