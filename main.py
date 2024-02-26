def letter_count(file_contents):
  lower_file_contents = file_contents.lower()
  result = {}
  for char in lower_file_contents:
    if char in result:
      result[char] += 1
    else:
      result[char] = 1
  print(result)

def num_words(file_contents):
  words = file_contents.split()
  print(len(words))

def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)
    num_words(file_contents)
    letter_count(file_contents)

main()
