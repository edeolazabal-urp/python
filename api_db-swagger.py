from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
from flasgger import Swagger, swag_from
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
swagger = Swagger(app)

# Configuración de la base de datos
DB_HOST = "localhost"
DB_NAME = "20241"
DB_USER = "postgres"
DB_PASSWORD = "admin"
DB_PORT = "5432"

# Conexión a la base de datos
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    return conn

@app.route('/')
def index():
    return "Welcome to the Flask PostgreSQL API!"

@app.route('/data', methods=['GET'])
@swag_from('docs/get_data.yml')
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM auto;')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@app.route('/data', methods=['POST'])
@swag_from('docs/add_data.yml')
def add_data():
    data = request.json
    brand = data['brand']
    price = data['price']
    tax = data['tax']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO auto (brand, price, tax) VALUES (%s, %s, %s)', (brand, price, tax))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Data added successfully'}), 201

@app.route('/data/<int:id>', methods=['PUT'])
@swag_from('docs/update_data.yml')
def update_data(id):
    data = request.json
    brand = data['brand']
    price = data['price']
    tax = data['tax']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE auto SET brand = %s, price = %s, tax=%s WHERE id = %s', (brand, price, tax, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Data updated successfully'})

@app.route('/data/<int:id>', methods=['DELETE'])
@swag_from('docs/delete_data.yml')
def delete_data(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM auto WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Data deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
