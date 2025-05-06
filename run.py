from app import create_app

# Crear la aplicación Flask
app = create_app()

if __name__ == '__main__':
    # esto hara que el backend sea accesible desde cualquier IP
    app.run(host='0.0.0.0', port=5000, debug=True)
