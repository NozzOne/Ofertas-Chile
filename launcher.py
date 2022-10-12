import webbrowser
from src import app, getProducts
from src.settings.Config import Config


if __name__ == "__main__":
    print("Abriendo navegador...")
    webbrowser.open("http://localhost:5000/")
    print("Iniciando servidor...")
    app.run(port=5000)
    print("Servidor iniciado!")