import sys
import time
import twitter

# Michelle's Twitter Credentials:
# Username: ribandm
# Password: sendmeonmyway

api = twitter.Api(
  consumer_key='NWvclDdT8J4XGEGb4X4mv4f7z',
  consumer_secret='B44Orf7O9pbfGQxCmedKswVeqWXfj6odWD5QyuF4xHsvjrcpQa',
  access_token_key='726454687281598467-z2xi3QTl47b86vKmX9hCmJiPRJ1VrON',
  access_token_secret='WWagXKISlQQkNuhr6ARaBGp7owaaTHuqhKBE7dIubrHRJ'
)

# Asks user for input: 
search_term = input("Please enter a search term: ")
number_of_desired_tweets = 500

# Provides specifications for get request (language, recent, total # of tweets): 
search = api.GetSearch(term=search_term, 
					   lang='en', 
					   result_type='recent', 
					   count=number_of_desired_tweets, 
					   max_id=''
					  )

# Output file name + time of get request: 
file_name = 'output-term:' + search_term + '-time:' + str(time.time()) + '.txt'

# All the results will save to an output file, not the terminal so we can analyze it: 
f = open(file_name, 'w')

# Numbers tweet starting with 1 to help user identify tweets: 
tweet_count = 1

# Search is a list of all the tweets
# Need to iterate through every tweet 
for t in search:
	# .write --> saving to output file 
	# Identifies Tweet # (up to 100)
	f.write('Tweet # ' + str(tweet_count) + ':' + '\n')
	tweet_count += 1
	# Username + time that Tweet was created: 
	f.write(t.user.screen_name + ' (' + t.created_at + ')')
	# Content of Tweet: 
	f.write(t.text)
	# New line: 
	f.write('\n')

print("Finished searching the Twitter API. Wrote the results to a file called " + file_name)