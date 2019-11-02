__author__ = 'Akshit'

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
##import csv
import time

ckey = 'gIU11Ni6ccIevfwZ9hmGkZFcV'
csecret = '4iB89v6zK4yO9aZK6puy3DyGzc1U53Z4CtbrQhcxSRJSWelN0x'
atoken = '131040011-Sr2nIzfHRmZO7xh0k3mIKU3zkh2ddmpAkjdz8De1'
asecret = 'S8eMLIeKJ16Bz3WnXbuYbu6T0km9jFIoyIJO9LI6pIpqD'

class listener(StreamListener):

    def on_data(self, data):
        ##print(data)
        ##return(True)
        """try:
            tweet = data.split(',"text":"')[1].split('",source')[0]
            print (tweet)
            saveThis = (time.time())+'::' + tweet
            saveFile = open("E:\Final Year\Project - SATDS\twit.txt",'a')
            saveFile.write(saveThis)
            saveFile.write("\n")
            saveFile.close()
            return  (True)
        except BaseException as e:
            print ("failed on data:", str(e))
            time.sleep(5)
            """
        x=open('twitterout.txt','a')
        x.write(str(data))
        ##x.write('\n \n \n')

        
        
        x.close()

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Arvind Kejriwal"])

"""
class listner(StreamListener):

    def on_data(self,data):
        try:
            tweet = data.split(',"text":"')[1].split('",source')[0]
            print tweet
            saveThis = (time.time())+'::' + tweet
            saveFile = open("twitDB2.txt",'a')
            saveFile.write(saveThis)
            saveFile.write("\n")
            saveFile.close()
            return  True
        except BaseException,e:
            print "failed on data,", str(e)
            time.sleep(5)



    def on_error(self, status):
        print status"""




