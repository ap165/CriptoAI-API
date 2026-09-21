from fastapi import APIRouter

from .login import router as login_router
from .register import router as register_router
from .reset_password import router as reset_password_router
from .send_login_otp import router as send_login_otp_router
from .send_otp import router as send_otp_router
from .send_reset_otp import router as send_reset_otp_router
from .verify_jwt import router as verify_jwt_router


router = APIRouter()

router.include_router(login_router)
router.include_router(register_router)
router.include_router(reset_password_router)
router.include_router(send_login_otp_router)
router.include_router(send_otp_router)
router.include_router(send_reset_otp_router)
router.include_router(verify_jwt_router)