from flask_env import MetaFlaskEnv
import os

project_name = "to_do_app"


class BaseSettings(metaclass=MetaFlaskEnv):       # anladim sozun duzu

    
    DEBUG = True
    # CSRF_ENABLED = True

    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_ECHO = True

    LOGGER_NAME = "%s_log" % project_name
    LOG_FILENAME = "app.%s.log" % project_name
