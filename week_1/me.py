def find_max_num(array):
  max = 0
  for i in range(len(array) - 1):
    print('>> Current max num is : ', str(max))
    num1 = array[i]
    num2 = array[i + 1]

    print('    Compare array[', str(i), '] and array[', str(i + 1), '] : ',
          str(num1), ', ', str(num2))
    if num1 > num2:
      result = num1
    else:
      result = num2

    print('    Compare max and [num1/num2] : ', str(max), ', ', str(result))
    if max > result:
      max = max
    else:
      max = result
      
  return max


def find_max_num2(array):
  # 이 부분을 채워보세요
  for num in array:
    num_idx = array.index(num)
    print(">> num : ", str(num))
    for compare_num in array[num_idx + 1:]:
      print("    compare_num : ", str(compare_num))
      if num < compare_num:
        print("--- break ---")
        break
    else:
      return num
