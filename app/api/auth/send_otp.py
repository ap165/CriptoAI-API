import json
from fastapi import APIRouter, Request
from datetime import datetime, timezone, timedelta
from pydantic import BaseModel
from utils import generate_otp, send_email, _json_response, users_col, otp_col, validate_email
from templates import REG_OTP

router = APIRouter()

class User(BaseModel):
    username: str
    email: str

@router.post("/send-otp")
async def send_otp(user: User):
    try:
        username = user.username
        to_email = user.email

        if not username and not to_email:
            _json_response(400, {"message": "Email and username is required."})
        
        if to_email:
            if not validate_email(to_email):
                return _json_response(400, {"message": "Invalid email address."})

        otp_data = generate_otp()
        existing_user = users_col.find_one({
            "$or": [
                {"email": to_email},
                {"userId": username}
            ]
        })
        
        if existing_user:
            return _json_response(400, {"message": "User with this email or username already exists."})

        else:
            otp_col.update_one(
                {"email": to_email },
                {"$set": {
                    "otp_hash": otp_data["hash"],
                    "expires_at": datetime.now(timezone.utc) + timedelta(minutes=10)
                }},
                upsert=True
            )
            send_email("no-reply", to_email, "OTP Verification Code", REG_OTP.replace("{{OTP_CODE}}", str(otp_data["otp"])).replace("{{USER_NAME}}", username))
            return _json_response(200, {"message": "OTP sent successfully."})
        
    except Exception as e:
        return _json_response(500, {"message": "An error occurred while sending OTP", "error": str(e)})