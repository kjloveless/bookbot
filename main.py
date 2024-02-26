def letter_count(file_contents):
  lower_file_contents = file_contents.lower()
  result = {}
  for char in lower_file_contents:
    if char in result:
      result[char] += 1
    else:
      result[char] = 1
  return result

def num_words(file_contents):
  words = file_contents.split()
  return len(words)

def sort_func(dict):
  return dict[1]

def print_report(file_path, num_words, char_dict):
  print(f"--- Begin report of {file_path} ---")
  print(f"{num_words} words found in the document\n\n")
  
  list_of_dict = list(char_dict.items())
  list_of_dict.sort(reverse=True, key=sort_func)
  for item in list_of_dict:
    key = item[0]  
    if not key.isalpha():
        continue
    print(f"The '{key}' character was found {char_dict[key]} times")
  print("--- End report ---")

def read_file(file_path):
  with open(file_path) as f:
    return f.read()

def main():
  file_path = "books/frankenstein.txt"
  file_contents = read_file(file_path)
  number_words = num_words(file_contents)
  char_dict = letter_count(file_contents)
  print_report(file_path, number_words, char_dict)

main()
