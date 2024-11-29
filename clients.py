import requests
import json

BASE_URL = 'http://127.0.0.1:5000/products'

# Add new products
def add_product(name, description, price):
    product = {'name': name, 'description': description, 'price': price}
    response = requests.post(BASE_URL, json=product)
    print(f"Add Product Response: {response.status_code}, {response.json()}")

# Retrieve all products
def get_products():
    response = requests.get(BASE_URL)
    print(f"Get Products Response: {response.status_code}")
    print(json.dumps(response.json(), indent=4))

if __name__ == '__main__':
    # Example usage
    add_product('Laptop', 'High-performance laptop', 1500.00)
    add_product('Phone', 'Smartphone with 5G', 800.00)
    get_products()
