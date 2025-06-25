from flask import Flask, request, render_template_string
import ssl

app = Flask(__name__)

# Simple HTML login form
LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head><title>Login Page</title></head>
<body>
    <h2>Login</h2>
    <form method="POST" action="/login">
        Username: <input type="text" name="username"><br><br>
        Password: <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(LOGIN_HTML)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    return f"Received: Username={username}, Password={password}"

if __name__ == '__main__':
    # Run Flask with SSL using self-signed certificate
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')
    app.run(host='0.0.0.0', port=443, ssl_context=context)
