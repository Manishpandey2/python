data = {
    "articles": [
        {
            "title": "Python 3.15 Released",
            "author": "Guido"
        },
        {
            "title": "AI Agents are Growing Fast",
            "author": "OpenAI"
        },
        {
            "title": "Nepal Wins Cricket Match",
            "author": "Sports Desk"
        }
    ]
}


articles = data["articles"]
for article in articles:
    print(f"{article['title'],"   >  ",article["author"]}")
