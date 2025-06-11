import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="AnimalFunction", auth_level=func.AuthLevel.ANONYMOUS)
def AnimalFunction(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('AnimalFunction HTTP trigger received a request.')

    method = req.method
    if method == 'GET':
        # Serve a simple HTML portfolio page
        html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Pavan's Portfolio</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                img { max-width: 300px; border-radius: 10px; box-shadow: 0 2px 8px #aaa; }
            </style>
        </head>
        <body>
            <h1>Pavan</h1>
            <img src="https://randomuser.me/api/portraits/men/75.jpg" alt="Pavan's photo">
            <p>Welcome to my portfolio website!</p>
        </body>
        </html>
        '''
        return func.HttpResponse(
            html,
            mimetype="text/html",
            status_code=200
        )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Method not allowed."}),
            mimetype="application/json",
            status_code=405
        )