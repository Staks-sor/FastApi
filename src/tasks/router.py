from fastapi import APIRouter, BackgroundTasks, Depends

from auth.base_config import current_user

from .tasks import send_email_report_dashboard

router = APIRouter(prefix="/report")


@router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):

    send_email_report_dashboard.delay(user.username)

    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }