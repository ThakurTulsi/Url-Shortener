import pyshorteners

# Install pyshortners lib for shortening the urls - pip install pyshortners


user_url = input("enter your url: ")
# user enters the url
s = pyshorteners.Shortener() 
url_short = s.tinyurl.short(user_url)
print("the shortened url is: ", url_short)
print("Good job! you did it!... WELCOME TULSS TO THE STARTUP CHAPTER ;)")