import json
from flask import Flask, jsonify, request  # Import necessary modules from Flask and json

# Create an instance of the Flask class
app = Flask(__name__)

# List of items with "Name" and "Price"
items = [
    {
        "Name": "Green Apple",
        "Price": 160
    },
    {
        "Name": "Momos",
        "Price": 80
    }
]

# Define a route for the root URL ("/") with GET method
@app.route("/", methods=["GET"])
def main():
    # Return the list of items as JSON when the root URL is accessed
    return {"Items": items}

# Define a route for dynamic URL to get an item by name
@app.route("/get-item/<string:name>", methods=["GET"])
def main_dyn(name):
    # Loop through items to find the one with the given name
    for item in items:
        if name == item['Name']:  # If item found, return it as JSON
            return jsonify(item)
    # If no matching item found, return a 404 response with an error message
    return jsonify({'Message': 'Record does not exist.'}), 404

# Define a route that accepts name as a parameter in the URL to get an item
@app.route("/get-itemss", methods=["GET"])
def main_param():
    # Retrieve the 'Name' parameter from the URL
    name = request.args.get('Name')
    # Loop through items to find the one with the given name
    for item in items:
        if name == item['Name']:
            return jsonify(item)  # Return the item if found
    # If no item found, return a 404 response
    return jsonify({'Message': 'Record does not exist.'}), 404

# Define a route to add a new item (using POST method)
@app.post("/add-Items")
def add_new():
    # Parse the JSON data from the request body
    request_data = request.get_json()
    # Add the new item to the items list
    items.append(request_data)
    # Return a success message with a 201 status code (Created)
    return {"message": "Item Added successfully."}, 201

# Define a route to update an existing item (using PUT method)
@app.put("/Update-Items")
def Upd_new():
    try:
        # Parse the JSON data from the request body
        request_data = request.get_json()

        # Ensure that 'Name' and 'Price' fields are present in the request
        if 'Name' not in request_data or 'Price' not in request_data:
            return {'message': "Invalid request. 'Name' and 'Price' are required fields."}, 400

        # Find the item by name and update its price
        for item in items:
            if item['Name'] == request_data['Name']:
                item['Price'] = request_data['Price']
                return {"message": "Item updated successfully."}, 200

        # If the item doesn't exist, return a 404 response
        return {'message': "Given Record doesn't exist."}, 404

    except Exception as e:
        # If an error occurs, print the error and return a 500 (Internal Server Error)
        print(f"Error occurred: {e}")
        return {'message': "An internal error occurred."}, 500

# Define a route to delete an item (using DELETE method)
@app.delete("/Delete-Items")
def del_item():
    # Retrieve the 'Name' parameter from the URL
    name = request.args.get('Name')
    # Loop through items to find the one with the given name
    for item in items:
        if name == item['Name']:
            # Remove the item from the list if found
            items.remove(item)
            return {'message': 'Item Deleted Successfully'}
    # If no matching item found, return a 404 response
    return jsonify({'Message': 'Record does not exist.'}), 404

# Main block to run the Flask app
if __name__ == "__main__":
    # Run the Flask app on localhost (0.0.0.0) at port 8000 with debug mode enabled
    app.run(debug=True, host="0.0.0.0", port=8000)

# To check the status code, we can use the `requests` library to send a GET request
import requests

# Sending a GET request to the root URL using localhost
response_root = requests.get("http://127.0.0.1:8000/")
# Print the status code for the root URL
print(f"Root URL Status Code: {response_root.status_code}")

# Sending a GET request to the /main URL using localhost
response_main = requests.get("http://127.0.0.1:8000/main")
# Print the status code for the /main URL
print(f"/main URL Status Code: {response_main.status_code}")
