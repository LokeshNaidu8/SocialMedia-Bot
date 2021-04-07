import tweepy
import time
consumerkey='3HPrnxzGG9soNCUGSzgNoUZ92'
consumersecretkey='DXYEWhAt8u0FGLN1HqKAnk3jYhqYzr51ZhSwLB70lzwEgHh4GC'

auth=tweepy.OAuthHandler(consumerkey,consumersecretkey)
auth.set_access_token('828288426222841862-vF845nsX1a3HSgiw8TuoZ5uioSge7XH',
                      'dg3wCFETHjYsFrWBSwvk427dXwEsNeWgdyLZqJgPsnmWO')

api=tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

user=api.me()
print(user)
print(user.name)
# for follower in tweepy.Cursor(api.followers).items():
#     print(follower.name)

search=['cat','dogs','animals','animal']
numberoftweets=500
for tweet in tweepy.Cursor(api.search,search).items(numberoftweets):
    try:
        print("tweet liked")
        tweet.favorite()
        time.sleep(2)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break