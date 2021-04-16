from tweepy import OAuthHandler
import tweepy

ckey = ""
csecret = ""
atoken = ""
asecret = ""
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth, wait_on_rate_limit=True)


ids = open('Data/ids.txt', 'r').read().splitlines()

data = {}
for id_ in tqdm(ids):
    try:
        x = api.get_status(id_, tweet_mode="extended")._json
    except tweepy.TweepError as e:
        print('Missing:', id_, e.args[0][0]['code'])
    data[id_] = x
