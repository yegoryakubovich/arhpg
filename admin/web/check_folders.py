import os


def check_folders():
    if not os.path.exists('media'):
        os.mkdir('media')

    if not os.path.exists('media/bot'):
        os.mkdir('media/bot')

    if not os.path.exists('media/bot/files'):
        os.mkdir('media/bot/files')

    if not os.path.exists('media/bot/photos'):
        os.mkdir('media/bot/photos')

    if not os.path.exists('media/exports'):
        os.mkdir('media/exports')
