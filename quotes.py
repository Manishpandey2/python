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
# import random

# try:
    # quotes = [
    #     {

    #     },
    #     {
    #         "text" : "nepal hami nepali sabaiko sajha ghar ho",
    #         "author": "Manish Pandey"
    #     },
    #     {
    #         "text" : "Happy birthday to you",
    #         "author": "ramesh kaka"
    #     },
    #     {
    #         "text" : "oh ho vailai kasto chitikka dekhiyo",
    #         "author": "kapada pasale"
    #     },
    #     {
    #         "text" : "good morning, tell me how can i help you",
    #         "author": "chatgpt"
    #     },
    # ]
    
#     quote = random.choice(quotes)
#     print("==== Random Qoute Generator ====")

#     print("1. Show Qoute")
#     print("2. Exit")

#     choose = int(input("Choose: "))



#     if choose == 1:
#         print(quote["text"])
#         print(f"- {quote['author']}")
#     else:
#         print("Good Bye!")
# except IndexError:
#     print("Invalid Choice!")
# except ValueError:
#     pirnt("Enter number 1-2 only")

#another version

import random
import json
with open("quotes.json","r") as file:
    quotes = json.load(file)

print("=== Random Qoute Generator ====")

fav = None
count = 0   

while True:
     
    print("1. Show Qoute")
    print("2. Exit")
    print("3. Add Yours")
    print("4. Remove a quote")
    print("5. Search by Author")
    print("6. Favourite Quote")
    print("7. Show all Quote")
    quote = random.choice(quotes)
    try:
        choose = int(input("Choose: "))
    except ValueError: 
        print("Enter a number")
        continue
    if choose == 1:
        print("-----------------------")

        print(quote["text"])
        print(f" - {quote['author']}")
    
        print("-----------------------")
        fav = input("To pick your favourte quote write authors name: ").strip().lower

        count += 1
        print(f"You saw {count} times quote")

    elif choose ==2:
        print("Good Bye!")
        break
    elif choose ==3:
        text = input("Enter Qoute: ")
        author = input("Enter Author Name: ")
        quotes.append({"text" : text, "author" : author})
        with open("quotes.json","w") as file:
            json.dump(quotes, file, indent = 4)
    elif choose == 4:
        print("All Qoutes")
        
        for i, quote in enumerate(quotes):
            print(f"{i} - {quote['text']}")
        remove = int(input("Enter the index value of quote which you want to delete: "))
        
        del quotes[remove]
        with open("quotes.json","w") as file:
            json.dump(quotes, file, indent = 4)
    elif choose == 5:
        Author = input("Author Name: ").strip().lower()
        Found = False
        for quote in quotes:
            if quote["author"].strip().lower() == Author:
                        print("-----------------------")

                        print(quote["text"])
                        print(f" - {quote['author']}")
    
                        print("-----------------------")
                        Found = True
        if not Found:
            print("There is no such authors")
    elif choose == 6:
        
        if fav==None : 
            print("There is no favourite quote selected yet")
        for quote in quotes:
            if quote["author"].strip().lower() == fav:
                print("-----------------------")

                print(quote["text"]);
                print(f" - {quote['author']}")
                print("-----------------------")
        

    elif choose == 7: 
        print("================ All Quote =====================")
        for i , quote in enumerate(quotes):
            print(i)
            print(quote['text'])
            print(f" - {quote['author']}")
            print("***********************")
    else:
        print("Invalid Choice")
