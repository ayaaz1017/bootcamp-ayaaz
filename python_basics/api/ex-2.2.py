from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

# Create HTTPBasic security instance
security = HTTPBasic()

# Dummy credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# Authentication dependency
def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != VALID_USERNAME or credentials.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Secure route
@app.get("/secure-data")
def secure_endpoint(username: str = Depends(authenticate)):
    return {"message": f"Hello, {username}. You have accessed a secure endpoint!"}

