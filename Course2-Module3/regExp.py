import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR[321] Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

#Basic Regular Expressions

import re
result = re.search(r"aza", "plaza")
print(result)

import re
result = re.search(r"aza", "bazaar")
print(result)

import re
result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "penguin"))
print(re.search(r"latur.", "laturs"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

#Wildcards and character classes

import re
print(re.search(r"[a-z]way", "The end of the highway"))
print(re.search(r"[a-z]way", "What a way to go"))
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

import re
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both cats and dogs."))

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
print(re.findall(r"cat|dog", "I like both dogs and cats."))

print(re.findall("Python", "Me gusta Python porq su sintaxis es sencilla. Python mola")).span()

#Repetition qualifiers

import re
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))

import re
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

import re
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))

##Quiz
import re
def repeating_letter_a(text):
  result = re.search(r"[Aa].*a", text)
  return result != None

print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True

#Escaping characters

import re
print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))

import re
print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

##Quiz

import re
def check_character_groups(text):
  result = re.search(r"[\w]+\s", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

#Regular expressions in action

import re
print(re.search(r"A.*a", "Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia"))

import re
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))

##Quiz

import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s]*[\.\?\!]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True

#Quiz final
#Question 1
#The check_web_address function checks if the text passed qualifies as a top-level web address, 
#meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), 
#as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain
# such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, 
#wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.

import re
def check_web_address(text):
  pattern = r"^[A-Za-z_][\.A-Za-z0-9_-]*[\.A-Za-z]$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

#Question 2
#The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12,
#with no leading zero, followed by a colon, then minutes between 00 and 59, then an optional space, 
#and then AM or PM, in upper or lower case. Fill in the regular expression to do that. How many of the concepts 
#that you just learned can you use here?

import re
def check_time(text):
  pattern = r"[1-12:[0-5][0-9] ?[AM-PMam-pm]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

#Question 3
#The contains_acronym function checks the text for the presence of 2 or more characters or digits 
#surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if 
#the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication 
#technologies used for text-based communication" should return True since (IM) satisfies the match conditions." 
#Fill in the regular expression in this function: 

import re
def contains_acronym(text):
  pattern = ___ 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

#Question 4
#An intern implemented a zip code checker, but it works only with five-digit zip codes. 
#Your task is to update the checker so that it includes all nine digits of the zip code; the leading five digits 
#and the optional four after the hyphen. The zip code needs to be preceded by at least one space, and cannot 
#be at the start of the text. Update the regular expression.

import re

def correct_function(text):
  result = re.search(r"[A-Z]* \d{5}-?[\d{4}]?", text)  # Corrected regex pattern with space
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False
