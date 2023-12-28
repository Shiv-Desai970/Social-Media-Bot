from instabot import Bot
import tweepy
import requests


#Instagram
def instagramFunc():
    instaUsername = input('Enter your username:')
    instaPassword = input('Enter your password:')
    photoPath = input("Enter the path for image:")
    postCaption = input('Enter caption for your post:')

    instagramBot = Bot() 
    instagramBot.login(username = instaUsername, password = instaPassword)
    instagramBot.upload_photo(photoPath,caption=postCaption)
    instagramBot.logout()
    print('Post successfully posted on Instagram!')


#Twitter
def twitterFunc():
    bearerKey = input('Enter your bearer_key:')
    consumerKey = input('Enter your consumer_key:')
    consumerSecret = input('Enter your Consumer_secret_key:')
    accessToken = input('Enter your access_token:')
    accessSecret = input('Enter your access_Secret_token:')

    keys = {
    "BEARER_TOKEN" : bearerKey,
    "API_KEY": consumerKey,
    "API_KEY_SECRET": consumerSecret,
    "ACCESS_TOKEN": accessToken,
    "ACCESS_TOKEN_SECRET": accessSecret,
}
    
    tweet = input("Enter your tweet:")
    client = tweepy.Client(keys["BEARER_TOKEN"], keys["API_KEY"], keys["API_KEY_SECRET"], keys["ACCESS_TOKEN"], keys["ACCESS_TOKEN_SECRET"])
    client.create_tweet(text=tweet)
    print('Post successfully posted on Twitter!')


#FaceBook
def facebookFunc():
    access_token = input('Enter your accessToken:')
    message = input('Enter your message:')
    pageId = input('Enter page id:')
    
    api_url = f'https://graph.facebook.com/v12.0/{pageId}/feed'
    params = {
        'access_token': access_token,
        'message': message
    }

    response = requests.post(api_url, params=params)

    print('Post successfully posted on Facebook!')

def main():

    print('Welcome to my social media bot')
    userInput = int(input('Enter a number between 1 to 4\n  1: instagram post \n 2: twitterpost \n 3: facebook \n 4: all social media apps\n')) 

    if userInput == 4: 
        instagramFunc() 
        twitterFunc() 
        facebookFunc()

    elif userInput == 1:
        instagramFunc()

    elif userInput == 2: 
        twitterFunc()

    elif userInput == 3: 
        facebookFunc()

if __name__ == '__main__':
    main()


