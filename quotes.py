# try:
#     quotes = [
#     {
#         "text": "Success is not final.",
#         "author": "Winston Churchill"
#     },
#     {
#         "text": "Stay hungry, stay foolish.",
#         "author": "Steve Jobs"
#     },
#     {
#         "text": "Code is like humor.",
#         "author": "Cory House"
#     }
#     ]
#     choice = int(input("Choose a quote(0-2): "))

#     print("----------------------------")

# #     print(quotes[choice]["text"])
# #     print(f"- {quotes[choice]['author']}")
# #     print("----------------------------")
# # except IndexError:
# #     print("Invalid Choice")
# # except ValueError:
# #     print("Please enter a number")
# import random
# try:
#     quotes = [
#     {
#         "text": "Success is not final.",
#         "author": "Winston Churchill"
#     },
#     {
#         "text": "Stay hungry, stay foolish.",
#         "author": "Steve Jobs"
#     },
#     {
#         "text": "Code is like humor.",
#         "author": "Cory House"
#     }
#     ]
#     quote = random.choice(quotes)
#     print("----------------------------")

#     print(quote["text"])
#     print(f"- {quote['author']}")
#     print("----------------------------")
# except IndexError:
#     print("Invalid Choice")
# except ValueError:
#     print("Please enter a number")


# Third Version
import random

try:
    quotes = [
        {

        },
        {
            "text" : "nepal hami nepali sabaiko sajha ghar ho",
            "author": "Manish Pandey"
        },
        {
            "text" : "Happy birthday to you",
            "author": "ramesh kaka"
        },
        {
            "text" : "oh ho vailai kasto chitikka dekhiyo",
            "author": "kapada pasale"
        },
        {
            "text" : "good morning, tell me how can i help you",
            "author": "chatgpt"
        },
    ]
    
    quote = random.choice(quotes)
    print("==== Random Qoute Generator ====")

    print("1. Show Qoute")
    print("2. Exit")

    choose = int(input("Choose: "))



    if choose == 1:
        print(quote["text"])
        print(f"- {quote['author']}")
    else:
        print("Good Bye!")
except IndexError:
    print("Invalid Choice!")
except ValueError:
    pirnt("Enter number 1-2 only")