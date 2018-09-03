## Getting Started

You must have a basic knowledge in python, twitter and all of the things in life, like change a tire.

### Prerequisites
First of all to make this pyt work you have to request a twitter developer account, is easy, but sometimes it takes time.

To actually make this work the following libraries are need

```
sudo pip install tweepy
sudo pip install tkinter
sudo pip install urllib
```

### Installing

It's a freaking python script for Odin's sake... if dont know how to run it take some steps back and try to go outside to see the sunlight

### How It (supposedly) Works

This PYT filters all tweets containing a specified text (i.e. a hashtag) and filters wich ones retweet based in a list of predefinied users ID's.

The o ther feature is tweet some content based on a predefinied list.

Simple and Clean (not that clean though....)

## Deployment

Create a separated credentials.py file in the root containing the following variables:

```
consumer_key = 'your consumer key'
consumer_secret = 'consumer secret'
access_token = 'access token'
access_token_secret = 'the secret access token'
```
All the tokens above are found in the App description in Twitter's developers page

To fill the list of users that will be retweeted just grab their ID's (you can use [TwitterByID](https://gettwitterid.com) ) and put each user in a different line of the 'collabUsers.txt' (yes I know, its kinda trash but i cant see a good reason to change it...)

```
078561498
09879846
948498454
```

After that to put some tweets in the account simply open "teste.txt" and write your tweet in the file ending the text with a ";" separator, if you want a flesh image in the tweet put the image in the "img" folder and the image name after the ";" separator

```
Hey I just met you and this is crazy, so get out of my garden or you wont leave here in One Piece; smile.gif
```

If you dont want a image in your tweet put an extra ";" after the tweet text

```
You are young, life has been kind to you;;
```

As I said it before, its way too simple...


## Versioning

It's version 1.0 , but it miraculously works as intended, future changes will be added in the future, but for now I'm really happy and don't feel like it.

## Authors

* **Wesley Takai** - *Initial work* - [TsutomuTakai](https://github.com/TsuomuTakai)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Many thanks to Tweepy team to make such a wonderful python library, it saved me a lot of time
