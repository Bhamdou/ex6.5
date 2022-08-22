# #STORY PROGRAM

# """This program should take user input() and based on the choice
# the user made change the course of the story.

# For example:

# print("Youre in a dark alley. Where do you go?")
# print("(1) left (2) straight (3) right")
# choice = input("choose: ")

# if choice == "1":
#    print("u go left and die")
# elif choice == "2":
#    print("u go straight and there is another crossing")
#    #continue tree here
# elif choice == "3": 
#    print("u go right and theres a wall")
# else:
#    print("u just die for inaction")
print("Youre in a dark alley. Where do you go?")
print("(1) left (2) straight (3) right")
choice = input("choose: ")






#1. Import the random module, as it is a built-in module of python.  So, there’s no need to install it manually.
# Importing random module
import random


#2.  Define several lists of phrases. Here, we have defined eight lists. We can define more also, it depends totally on our choice.

# Sentence_starter – This list gives an idea about the time of the event.
# character – This list tells about the main character of this story.
# time – This list defines the exact day on which some incident has occurred.
# story_plot – This list defines the plot of the story.
# place – This list defines the place at which the incident occurred.
# second_character – This list defines the second character of the story.
# age – This list defines the age of the second character.
# work – This list tells about the work the second character was doing.
# Defining list of phrases which will help to build a story
Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']

character = [' there lived a king.',' there was a man named Jack.',
			' there lived a farmer.']

time = [' One day', ' One full-moon night']

story_plot = [' he was passing by', ' he was going for a picnic to ']

place = [' the mountains', ' the garden']

second_character = [' he saw a man', ' he saw a young lady']

age = [' who seemed to be in late 20s', ' who seemed very old and feeble']

work = [' searching something.', ' digging a well on roadside.']
#3. With the help of random.choice() select an item from each list and concatenate the selected items to generate sentences for the story.

# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
	random.choice(time)+random.choice(story_plot)+
	random.choice(place)+random.choice(second_character)+
	random.choice(age)+random.choice(work))

# Output:

# In the 20 BC there lived a king. One day he was going for a picnic to  the mountains he saw a man who seemed to be in late 20s digging a well on roadside.





#Let’s try the full implementation with the help of an example.
# Importing random module
import random

# Defining list of phrases which will help to build a story

Sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
character = [' there lived a king.',' there was a man named Jack.',
			' there lived a farmer.']
time = [' One day', ' One full-moon night']
story_plot = [' he was passing by',' he was going for a picnic to ']
place = [' the mountains', ' the garden']
second_character = [' he saw a man', ' he saw a young lady']
age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
work = [' searching something.', ' digging a well on roadside.']

# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
	random.choice(time)+random.choice(story_plot) +
	random.choice(place)+random.choice(second_character)+
	random.choice(age)+random.choice(work))
