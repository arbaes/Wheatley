import wheatley
import configparser
import logging

# Logging Configuration
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Get config
config = configparser.ConfigParser()
config.read('config.ini')
token = config['Credentials']['token']

# Start the bot
client = wheatley.Wheatley()
client.run(token)
