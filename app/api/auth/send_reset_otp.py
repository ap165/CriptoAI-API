from utils import generate_otp, send_email, _json_response, users_col, otp_col
from datetime import datetime, timezone, timedelta
from fastapi import APIRouter
from pydantic import BaseModel
from templates import PASS_RESET_OTP

router = APIRouter()

class User(BaseModel):
    username: str
    email: str


@router.post("/send-reset-otp")
async def send_reset_otp(user: User):
    
    try:
        email = user.username
        username = user.email

        user = users_col.find_one({
            "$or" : [
                {"email": email},
                {"userId": username}
            ]
        })

        if not user:
            if email:
                return _json_response(400, {"message": "No user found with this email."})
            else:
                return _json_response(400, {"message": "No user found with this username."})
        
        otp_data = generate_otp()
        otp_col.update_one(
                {"email": user["email"]}, 
                {"$set": {
                    "otp_hash": otp_data["hash"],
                    "expires_at": datetime.now(timezone.utc) + timedelta(minutes=10)
                }},
                upsert=True
            )
        
        send_email("no-reply", user["email"], "OTP for password reset", PASS_RESET_OTP.replace("{{USER_NAME}}", user["userId"]).replace("{{OTP_CODE}}", str(otp_data["otp"])))

        return _json_response(200, {"message": "OTP sent successfully."})
    
    except Exception as e:
        return _json_response(500, {"message": "An error occurred while sending OTP", "error": str(e)})
