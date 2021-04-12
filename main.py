from create_api import create_api
from randomarticle import randomarticle
import logging

logging.basicConfig(
    filename='twitter-bot.log', encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger()


def post_tweet(event="", context=""):
    api = create_api()
    article = randomarticle()
    tweet = article.write_tweet()
    try:
        api.update_status(status=tweet)
    except Exception as e:
        logger.error("Error posting tweet", exc_info=True)
        raise e
    logger.info("Tweet successfully posted")


post_tweet()
