import azure.functions as func
import logging
import os

app = func.FunctionApp()

@app.route(route="static/{filename}", auth_level=func.AuthLevel.ANONYMOUS)
def MyProfile(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('MyProfile HTTP trigger received a request.')

    try:
        html_path = os.path.join(os.path.dirname(__file__), "myprofile.html")
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        return func.HttpResponse(html_content, mimetype="text/html", status_code=200)

    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
