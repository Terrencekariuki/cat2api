from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory product storage
products = []

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({'error': 'Invalid input'}), 400
    products.append(data)
    return jsonify({'message': 'Product created', 'product': data}), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
