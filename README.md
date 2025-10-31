# magabot
![magabot-pic](https://github.com/jesswhyte/magabot/blob/master/magabot.jpg)
#MAGAbot is a python script running on a Raspberry Pi computer (well, any computer you want, but I built her using a RPi). She monitors a live streaming API from Twitter (~ .5-1% of all public tweets) for tweets combining the “Make America Great Again” hashtag (#MAGA) and terms that disparage women (e.g. bitch, cunt, slut, whore). When she finds one, she reads it aloud and displays it on a LED character display. 

She is intended to catch you off guard. As the minutes pass, you forget she is there. And then, there it is. If it’s a busy day, this feeling may shift to annoyance, anger, sadness, acceptance….

Video of MAGAbot in action: [https://youtu.be/c3mxNi-5_WQ](https://youtu.be/PD2uyMwMKfE)

To run MAGAbot, you will need:
flite,
twitter package for python, 
API keys/tokens from dev.twitter.com.

Note: this version of the script does not include LCD character display output as it is intended to run on any computer with python installed. Please contact me for a RPi version with LCD output. 
