# api/index.py

from app import app  # This imports your FastAPI app from app.py
from mangum import Mangum

# This wraps the FastAPI app to make it compatible with Vercel's Lambda
handler = Mangum(app)
