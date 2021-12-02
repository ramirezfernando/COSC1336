'''
Fernando Ramirez 2030198  
COSC 1336
Homework #3
'''
words = {}
with open("words.txt") as file:
  for line in file.readlines():
    word = line.strip()
    length = len(word)
    if length in words:
      words[length].append(word)
    else:
      words[length] = [word]


# FOR 1
def find_anagram(dict, wish_to_find):
  anagram_list = []
  word_key = len(wish_to_find)
  for word in words[word_key]:
    #if wish_to_find != word and (sorted(word) == sorted(wish_to_find)):
    if sorted(word) == sorted(wish_to_find):
      anagram_list.append(word)
      #print(word)
    else:
      pass
  print(anagram_list)

# FOR 2
def anagram_groups_by_word_length(length_of_words):
  # THIS CONTAINS LISTS INSIDE LISTS
  list_with_lists = []
  for word in words[length_of_words]:
    for other_words in words[length_of_words]:
      if (word, other_words) not in list_with_lists and word != other_words and (sorted(word) == sorted(other_words)):
        list_with_lists.append((word, other_words))
        #print(word,other_word)
      else:
        pass
  # REMOVING LISTS INSIDE AND REPEATING WORDS
  list_without_lists = []
  for lists in list_with_lists:
    for stuff in lists:
      if stuff in list_without_lists:
        pass
      else:
        list_without_lists.append(stuff)
  return list_without_lists
  #return list_with_lists


      



def output():
  print("**************************************************" "\n"
  "1. Find the anagrams of a word" "\n"
  "2. Display the anagram groups by word length" "\n"
  "3. Display the anagram groups by group length" "\n"
  "0. Exit" "\n"
  "**************************************************" "\n")

output()
selection = input("Please enter a selection: ")



if selection == "1":
  wish_to_find = input("Please enter the word you wish to find: ").upper()
  if wish_to_find in words[len(wish_to_find)]:
    print("The anagrams for {} are: ".format(wish_to_find))
    find_anagram(words, wish_to_find)
    
  else:
    print("Sorry, >>{}<< was not found.".format(wish_to_find))
   

if selection == "2":
  length_list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
  length_of_words = int(input("Please enter the length of the words to display(2-15): "))
  if length_of_words in length_list:
    print(anagram_groups_by_word_length(length_of_words))
    print("I found it")
    
  else:
    print("Sorry, >>{}<< is not a valid word length.".format(length_of_words))
    



