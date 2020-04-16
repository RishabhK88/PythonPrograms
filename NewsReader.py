from newsapi import NewsApiClient

print("NewsReader")
print("\nReads you News, so you don't have to!")
print("News Categories:")
print("1. Business")
print("2. Entertainment")
print("3. General")
print("4. Health")
print("5. Science")
print("6. Sports")
print("7. Technology")
print("8. All Categories")
cat = input("Enter the required category: ")


def speak(str):

    from win32com.client import Dispatch

    speak = Dispatch("SAPI.spVoice")

    speak.Speak(str)


newsapi = NewsApiClient(api_key='46c9180b9b9e45aaace95b4ad223680e')

if cat == "all categories":
    top_headlines = newsapi.get_top_headlines(language='en',
                                              country='us')

else:
    top_headlines = newsapi.get_top_headlines(category=cat,
                                              language='en',
                                              country='in')

articles = top_headlines["articles"]
print("\n")
for i in (articles):
    print(i["title"])
    speak(i["title"])
    print("\n")
