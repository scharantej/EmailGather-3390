## Flask Application Design

### HTML Files

- **index.html**: This is the main HTML file that will serve as the frontend for the single-page application. It should include the necessary HTML elements to create the user interface and allow for user interactions (e.g., email input, submit button).
```html
<!DOCTYPE html>
<html>
<head>
  <title>Email Sign Up</title>
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="container">
    <h1>Email Sign Up</h1>
    <form id="signup-form">
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" class="form-control" name="email" required>
      </div>
      <button type="submit" class="btn btn-primary">Sign Up</button>
    </form>
  </div>
</body>
</html>
```

### Routes

- **@app.route('/')**: This route is bound to the root URL (/) and serves the `index.html` file, which is the frontend of the application.
```python
@app.route('/')
def index():
  return render_template('index.html')
```

- **@app.route('/signup', methods=['POST'])**: This route is bound to the '/signup' URL and handles POST requests for email sign-up. It retrieves the email from the request, saves it in the database, and returns a success message.
```python
@app.route('/signup', methods=['POST'])
def signup():
  email = request.form['email']
  # Code to save the email in the database
  return 'Sign up successful!'
```