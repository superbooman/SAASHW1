from flask import Flask, jsonify, request
app = Flask(__name__)

#information: cart content, product name, quantity, total price]
cart = []

#Endpoint #1: Get information
@app.route('/cart', methods = ['GET'])
def get_cart():
    return jsonify(cart)

#Endpoint #2: Post quantity of product to cart (using id)
@app.route('/cart/<int:user_id>/add/<int:product_id>', methods = ['POST'])
def add_cart(user_id,product_id):
    

    data = request.json
    quantity = data.get('quantity')
    quantityid = {"quantity":quantity, 
                  "product_id":product_id}
    if not quantity:
        return jsonify({"error": "Quantity not found"}), 404
    
    response = request.post('http://127.0.0.1:5000/product_list/remove_quantity', json = quantityid)
    
    current_cart_id = len(cart)+1

    new_cartproduct = {
        "id": current_cart_id,
        "name": response.json.get('name'),
        "price": response.json.get('price'),
        "quantity": quantity
    }
    cart.append(new_cartproduct)

    cart_item = next((cart_item for cart_item in cart if cart_item["id"] == current_cart_id), None)
    if cart_item:
        return jsonify({"cart_item": cart_item}), 200
    else:
        return jsonify({"error": "Cart Item unable to be added"}), 404
    
#Endpoint #3: Remove quantity from user cart
@app.route('/cart/<int:user_id>/remove/<int:product_id>', methods = ['POST'])
def add_cart(user_id,product_id):
    

    data = request.json
    quantity = data.get('quantity')
    quantityid = {"quantity":quantity, 
                  "product_id":product_id}
    if not quantity:
        return jsonify({"error": "Quantity not found"}), 404
    
    response = request.post('http://127.0.0.1:5000/product_list/add_quantity', json = quantityid)
    
    current_cart_id = len(cart)+1

    new_cartproduct = {
        "id": current_cart_id,
        "name": response.json.get('name'),
        "price": response.json.get('price'),
        "quantity": quantity
    }
    cart.pop(new_cartproduct)

    cart_item = next((cart_item for cart_item in cart if cart_item["id"] == current_cart_id), None)
    if cart_item:
        return jsonify({"cart_item": cart_item}), 200
    else:
        return jsonify({"error": "Cart Item unable to be removed"}), 404

if __name__ == '__main__':
    app.run(debug=True)
