import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="MyProfile", auth_level=func.AuthLevel.ANONYMOUS)
def MyProfile(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('MyProfile HTTP trigger received a request.')

    method = req.method
    if method == 'GET':
        # Serve the new, beautiful HTML portfolio page
        try:
            with open('static/index.html', 'r', encoding='utf-8') as f:
                html = f.read()
            return func.HttpResponse(
                html,
                mimetype="text/html",
                status_code=200
            )
        except Exception as e:
            return func.HttpResponse(
                f"<h1>Error loading portfolio page</h1><p>{str(e)}</p>",
                mimetype="text/html",
                status_code=500
            )
    else:
        return func.HttpResponse(
            json.dumps({"error": "Method not allowed."}),
            mimetype="application/json",
            status_code=405
        )