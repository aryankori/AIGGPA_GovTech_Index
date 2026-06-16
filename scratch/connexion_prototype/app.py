import connexion

# Create the Connexion App wrapper using the Flask backend
app = connexion.FlaskApp(__name__, specification_dir='./')

# Add the API specification (maps the endpoints defined in openapi.yaml to python functions)
app.add_api('openapi.yaml')

if __name__ == '__main__':
    print("--------------------------------------------------")
    print("Starting Connexion API Prototype server...")
    print("- Swagger UI Dashboard: http://localhost:8080/ui/")
    print("- Example Endpoint (Greet): http://localhost:8080/hello?name=Aryan")
    print("- Example Endpoint (Add): http://localhost:8080/add?a=10&b=25")
    print("--------------------------------------------------")
    app.run(port=8080)
