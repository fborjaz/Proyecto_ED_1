from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo!, este es el inicio de mi aplicacion web para estructura de datos!'

if __name__ == '__main__':
    app.run()
