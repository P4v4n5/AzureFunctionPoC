import azure.functions as func
import logging
import os

app = func.FunctionApp()

@app.route(route="MyProfile", auth_level=func.AuthLevel.ANONYMOUS)
def MyProfile(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('MyProfile HTTP trigger received a request.')

    try:
        with open('static/index.html', 'r', encoding='utf-8') as f:
            html = f.read()
        return func.HttpResponse(html, mimetype="text/html")
    except Exception as e:
        return func.HttpResponse(f"<h1>Error loading page</h1><p>{e}</p>", status_code=500)

# 🛠️ Add this route for serving static files (css, js, images)
@app.route(route="static/{filename}", auth_level=func.AuthLevel.ANONYMOUS)
def StaticFiles(req: func.HttpRequest, filename: str) -> func.HttpResponse:
    try:
        path = os.path.join("static", filename)
        ext = os.path.splitext(filename)[1]
        
        # Basic content-type guessing
        if ext == ".css":
            mime = "text/css"
        elif ext == ".js":
            mime = "application/javascript"
        elif ext in [".png", ".jpg", ".jpeg"]:
            mime = "image/jpeg"
        elif ext == ".svg":
            mime = "image/svg+xml"
        else:
            mime = "application/octet-stream"

        with open(path, "rb") as f:
            return func.HttpResponse(f.read(), mimetype=mime)
    except Exception as e:
        return func.HttpResponse(f"File not found: {e}", status_code=404)
