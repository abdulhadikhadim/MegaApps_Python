import requests
# from email_info import send_email
topic = input("Enter the topic you want the news for like (apple/tesla...)")
api_key = '428b10b5a2cf4fe5a87f51f104918fb0'
url = '''https://newsapi.org/v2/everything?q=f"{topic}"&sortBy=publishedAt&apiKey=428b10b5a2cf4fe5a87f51f104918fb0&language=en'''

r = requests.get(url)
content = r.json()

body = ' '
for article in content['articles'][0:20]:
    body += "Subject: Today's News"+ '\n' + (article['title'] + '\n' 
             + article['description'] + '\n' 
             + article['url'] + '\n\n')
print(body)

body.encode('utf-8')
send_email(message = body)

# import requests

# url = "https://en.wikipedia.org/wiki/Cat#/media/File:Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi-01A.jpg"

# r = requests.get(url)

# with open('images.jpg', 'wb') as file:
#     file.write(r.content)