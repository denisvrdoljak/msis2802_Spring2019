""" Streaming twitter API example """

# authors: Phil Mui, Michele Samorani, Yuhao Wang
import sys
import tweepy
import time
try:
    import configparser
except:
    from six.moves import configparser
class TwitterListener(tweepy.StreamListener):
    """ Twitter stream listener. """
    def on_status(self, tweet):
        f.write(str(tweet.text.encode('utf-8') + b"\n"))
        f.flush()
        print(tweet.text.encode('utf-8'))
        sys.stdout.flush()
	
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

    def on_timeout(self):
        print('timeout : wait for next poll')
        sleep(10)

def get_config():
    """ Get the configuration """
    conf = configparser.ConfigParser()
    conf.read('config.cfg')
    return conf

def get_stream():
    config = get_config()
    auth = tweepy.OAuthHandler(config.get('twitter', 'consumer_key'),
                               config.get('twitter', 'consumer_secret'))

    auth.set_access_token(config.get('twitter', 'access_token'),
                          config.get('twitter', 'access_token_secret'))

    listener = TwitterListener()
    stream = tweepy.Stream(auth=auth, listener=listener)
    return stream

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            print("Usage: %s <word>" % (sys.argv[0]))
        else:
            word = sys.argv[1]
            f = open(word + '.txt', 'w')
            stream = get_stream()
            print("Listening to " + word + " and #" + word)
            print("Tweets are written to your_key_word.txt")
            print("Press CTRL + c to terminate...")
            time.sleep(2)
            stream.filter(languages=["en"],track=[word, '#' + word])
    except KeyboardInterrupt:
        f.close()
        print('*****************************\nInterrupted')
        sys.exit()
