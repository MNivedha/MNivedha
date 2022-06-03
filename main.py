#Write a Python program to remove specific words from a given list. 
#Original list:
#['red', 'green', 'blue', 'white', 'black', 'orange']
#Remove words:
#['white', 'orange']
#After removing the specified words from the said list:
#['red', 'green', 'blue', 'black']


def remove_words(list1, remove_words):
      result = list(filter(lambda word: word not in 
      remove_words, list1))
      return result
        
colors = ['red', 'green', 'blue', 'white', 'black', 'orange']
remove_colors = ['white', 'orange']
print("Original list:")
print(colors)
print("\nRemove words:")
print(remove_colors)
print("\nAfter removing the specified words from the said list:")
print(remove_words(colors, remove_colors))