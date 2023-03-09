def find_max_num(array):  #이중 for문
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


def find_max_num2(array):  #지정 변수
  return 0