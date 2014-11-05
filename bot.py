import praw
import re
import settings

r = praw.Reddit(user_agent='r/starcraft new player bot')
r.login(settings.reddituser, settings.redditpass)
subreddit = r.get_subreddit('jo3m3tal')
comments = praw.helpers.comment_stream(r,subreddit)


for comment in comments:
  if re.match(r".*/u/automaton2000.*", comment.body, re.IGNORECASE) != None:
    comment.reply('are you new?')
