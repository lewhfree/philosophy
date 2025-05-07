import wikipediaapi as wikipedia

userAgentString = "PhilosophyChecker/0.0.1 (github.com/lewhfree/philosophy)"

wiki = wikipedia.Wikipedia(user_agent=userAgentString, language='en')

