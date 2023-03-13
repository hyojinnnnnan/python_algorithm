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


def find_max_occurred_alphabet(p_input):
  """
  최빈값 찾기 : 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환
  """
  alphabet_occurrence_array = [0] * 26  # 초기화
  standard = ord('a')  # 97
  max_idx = 0  # 초기화 : 제일 많이 나온 알파벳이 저장된 위치(index)

  for item in p_input:
    print(f">> check item : {item}")

    if item.isalpha() == True:
      alphabet_idx = ord(item) - standard  # 예) ord('c') - 97 = 2
      print(f"save '{item}' into alphabet_occurrence_array[{alphabet_idx}]")
      print(
        f"current alphabet_occurrence_array[{alphabet_idx}] : {alphabet_occurrence_array[alphabet_idx]}"
      )

      alphabet_occurrence_array[alphabet_idx] += 1
      print(
        f"+1 alphabet_occurrence_array[{alphabet_idx}] : {alphabet_occurrence_array[alphabet_idx]}"
      )

      item_occurrence = alphabet_occurrence_array[alphabet_idx]
      if item_occurrence > alphabet_occurrence_array[max_idx]:
        max_idx = alphabet_idx

  return chr(
    max_idx +
    97), max_idx, alphabet_occurrence_array[max_idx], alphabet_occurrence_array


input = "hello my name is sparta"
result = find_max_occurred_alphabet(input)
print("=========================")
print(f"result : {result}")
