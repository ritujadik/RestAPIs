from fastapi import FastAPI,Body,HTTPException
import re
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
stored_email = "xyz@gmail.com"
stored_mobile = "9999999999"
stored_password = "Abc@123"


def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_valid_password(password: str) -> bool:
    return (
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[@#$%^&*!]', password)
    )

def is_valid_mobile(number: str) -> bool:
    return len(number) == 10 and number.isdigit()

# Mock stored credentials

class LoginRequest(BaseModel):
    email: str
    mobile: str
    password: str
@app.post("/login")
def login(request: LoginRequest):
    if (
            (request.email == stored_email and request.password == stored_password) or
            (request.mobile == stored_mobile and request.password == stored_password)
    ):
        print("email:",request.email)
        print("mobile:",request.mobile)
        print("password:",request.password)
        return {"message": "You have logged in successfully"}

    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.post("/signup")
def signup(email: str = Body(...), mobile: str = Body(...), password: str = Body(...)):
    if not is_valid_email(email):
        return {"error": "Invalid email format"}
    if not is_valid_mobile(mobile):
        return {"error": "Please enter a valid 10-digit mobile number"}
    if not is_valid_password(password):
        return {"error": "Password must be at least 8 characters long and include uppercase, lowercase, digit, and special character."}
    return {"message": "You have signed up successfully"}

@app.post("/update_mobile")
def update_mobile(current_mobile: str = Body(...), new_mobile: str = Body(...)):
    if current_mobile != stored_mobile:
        return {"error": "Your current mobile number is incorrect"}
    if not is_valid_mobile(new_mobile):
        return {"error": "New mobile number is invalid"}
    return {"message": "Your new mobile number has been updated", "new_mobile": new_mobile}

@app.post("/update_email")
def update_email(current_email: str = Body(...), new_email: str = Body(...)):
    if current_email != stored_email:
        return {"error": "Your current email is incorrect"}
    if not is_valid_email(new_email):
        return {"error": "New email format is invalid"}
    return {"message": "Your email has been updated", "new_email": new_email}

@app.post("/update_password")
def update_password(current_password: str = Body(...), new_password: str = Body(...)):
    if current_password != stored_password:
        return {"error": "Your current password is incorrect"}
    if not is_valid_password(new_password):
        return {"error": "New password format is invalid"}
    return {"message": "Your password has been updated successfully"}

