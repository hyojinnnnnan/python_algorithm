# [01. 최댓값 찾기]


# 이중 for문
# me.py의 def find_max_num2(array)와 비교해보기
def find_max_num(array):
  for num in array:
    print('>> num: ', str(num))
    for compare_num in array:
      print('    compare_num: ', str(compare_num))
      if num < compare_num:
        print('    num: ', str(num), ' / compare_num: ', str(compare_num),
              ' (Break)')
        break
    else:
      print('    num: ', str(num), ' (Compare to the end)')
      return num


# 지정 변수
# me.py의 def find_max_num(array)와 비교해보기
def find_max_num2(array):
  max_num = array[0]
  print('>> current max_num: ', str(max_num))
  for num in array:
    print('    num: ', str(num))
    if num > max_num:
      print("    *num is bigger than current max_num, change max_num to num")
      max_num = num
  return max_num
