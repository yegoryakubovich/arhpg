from datetime import datetime, timezone

import requests
from loguru import logger

from app.aiogram import bot_get
from app.db.manager import db_manager
from app.db.models.notification_report import NotificationReport
from app.db.models.notification_user import NotificationUser
from app.db.models.user import User
from app.repositories.notification import Notification
from aiogram.utils.exceptions import BotBlocked

bot = bot_get()


@db_manager
async def notificator():
    logger.info("notificator")
    utc_now = datetime.now(timezone.utc)
    notifications = Notification.list_waiting_get(utc_now)
    for notification in notifications:
        await send_notification(notification)


@db_manager
async def send_notification(notification):
    users = [user for user in User.select().join(NotificationUser).where(NotificationUser.notification == notification)]
    utc_now = datetime.now(timezone.utc)

    for user in users:
        report = NotificationReport(
            notification=notification,
            user=user,
            state='waiting',
            datetime=utc_now,
        )
        try:
            await bot.send_message(user.tg_user_id, notification.text)
            notification.state = 'completed'
            report.state = 'completed'
        except requests.exceptions.RequestException as _:
            notification.state = 'error'
            report.state = 'error'
        except BotBlocked as _:
            notification.state = 'error'
            report.state = 'error'
        finally:
            notification.save()
            report.save()

