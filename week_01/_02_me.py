# str.isalpha() : 해당 문자열이 알파벳인지 여부 확인 : return : True / False
'''
print("a".isalpha())    # True
print("1".isalpha())    # False

s = "abcdefg"
print(s[0].isalpha())   # True
'''
# ord() : 문자를 아스키코드 변환
'''
print(ord('a')) -> 97
print(ord('a')-ord('a')) -> 0
print(ord('b')-ord('a')) -> 1
print(ord('c')-ord('d')) -> 2
'''

input = "hello my name is sparta"
alphabet_occurrence_array = [0] * 26


def find_max_occurred_alphabet(string):
  # 이 부분을 채워보세요!
  return "a"


result = find_max_occurred_alphabet(input)
print(result)
