from create_api import create_api
from randomarticle import randomarticle


def post_tweet(event="", context=""):
    api = create_api()
    article = randomarticle()
    tweet = article.write_tweet()
    try:
        api.update_status(status=tweet)
    except Exception as e:
        print("I'm stupid, sorry.. some error occured")
        raise e
    print("Tweet successfully posted")
