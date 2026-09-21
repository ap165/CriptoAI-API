from datetime import datetime, timezone
from fastapi import APIRouter,  Request
from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel
from utils import generate_jwt, send_email, _json_response, users_col, otp_col
from templates import LOGIN

router = APIRouter()

class UserCreate(BaseModel):
    email: str
    username: str
    password: str
    otp: str

@router.post("/login")
async def login(request: Request, user: UserCreate):
    try:
        
        IP_ADDRESS = request.client.host if request.client else "Unknown IP"
        LOGIN_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        email = user.email
        password = user.password
        
        if not email:
            username = user.password
            user = users_col.find_one({"userId": username})
        else:
            user = users_col.find_one({"email": email})
        
        if not user:
            return _json_response(401, {"message": "Invalid Credentials."})
        password_valid = pbkdf2_sha256.verify(password, user.get("passwordHash")) if password else False
        
        if not password:
            otp = user.otp
            otpHash = otp_col.find_one({"email": user.get("email")}, {"otp_hash": 1}) if user.get("email") else None
            otpMatch = otpHash and pbkdf2_sha256.verify(str(otp), otpHash["otp_hash"])
            if not user or not otpMatch:
                return _json_response(401, {"message": "Invalid credentials"})
            otp_col.delete_one({"email": user["email"]})
        
        elif not user or not password_valid:
            return _json_response(401, {"message": "Invalid credentials"})
        
        
        jwt_token = generate_jwt(str(user["_id"]))
        send_email(
            "no-reply",
            user["email"],
            "New Login Detected",
            LOGIN.replace("{{USER_NAME}}", user["userId"]).replace("{{IP_ADDRESS}}", IP_ADDRESS).replace("{{LOGIN_TIME}}", LOGIN_TIME)
        )
        
        return _json_response(200, {
            "username": user["userId"],
            "email": user["email"],
            "name": user["name"],
            "token": jwt_token
        })
    
    except Exception as e:
        return _json_response(500, {"message": "An error occurred during login", "error": str(e)})