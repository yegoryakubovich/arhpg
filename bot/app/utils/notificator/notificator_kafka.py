import json

from confluent_kafka import Consumer

from app.aiogram import bot_get
from app.db.manager import db_manager
from app.repositories import User, Text
from app.utils.api_client import api_client
from settings import settings


@db_manager
async def notificator_kafka():
    bot = bot_get()
    kafka_config = {
        'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
        'security.protocol': settings.KAFKA_SECURITY_PROTOCOL,
        'sasl.mechanism': settings.KAFKA_SASL_MECHANISM,
        'sasl.username': settings.KAFKA_SASL_PLAIN_USERNAME,
        'sasl.password': settings.KAFKA_SASL_PLAIN_PASSWORD,
        'group.id': 'user_consumer_group',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(kafka_config)

    topic = 'timetable'

    consumer.subscribe([topic])

    while True:
        msg = consumer.poll(10)

        if msg is None:
            continue
        else:
            value = msg.value()
            if value is not None:
                value = value.decode('utf-8')
                data = json.loads(value)
                message_type = data.get('type')
                if message_type == 'event':
                    message_action = data.get('action')
                    if message_action == 'update':
                        message = ""
                        event_id = data.get('id', {}).get('event', {}).get('uuid')
                        user_data = await api_client.xle.get_events_user(event_id)
                        unti_ids = {user.get('unti_id') for user in user_data}
                        arhpg_ids = await User.get_all_arhpg_id()

                        tg_user_ids = list(unti_ids.intersection(arhpg_ids))

                        event_title = data.get('data', {}).get('title', '')
                        new_time = data.get('data', {}).get('started_at', '')
                        new_data = data.get('data', {}).get('ended_at', '')

                        if new_time and new_data:
                            message = Text.get('update_data_datatime').format(event_title=event_title) \
                                    + Text.get('new_datatime_program').format(new_data=new_data, new_time=new_time)  \
                                    + Text.get('current_program')
                        elif new_data:
                            message = Text.get('update_data').format(event_title=event_title) \
                                    + Text.get('new_data_program').format(new_data=event_title) \
                                    + Text.get('current_program')
                        elif new_time:
                            message = Text.get('update_time').format(event_title=event_title) \
                                    + Text.get('new_time_program').format(new_time=event_title) \
                                    + Text.get('current_program')
                        if message_action == 'delete':
                            message = Text.get('cancellation_program').format(event_title=event_title) \
                                      + Text.get('current_program')

                        if tg_user_ids:
                            for tg_user_id in tg_user_ids:
                                bot.send_message(chat_id=tg_user_id, text=message)

                consumer.close()
