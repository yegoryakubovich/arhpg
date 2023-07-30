# Generated by Django 4.2.3 on 2023-07-27 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryText',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Текст - Категория',
                'verbose_name_plural': 'Текст - Категории',
                'db_table': 'categories_texts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('priority', models.IntegerField(verbose_name='Приоритет')),
                ('type', models.CharField(choices=[('text', 'Текст'), ('link', 'Ссылка')], max_length=8, verbose_name='Тип')),
                ('question', models.CharField(max_length=2048, verbose_name='Вопрос')),
                ('answer_button', models.CharField(max_length=2048, verbose_name='Кнопка ответа')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
                'db_table': 'faqs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FaqAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=8, verbose_name='Тип')),
                ('value', models.CharField(max_length=2048, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'FAQ - Вложение',
                'verbose_name_plural': 'FAQ - Вложения',
                'db_table': 'faqs_attachments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, max_length=4096, verbose_name='Текст')),
                ('datetime', models.DateTimeField(blank=True, null=True, verbose_name='Время')),
                ('state', models.CharField(choices=[('waiting', 'waiting'), ('completed', 'completed'), ('deleted', 'deleted')], default='waiting', max_length=16, null=True, verbose_name='Состояние')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
                'db_table': 'notifications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=16)),
                ('datetime', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Уведомление - отчёт',
                'verbose_name_plural': 'Уведомление - отчёты',
                'db_table': 'notifications_reports',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Уведомление - Пользователь',
                'verbose_name_plural': 'Уведомление - Пользователи',
                'db_table': 'notifications_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=256, verbose_name='Ключ')),
                ('value', models.CharField(max_length=256, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
                'db_table': 'settings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=256, verbose_name='Ключ')),
                ('value', models.CharField(max_length=8192, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Тексты',
                'db_table': 'texts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_id', models.BigIntegerField(verbose_name='ID билета')),
                ('state', models.CharField(max_length=16, verbose_name='Состояние')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
                'db_table': 'tickets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('arhpg_id', models.BigIntegerField(verbose_name='Arhpg ID')),
                ('arhpg_token', models.CharField(max_length=1024, verbose_name='Arhpg Token')),
                ('tg_user_id', models.BigIntegerField(verbose_name='ID Telegram')),
                ('firstname', models.CharField(blank=True, max_length=128, null=True, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, max_length=128, null=True, verbose_name='Фамилия')),
                ('email', models.CharField(blank=True, max_length=256, null=True, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
                'db_table': 'tags',
            },
        ),
    ]
