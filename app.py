from flask import Flask, render_template, jsonify

app = Flask(__name__)

stock_list = [
    {
      "id": 1, 
      "name": "Apple", 
      "quantity": 50, 
      "price": 1.5
    },
    {
      "id": 2, 
      "name": "Banana", 
      "quantity": 30, 
      "price": 0.75
    },
    {
      "id": 3,
      "name": "Orange",
      "quantity": 40, 
      "price": 1.0
    },
    {
      "id": 4,
      "name": "Grapes",
      "quantity": 20,
      "price": 2.0
    },
    {
      "id": 5, "name":
      "Watermelon",
      "quantity": 15,
      "price": 3.0
    },
    {
      "id": 6,
      "name": "Pineapple",
      "quantity": 25,
      "price": 2.5
    },
    {
      "id": 7, "name":
      "Strawberry",
      "quantity": 35,
      "price": 2.0
    },
    {
      "id": 8, "name"
      : "Blueberry",
      "quantity": 40,
      "price": 1.75
    },
    {
      "id": 9,
      "name": "Mango",
      "quantity": 22,
      "price": 2.25
    },
    {
      "id": 10,
      "name": "Peach",
      "quantity": 18,
      "price": 2.75
    },
]


@app.route("/")
def hello_stock_hub():
  return render_template('home.html',
                        stocks=stock_list,
                        company_name='Stock-Hub')


@app.route("/api/stocks")
def list_stocks():
  return jsonify(stock_list)
  
if __name__ == '__main__': 
  app.run(host='0.0.0.0', debug=True)