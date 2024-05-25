import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6592054852:AAErlPlwr3UKXAzsaSvyCGGbdaPON9WNqug")

    APP_ID = int(os.environ.get("APP_ID", 26702912))

    API_HASH = os.environ.get("API_HASH", "f168695fe27367f16298b0c6293e7ddc")
