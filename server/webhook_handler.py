import config
from collections import defaultdict
from requests_futures.sessions import Session
from flags.lookup import lookup
import logging

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class WebhookHandler(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.session = Session()

    def SendLogin(self, user, users=0):
        try:
            if config.webhook_user_logged_in:
                info = defaultdict(dict)
                info["title"] = "A user has logged in!"
                info["description"] = u"Player {0} representing {1} has joined the {2} others.".format(user.handle, user.country, users)
                info["provider"]["name"] = "RT Community Server"
                info["provider"]["url"] = "https://risingthunder.community"
                self.session.post(config.webhook_user_logged_in,json={"embeds":[info]})
        except:
            logging.debug("Couldn't post webhook.")