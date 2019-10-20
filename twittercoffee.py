#  Twitter bot that talks randomly about coffee.
#  v0.2

import random
import tweepy

#  Wordlists to generate random-ish sentences

curse = ['Damn! ', 'Mmmh! ', 'MMMMMMMMMMH! ', 'About time! ', 'Finally! ']
adverbs = ['Nearly ', 'Almost ', 'Firmly ', 'Truthfully ', 'Quickly ', 'Wickedly ', 'Brutally ', 'Cheerfully ']
verbs = ['drinking', 'sipping', 'consuming', 'grinding']
coffee = [' #blackgold, ', ' #coffee again, ', ' #techfuel, ', ' #ACupOfJoe, ', ' #C8H10N4O2, ', ' #covfefe, ', ' #mormoncrack, ', ' #mud, ', ' #coffay, ']
verbs2 = ['awaiting', 'looking forward to', 'anticipating', 'preparing for']
nouns = [' the morning.', ' the afternoon.', ' the evening.', ' the apocalypse.', ' the storm.', ' the Rapture.', ' the end of Days.']

tweet_curse = random.choice(curse)
tweet_verbs = random.choice(verbs)
tweet_adverbs = random.choice(adverbs)
tweet_nouns = random.choice(nouns)
tweet_verbs2 = random.choice(verbs2)
tweet_coffee = random.choice(coffee)

tweet_sentence = tweet_curse + tweet_adverbs + tweet_verbs + tweet_coffee + tweet_verbs2 + tweet_nouns  # Combining them all to form an actual sentence 

print(tweet_sentence)


#  Credentials - https://tweepy.readthedocs.io/en/v3.5.0/getting_started.html


def main():  # Template created by https://twitter.com/mattccrampton
    twitter_auth_keys = {

        "consumer_key": "xxx",
        "consumer_secret": "zzz",
        "access_token": "yyy",
        "access_token_secret": "ccc"
    }

    auth = tweepy.OAuthHandler(
        twitter_auth_keys['consumer_key'],
        twitter_auth_keys['consumer_secret']
    )

    auth.set_access_token(
        twitter_auth_keys['access_token'],
        twitter_auth_keys['access_token_secret']
    )


    api = tweepy.API(auth)
    tweet = tweet_sentence  # Tweets the randomly generated sentence
    status = api.update_status(status=tweet)


if __name__ == "__main__":
    main()
