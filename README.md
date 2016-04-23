# SocialNPHS
Analyze the New Paltz High School through data from social media

## Project outline

- Use APIs from Twitter, Instagram, maybe Facebook.
- Begin with:
	- a list of social media accounts known to belong to NPHS
	- Other useful NPHS-related data like:
		- List of teacher names (first, last, gender)
		- List of upcoming events, etc.
- Include all the accounts that the initial accounts follow who are within ~5 miles of New Paltz
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

## Guidelines

Some tentative guidelines for development:

- Write mostly in Python
- Project structure
  - There should be a folder for each social network, keeping isolated structure between them. Each folder should contain:
    - A script leveraging that social network's API which **exposes a common interface**. Basically, this code should allow for data from different social networks to be accessed in the same way. It should expose methods for returning the text of posts by NPHS students, but not go so deep as to implement sentiment analysis, which can be implemented just once at a higher level.
    - JSON data about accounts belonging to NPHS students, formatted like
    ```json
	{
		"@1Defenestrator": {
			"grade":2019,
			"name":"Luke Taylor",
			"alias":null,
			"sex":"M"
		},
		"@G4_Y5_3X": {
			"grade":2017,
			"name":"Moshe Katzin-Nystrom",
			"alias":"(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Pråppe",
			"sex":"M"
		},
	}
    ```
  - There should be a higher-level interface that uses the data from the previously described submodules. It should read post text, and ignore social network. In other words, all sources are created equal. This should implement:
    - Sentiment analysis (is the post positive or negative?)
    - Other text processing
      - Identify the subject, if any, and compare against a database of teachers and other students
    - An exposed Python interface for accessing processed data
  - There should be a folder full of scripts that leverage the data from the higher-level interface. These should implement things like graphs and charts, which should be kept separate from the Python interface.
