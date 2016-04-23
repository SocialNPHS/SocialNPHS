# SocialNPHS
Analyze the NPHS through data from social media

## Project outline

- Use APIs from Twitter, Instagram, maybe Facebook.
- Begin with:
	- a list of social media accounts known to belong to NPHS 
	- Other useful NPHS-related data like:
		- List of teacher names (first, last, gender)
		- List of upcoming events, etc.
- Include all the accounts that the initial accounts follow who are within 5 miles of New Paltz
	- Judge location by looking at their geolocated posts
	- These accounts are *likely* to belong to NPHS students
- Regularly analyze all tweets/posts from accounts likely to belong to NPHS students.
- Create graphs and stuff pertaining to NPHS related stuff
	- Sentiment analysis of posts about NPHS teachers
		- Frequency of mentioning individual teacher's names on social media
		- Analyze natural language to determine proportion of positive/negative posts about a teacher
	- Sentiment analysis of posts about students
		- For the list of student names, determine proportion of positive/negative posts that mention a student

## Libraries

- Use [nltk](http://www.nltk.org) for text processing
- Social libraries
  - [tweepy](http://www.tweepy.org)
  - [python-instagram](https://github.com/facebookarchive/python-instagram) maybe, haven't looked into it.
