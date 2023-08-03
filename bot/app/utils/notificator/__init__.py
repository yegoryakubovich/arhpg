from asyncio import new_event_loop, set_event_loop

from time import sleep
from threading import Thread
import aioschedule as schedule

from app.utils.notificator.notificarot_user import notificator_user
from app.utils.notificator.notificator import notificator
from app.utils.notificator.notificator_kafka import notificator_kafka
from app.utils.notificator.notificator_tag import notificator_tag
from app.utils.notificator.notificator_usedesk import notificator_usedesk


def notificator_thread():
    loop = new_event_loop()
    set_event_loop(loop)

    schedule.every(2).minutes.do(notificator)
    schedule.every(15).minutes.do(notificator_kafka)
    schedule.every(5).seconds.do(notificator_usedesk)
    schedule.every(6).seconds.do(notificator_user)
    schedule.every(5).seconds.do(notificator_tag)
    while True:
        loop.run_until_complete(schedule.run_pending())
        sleep(3)


def notificator_create():
    thread = Thread(target=notificator_thread, args=())
    thread.start()
