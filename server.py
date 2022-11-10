from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)

@app.route('/')
def index():
    users_info = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('index.html', users = users_info)



if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)