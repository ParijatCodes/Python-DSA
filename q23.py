#search for a keyword

interest= input("Type your interest:")

topic = "This python tutorial is awesome to start learning AI"

if(interest.lower() in topic.lower()):
    print(topic)
else:
    print("No Topic Found")