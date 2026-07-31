quotes = [
    {
        "text": "Success is not final.",
        "author": "Winston Churchill"
    },
    {
        "text": "Stay hungry, stay foolish.",
        "author": "Steve Jobs"
    },
    {
        "text": "Code is like humor.",
        "author": "Cory House"
    }
]
choice = int(input("Choose a quote(0-2): "))

print("----------------------------")

print(quotes[choice]["text"])
print(f"- {quotes[choice]['author']}")
print("----------------------------")
