from datetime import datetime, timezone
from fastapi import APIRouter, Request
from utils import send_email, _json_response, users_col, otp_col, validate_password
from passlib.hash import pbkdf2_sha256
from templates import PASS_CHANGED
from pydantic import BaseModel

router = APIRouter()

class userCreate(BaseModel):
    username: str
    email: str
    otp: str
    newPass: str

@router.post("/reset-password")
async def reset_password(request: Request, user: userCreate):
    try:
        username = user.username
        email = user.email
        otp = user.otp
        new_password = user.newPass

        CHANGE_TIME = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        IP_ADDRESS = request.client.host if request.client else "Unknown IP"

        if not validate_password(new_password):
            return _json_response(400, {"message": "Password must be at least 8 characters."})
        
        if not otp:
            return _json_response(400, {"message": "OTP is required."})

        user = users_col.find_one({
            "$or": [
                {"email": str(email)},
                {"userId": str(username)}
            ]
        })

        if not user:
            return _json_response(400, {"message": "No user found."})

        otpHash = otp_col.find_one({"email": user["email"]}, {"otp_hash": 1})
        otp_valid = otpHash and pbkdf2_sha256.verify(str(otp), otpHash["otp_hash"])

        if otp_valid:
            otp_col.delete_one({"email": user["email"]})
            new_passwordHash = pbkdf2_sha256.hash(new_password)

            users_col.update_one(
                {"email": user["email"]},
                {"$set": {
                    "passwordHash": new_passwordHash,
                    "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                }},
            )
            send_email(
                "no-reply",
                user["email"],
                "Password Reset Detected",
                PASS_CHANGED.replace("{{USER_NAME}}", user["userId"]).replace("{{IP_ADDRESS}}", IP_ADDRESS).replace("{{CHANGE_TIME}}", CHANGE_TIME)
            )
            return _json_response(200, {"message": "Password reset successful."})

        else:
            return _json_response(400, {"message": "Invalid OTP"})

    except Exception as e:
        return _json_response(500, {"message": "An error occurred while resetting password", "error": str(e)})