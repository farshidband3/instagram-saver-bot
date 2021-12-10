
import os


class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	API_ID = int(os.environ.get("API_ID", 12345))
	API_HASH = os.environ.get("API_HASH")
	OWNER_ID = int(os.environ.get("OWNER_ID", 1445283714))
	CAPTION = "By @AHToolsBot"
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "insta_Bot")
	
