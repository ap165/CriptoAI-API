import json
from datetime import datetime, timezone, timedelta
from fastapi import APIRouter, Request
from pydantic import BaseModel
from utils import generate_otp, send_email, _json_response, users_col, otp_col
from templates import LOGIN_OTP

router=APIRouter()

class userCreate(BaseModel):
    username: str
    email: str

@router.post("/send-login-otp")
async def send_login_otp(user: userCreate):
    
    try:
        username = user.username
        to_email = user.email

        otp_data = generate_otp()
        existing_user = users_col.find_one({
            "$or": [
                {"email": to_email},
                {"userId": username}
            ]
        })

        if not existing_user:
            return _json_response(400, {"message": "No user found with this email or username."})
        else:
            otp_col.update_one(
                {"email": existing_user["email"]}, 
                {"$set": {
                    "otp_hash": otp_data["hash"],
                    "expires_at": datetime.now(timezone.utc) + timedelta(minutes=10)
                }},
                upsert=True
            )
            send_email("no-reply", existing_user["email"], "Your Login OTP Code", LOGIN_OTP.replace("{{OTP_CODE}}", str(otp_data["otp"])).replace("{{USER_NAME}}", existing_user["userId"]))
            
            return _json_response(200, {"message": "Login OTP sent successfully."})     
    except Exception as e:
        return _json_response(500, {"message": "An error occurred while sending login OTP", "error": str(e)})