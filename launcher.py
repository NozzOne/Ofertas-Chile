import webbrowser
from src import app, log


if __name__ == "__main__":
    print("Abriendo navegador...")
    webbrowser.open("http://localhost:5000/")
    print("Iniciando servidor...")
    app.run(port=5000)
    print("Servidor iniciado! :D, Url: http://localhost:5000/")
    print("Presiona Ctrl+C para cerrar el servidor.")
