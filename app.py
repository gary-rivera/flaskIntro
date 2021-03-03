from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """welcome"""

    return """
        <html>
            <head>
                <title>Welcome</title>
            </head> 
            <body>
                <h1>welcome</h1>
            </body>
        </html
    """


@app.route('/home')
def home():
    """ home page """

    return """
        <html>
            <head>
                <title>Welcome Home</title>
            </head> 
            <body>
                <h1>welcome home</h1>
            </body>
        </html
    """


@app.route('/back')
def back():
    """ welcome back """

    return """
        <html>   
            <head>
                <title>Welcome Back</title>
            </head> 
            <body>
                <h1>welcome back</h1>
            </body>
        </html
    """
