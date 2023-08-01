from app.db.manager import db_manager
from app.repositories import User
from app.repositories.tag import Tag
from app.repositories.user_tag import UserTag
from app.utils.api_client import api_client


@db_manager
async def notificator_tag():
    existing_tags = await Tag.get()
    tags = await api_client.user.get_all_tags()
    existing_tags_dict = {tag.tag_id: tag for tag in existing_tags}

    for tag_data in tags['payload']:
        tag_id = tag_data['id']
        if tag_id not in existing_tags_dict:
            tag = await Tag.create(
                tag_id=tag_id,
                name=tag_data['slug'],
                title=tag_data['title']
            )
            tag.save()

            response = await api_client.user.get_users_by_tags(tag_id)
            if response['result']['successful']:
                users = response['payload']
                if users:
                    all_arhpg_id = await User.get_all_arhpg_id()
                    for user_data in users:
                        user_id = user_data['leader_id']
                        if user_id in all_arhpg_id:
                            tag_user = await UserTag.create(tag_id, user_id)
                            tag_user.save()
