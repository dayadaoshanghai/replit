# # 循环方法实现
# def check_palindrome(word_list):
#     start = 0
#     end = len(word_list) - 1
#     while start < end:
#         if word_list[start] != word_list[end]:
#             return False
#         else:
#             start += 1
#             end -= 1
#     return True

# 递归方法实现
def check_palindrome(word_list, start, end):
    if start >= end:
        return True
    if word_list[start] != word_list[end]:
        return False
    return check_palindrome(word_list, start + 1, end - 1)

def main():
  print("🌟Palindrome Checker🌟")
  word = input("Input a word>")
  standarlize = word.lower() 
  word_list = list(standarlize)
  if check_palindrome(word_list, 0, len(word_list)-1):
    print("The word is a palindrome")
  else:
    print("The word is not a palindrome")

if __name__ == "__main__":
  main()