# 1-2-3-Direct-Messages-With-Tweepy
Reading, replying and deleting Twitter Direct Messages with Tweepy

This is the sample code of the [Twitter Direct Messages like a Pro (with Tweepy)](https://beppecatanese.medium.com/twitter-direct-messages-like-a-pro-with-tweepy-48bc1cdade04) 
article.

## Setup

Clone the repository

```
git clone https://github.com/gcatanese/1-2-3-Direct-Messages-With-Tweepy.git
```

Create and *.env* file in the same folder as *app.py*. The *.env* file defines the environment variables.  
Configure the values using the Twitter tokens from the the Twitter Developer account:
* TWITTER_API_KEY=x
* TWITTER_API_SECRET_KEY=y
* TWITTER_ACCESS_TOKEN=z
* TWITTER_ACCESS_TOKEN_SECRET=s

## Run 
Run the application
```
python app.py
```
The application will start a Thread reading the DMs every 60 seconds.
Each new incoming message is replied and deleted. 