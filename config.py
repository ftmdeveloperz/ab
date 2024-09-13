import os


class Config(object):
    API_HASH = os.environ.get("API_HASH", "b3a786dce1f4e7d56674b7cadfde3c9d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7037453058:AAGDtxFckOjQryf7pwPVK7zdiMSW-vL6w6s")
    TELEGRAM_API = os.environ.get("TELEGRAM_API", "28776072")
    OWNER = os.environ.get("OWNER", "7042535787")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "ftmdeveloper")
    PASSWORD = os.environ.get("PASSWORD", "@ftmdeveloper")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ftm:ftm@cluster0.rhh9r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    LOGCHANNEL = os.environ.get("LOGCHANNEL", "-1002209201816")  # Add channel id as -100 + Actual ID
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQG3FogAkXFq48_fYpmJhUFE9y7TWFSeIZwbiFaMaNwVnm5M_4Unc_mu_FLOtG_bXeIB1FrGNtMzk06eUfTvu2vN2ykeUR3OJ3JdjN4jy7Vas8mRafAQxZf4cGnW3CZIdBJJnVgpJz-oM-C0GzQLQNjBQqhLWE5WCmYVzH-gQKmSwS7lYbLSykK5PceiPWeRtEEtvacZrs-ofBD9Rd3DWWVqy5GzEL-6cqD-eg8JeuWlBMVUgclhAwPebzVXzgac3TUz1LOwE3Wb3kO1i31Wrg-7ruKnAb2bebIju3qQEQzHPdh91wyb-Wp_nveNVdmE8GFnxF6wFh4RB_Qh0b_EngIFPEpNTQAAAAGjxJFrAA")
    IS_PREMIUM = True
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
