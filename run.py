import os 
from flask import Flask
# Importing Flask class

app = Flask(__name__)
# Creating an instance of this and storing it in a variable called 'app'

@app.route("/")
def index():
    return "Hello, World"


# In Python, a decorator starts with the @ symbol (pie-notation)
# Decorator is a way of wrapping functions

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

# **IMPORTANT** debug=True call allow arbitrary code to be run and can be security flaw
# debug=True while testing application in development mode but change it to debug=False before submit project