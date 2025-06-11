import azure.functions as func
import logging
import os
import mimetypes

app = func.FunctionApp()

# Serve the main HTML portfolio page
@app.route(route="MyProfile", auth_level=func.AuthLevel.ANONYMOUS)
def MyProfile(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('MyProfile HTTP trigger received a request.')

    try:
        html_path = os.path.join(os.path.dirname(__file__), "myprofile.html")
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        return func.HttpResponse(html_content, mimetype="text/html", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"<h1>Error:</h1><pre>{str(e)}</pre>", status_code=500)


# Serve static files (like MyImg.jpg) from /static folder
@app.route(route="static/{filename}", auth_level=func.AuthLevel.ANONYMOUS)
def static_files(req: func.HttpRequest) -> func.HttpResponse:
    try:
        filename = req.route_params.get("filename")  # correct way in Python v4
        static_path = os.path.join(os.path.dirname(__file__), "static", filename)

        if not os.path.exists(static_path):
            return func.HttpResponse("File not found", status_code=404)

        mime_type = mimetypes.guess_type(static_path)[0] or "application/octet-stream"
        with open(static_path, "rb") as f:
            content = f.read()

        return func.HttpResponse(content, mimetype=mime_type)

    except Exception as e:
        return func.HttpResponse(f"<h1>Error serving static file</h1><pre>{str(e)}</pre>", status_code=500)
