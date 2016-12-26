from flask import Flask

app = Flask(__name__)
app.config.from_object('edo.default_settings')
app.config.from_envvar('EDO_SETTINGS', silent=True)

from . import views  # noqa
