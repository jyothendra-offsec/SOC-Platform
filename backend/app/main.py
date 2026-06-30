from fastapi import FastAPI

app = FastAPI(
    title="SOC Platform",
    description="Enterprise Security Operations Platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the SOC Platform API"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
