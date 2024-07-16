
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/signup', methods=['POST'])
def signup():
  email = request.form['email']
  # Sample code to implement email saving to a database
  print(f"The email {email} was saved.")
  return 'Sign up successful!'

if __name__ == '__main__':
  app.run(debug=True)
