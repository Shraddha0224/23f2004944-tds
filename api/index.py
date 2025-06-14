from app import app  # Your FastAPI app from app.py
from fastapi_vercel import vercel_handler

handler = vercel_handler(app)
