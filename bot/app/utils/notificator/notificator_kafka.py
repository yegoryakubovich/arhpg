import json

from confluent_kafka import Consumer
from loguru import logger

from app.aiogram import bot_get
from app.db.manager import db_manager
from app.repositories import User, Text
from app.utils.api_client import api_client
from settings import settings


@db_manager
async def notificator_kafka():
    logger.info("notificator_kafka")

    try:
        bot = bot_get()
        kafka_config = {
            'bootstrap.servers': settings.KAFKA_HOSTS,
            'security.protocol': settings.KAFKA_SP,
            'sasl.mechanism': settings.KAFKA_SASL_MECHANISM,
            'sasl.username': settings.KAFKA_SASL_USER,
            'sasl.password': settings.KAFKA_SASL_PASSWORD,
            'group.id': 'user_consumer_group',
            'auto.offset.reset': 'earliest'
        }

        consumer = Consumer(kafka_config)

        topic = 'timetable'

        consumer.subscribe([topic])

        msg = consumer.poll(10)

        if msg is not None:
            value = msg.value()
            if value is not None:
                value = value.decode('utf-8')
                data = json.loads(value)
                message_type = data.get('type')
                if message_type == 'timetable':
                    message_action = data.get('action')
                    if message_action == 'update':
                        message = ""
                        event_id = data.get('id', {}).get('timetable', {}).get('uuid')

                        user_data = await api_client.event.get_events_user(event_id)
                        unti_ids = {user.get('unti_id') for user in user_data}
                        arhpg_ids = await User.get_all_arhpg_id()

                        tg_user_ids = list(unti_ids.intersection(arhpg_ids))

                        event_title = data.get('data', {}).get('title', '')
                        new_datatime = data.get('data', {}).get('started_at', '')
                        delete = data.get('data', {}).get('is_deleted', 1)

                        if new_datatime:
                            message = Text.get('update_datatime_program').format(event_title=event_title) + '\n' \
                                      + Text.get('current_program')
                        if delete:
                            message = Text.get('cancellation_program').format(event_title=event_title) \
                                      + Text.get('current_program')

                        if tg_user_ids:
                            for tg_user_id in tg_user_ids:
                                await bot.send_message(chat_id=tg_user_id, text=message)

        consumer.close()

    except Exception as e:
        logger.error(f"notificator_kafka: {str(e)}")