from flask import Flask, render_template, jsonify ,request, redirect, url_for


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
users = {}


@app.route("/")
def hello_stock_hub():
  return render_template('home.html',
                        stocks=stock_list,
                        company_name='Stock-Hub')


@app.route("/api/stocks")
def list_stocks():
  return jsonify(stock_list)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            # Successful login, redirect to home
            return redirect(url_for('home'))
        else:
            # Invalid credentials, show login page with error message
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        if username in users:
            return render_template('register.html', error='Username already taken')

        # Register the user (in-memory, in a real app, you would store this in a database)
        users[username] = password

        # Redirect to login page after successful registration
        return redirect(url_for('login'))

    return render_template('register.html')

if __name__ == '__main__': 
  app.run(host='0.0.0.0', debug=True)