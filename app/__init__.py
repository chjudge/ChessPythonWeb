from flask import Flask

app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
        SECRET_KEY="jMTCHNVkCPY1gDmamOpV",
        SEND_FILE_MAX_AGE_DEFAULT=0,
        USE_SESSION_FOR_NEXT=True,
    )


from app import routes
