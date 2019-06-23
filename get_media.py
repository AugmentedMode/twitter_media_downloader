import tweepy
from tweepy import OAuthHandler
import urllib.request

CONSUMER_KEY = 'MWoTCuJdBzCWCp8kkhaQT9tLU'
CONSUMER_SECRET = 'XKzHo8XLiW4Ca5qQW53fOhOcQeHZGLbzlzjy3pyA27J6frYUmJ'
ACCESS_KEY = '1074454140363907072-KnjmAieJvCtccwAD1uKhpzzNeRRYd1'
ACCESS_SECRET = 'hx49vrho5SSmvAYN3PiWAjbdK4ntxO8YZz5qxTBL59qwg'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

try:
    tweet_url = str(input('Input URL: '))
    tweet_id = tweet_url.rsplit('/', 1)[-1]

    tweet = api.get_status(tweet_id)

    try:
        media_file = tweet.extended_entities['media'][0]['video_info']['variants'][0]['url']
        urllib.request.urlretrieve(media_file, 'downloaded_gif.mp4')
    except Exception as e:
        print('Sorry, could not download this GIF')

except Exception as e:
    print('Sorry, please input a valid URL')
