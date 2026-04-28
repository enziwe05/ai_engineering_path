#EXERCISE 3
sentence = "machine learning is the future of technology"

sentCap = sentence.upper()
print(sentCap)
#2
index = sentence.find("learning")
 

#3
replace =  sentence.replace("future", "backbone")
print(replace)

#4 
print(len(sentence))

#5
print(sentence[-10:])

print("------------------------")

#Exercise 4
ai_course = {"title":"AI Engineering Bootcamp", "topics":"a list of 4 topics you learned today", "completed":"False"}
print(ai_course["title"])

#3
ai_course["instructor"] = "Claude"
print(ai_course["instructor"])

#4
x = ai_course["title"].find("Engineering")
print(ai_course["title"][x:x+11])

#
ai_course["completed"] = True
print(ai_course)