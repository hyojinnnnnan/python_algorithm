# .replit : run = "python3 main.py"
'''
.replit 이란 어떤 파일을 main 으로 지정하고 실행할 지 적는 config 파일인 셈입니다.
run = "" 안에 들어가는 구문은 리눅스 OS에서 해당 파일을 run 시키는 bash명령어 입니다.
'''

input = "hello my name is jin"  # length : 20 / index : 0~19
alphabet_occurrence_arr = [0] * 26


def find_max_occurred_alphabet(p_string):
  for idx in range(len(p_string)):
    print(idx)
  return "a"


result = find_max_occurred_alphabet(input)
print(result)