cities = ["mbabane", "cape town", "nelspruit", "sydney" , "https"]

for city in cities:
    for letter in city:
        if letter in "aeiou":
            print (f"{city} has a vowel")
            break
        else:
            print("kyabhedza")


