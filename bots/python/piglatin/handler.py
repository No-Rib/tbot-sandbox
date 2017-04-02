"""Provides Handler class"""

import telepot


class Handler(object):
    """Piglatin Tbot hadler class."""

    def __init__(self, token):

        self.token = token
        self.bot = None
        self.loop = None

    @staticmethod
    def piglatinize(word):
        return word[1:] + word[0] + "ay"

    def handler(self, msg):
        """Tbot message handler."""

        self.bot.sendMessage(msg["chat"]["id"], self.piglatinize(msg["text"]))

    def run(self):
        """Initializes Tbot loop."""

        self.bot = telepot.Bot(self.token)
        self.loop = self.bot.message_loop(self.handler, run_forever="Running")
