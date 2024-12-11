from flask import Flask
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from endpoints.check_connections import check_connections
from endpoints.query import query
from endpoints.analyze_db import analyze_db
from endpoints.create_chart import create_chart



from decorators.private_route import private_route

app = Flask(__name__)
CORS(app, support_credentials=True  )


load_dotenv()

@app.route('/check-connections', methods=['POST'])
@cross_origin(origin='*')
def check_connections_endpoint():
    return check_connections()


@app.route('/analyze-db')
@cross_origin(origin='*')
@private_route
def analyze_db_endpoint(decoded_data):
    return analyze_db(decoded_data)

@app.route('/query')
@cross_origin(origin='*')
@private_route
def query_endpoint(decoded_data):
    return query(decoded_data)


@app.route('/create-chart', methods=['POST'])
@cross_origin(origin='*')
@private_route
def create_chart_endpoint(decoded_data):
    return create_chart(decoded_data)


# if __name__ == '__main__':
#     app.run()