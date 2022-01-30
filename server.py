from flask import Flask, flash, redirect, render_template

# creating instance of Flask Class, using __name__ for name of app module or 
# package
# Flask now knows where to look for resources such as templates and static files
app = Flask(__name__)
app.secret_key = "user123"

# route() decorator tells Flask what URL should trigger function
@app.route('/')
def first_poc():
    """Home page."""
    # returns msg desired to be displayed in user's browser
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

