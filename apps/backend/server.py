########
#
# FastAPI-based Content Management Server
# - using plain database & qdrant vector store
#
########
from fastapi import FastAPI, HTTPException
# from qdrant_client import QdrantClient
from fastapi.middleware.cors import CORSMiddleware
# from qdrant_client.http.models import Distance, VectorParams, PointStruct
from pydantic import BaseModel
from typing import List, Optional, Dict
from uuid import uuid4
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Chapterhouse Local API Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    """Initialise required modules on startup."""
    print("startup event.")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
    }

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8088, reload=True)

