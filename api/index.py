from app import app  # FastAPI app defined in app.py

def handler(request):
    from mangum import Mangum
    asgi_handler = Mangum(app)
    return asgi_handler(request)
