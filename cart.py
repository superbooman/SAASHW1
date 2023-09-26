from flask import Flask, jsonify, request
app = Flask(__name__)

#information: cart content, product name, quantity, total price]
cart = []

#Endpoint #1: Get information
@app.route('/cart', methods = ['GET'])
def get_cart():
    return jsonify(cart)

#Endpoint #2: Post quantity of product to cart (using id)
@app.route('/cart', methods = ['POST'])
def add_cart():
    new_item = request.json.get('id')
    product = next((product for product in product if product["id"] == product), None)
    if product:
        cart.append(product)
        return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not found"}), 404
    
#Endpoint #3: Post removal of quantity from cart (using id)
@app.route('/cart', methods = ['POST'])
def add_cart():
    new_item = request.json.get('id')
    product = next((product for product in product if product["id"] == product), None)
    if product:
        cart.pop(product)
        return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)