from flask import Flask, jsonify, request
app = Flask(__name__)

#information: name, price, quantity

product_list = [
    {"id": 1 , "name": "beans", "price": 3.59, "quantity": 5},
    {"id": 2 , "name": "rice", "price": 2.50, "quantity": 10},
    {"id": 3 , "name": "fish", "price": 6.23, "quantity": 2},
    {"id": 4 , "name": "cereal", "price": 5.50, "quantity": 22}
]

#Endpoint 1: get all product list
@app.route('/product_list', methods=['GET'])
def get_products():
    return jsonify({"product_list": product_list})

#Endpoint 2: get individual product
@app.route('/product_list/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in product_list if product["id"] == product_id), None)
    if product:
        return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not found"}), 404

#Endpoint 3: post add product information
@app.route('/product_list', methods=['POST'])
def create_product():
    new_product = {
        "id": len(product_list) + 1,
        "name": request.json.get('name'),
        "price": request.json.get('price'),
        "quantity": request.json.get('quantity')
    }
    product_list.append(new_product)
    return jsonify({"message": "Product created", "product": new_product}), 201

#Endpoint 4: modify quantity value down
@app.route('/product_list/remove_quantity', methods=['POST'])
def remove_quantity():
    data = request.json
    quantity_remove = data.get('quantity')
    id = data.get('product_id')

    product = next((p for p in product_list if p["id"] == id), None)
    if product:
        product['quantity'] = product['quantity'] - quantity_remove
        return jsonify({"message": "Product quantity modified successfully", "product": product})
    else:
        return jsonify({"error": "Product not found"}), 404

#Endpoint 5: modify quantity value up
@app.route('/product_list/add_quantity', methods=['POST'])
def add_quantity():
    data = request.json
    quantity_add = data.get('quantity')
    id = data.get('product_id')

    product = next((p for p in product_list if p["id"] == id), None)
    if product:
        product['quantity'] = product['quantity'] + quantity_add
        return jsonify({"message": "Product quantity modified successfully", "product": product})
    else:
        return jsonify({"error": "Product not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
