#Reddit Bot
import praw
import time
import random

r = praw.Reddit(user_agent = "Test Bot by /u/Pocket_Dealer_Bot")
print("Logging in...")
r.login() #placeholders

Deal = "What's the Deal"
Aces = ['pocket rockets', 'aces']
Kings = ['kings']
Queens = ['queens']
Jacks = ['jacks']
Tens = ['tens']
Nines = ['nines']
Eights = ['eights']
Sevens = ['sevens']
Sixes = ['sixes']
Fives = ['fives']
Fours = ['fours']
Threes = ['threes']
Twos = ['deuces', 'twos']
Deck = [Aces, Kings, Queens, Jacks, Tens, Nines, Eights, Sevens, Sixes, Fives, Fours, Threes, Twos]
comment_cache = []

def bot_func():
	print('Finding subreddit..')
	subreddit = r.get_subreddit("test")
	print('Grabbing comments...')
	comments = subreddit.get_comments(limit=20)
	for comment in comments:
		comment_text = comment.body.lower()
		isMatchDeal = any(string in comment_text for string in Deal)
		isMatchAces = any(string in comment_text for string in Aces)
		isMatchKings = any(string in comment_text for string in Kings)
		isMatchQueens = any(string in comment_text for string in Queens)
		isMatchJacks = any(string in comment_text for string in Jacks)
		isMatchTens = any(string in comment_text for string in Tens)
		isMatchNines = any(string in comment_text for string in Nines)
		isMatchEights = any(string in comment_text for string in Eights)
		isMatchSevens = any(string in comment_text for string in Sevens)
		isMatchSixes = any(string in comment_text for string in Sixes)
		isMatchFives = any(string in comment_text for string in Fives)
		isMatchFours = any(string in comment_text for string in Fours)
		isMatchThrees = any(string in comment_text for string in Threes)
		isMatchTwos = any(string in comment_text for string in Twos)
		if commend.id not in comment_cache and isMatchDeal:
			print('Match found! Comment ID: ' + comment.id)
			if commend.id not in comment_cache and isMatchAces:
				comment.reply("31 percent chance of victory. It's the statistical best")
			elif commend.id not in comment_cache and isMatchKings:
				comment.reply("26 percent chance of victory.")
			elif commend.id not in comment_cache and isMatchQueens:
				comment.reply("22 percent chance of victory.")
			elif commend.id not in comment_cache and isMatchJacks:
				comment.reply("19 percent chance of victory.")
			elif commend.id not in comment_cache and isMatchTens:
				comment.reply("17 percent chance of victory.")
			elif commend.id not in comment_cache and isMatchNines:
				comment.reply("15 percent chance of victory.")
			elif commend.id not in comment_cache and isMatchEights:
				comment.reply("14 percent chance of victory.")
			elif commend.id not in comment_cache and isMatchSevens:
				comment.reply("13 percent chance of victory.")
			elif commend.id not in comment_cache and isMatchSixes:
				comment.reply("13 percent chance of victory.")
			elif commend.id not in comment_cache and isMatchThrees or isMatchFours or isMatchFives:
				comment.reply("12 percent chance of victory.")
			else:
				Dealt = random.choice(Deck)
				comment.reply(Dealt)
			print('Reply successful!')
			cache.append(comment.id)
	print('Comments loop finished, time to sleep')
while True:
	run_bot()
	time.sleep(10)

