import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="AnimalFunction", auth_level=func.AuthLevel.ANONYMOUS)
def AnimalFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('AnimalFunction HTTP trigger received a request.')

    # In-memory animal list (for PoC only)
    if not hasattr(AnimalFunction, 'animals'):
        AnimalFunction.animals = []

    method = req.method
    if method == 'GET':
        # List all animals
        return func.HttpResponse(
            json.dumps({"animals": AnimalFunction.animals}),
            mimetype="application/json",
            status_code=200
        )
    elif method == 'POST':
        try:
            data = req.get_json()
            animal = data.get('animal')
            if animal:
                AnimalFunction.animals.append(animal)
                return func.HttpResponse(
                    json.dumps({"message": f"Added animal: {animal}", "animals": AnimalFunction.animals}),
                    mimetype="application/json",
                    status_code=201
                )
            else:
                return func.HttpResponse(
                    json.dumps({"error": "Missing 'animal' in request body."}),
                    mimetype="application/json",
                    status_code=400
                )
        except Exception as e:
            return func.HttpResponse(
                json.dumps({"error": str(e)}),
                mimetype="application/json",
                status_code=400
            )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Method not allowed."}),
            mimetype="application/json",
            status_code=405
        )