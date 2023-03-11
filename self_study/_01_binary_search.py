# [01. 이진탐색]
''' 
(문제) 
숫자가 작은 수 ->큰 수 순으로 정렬된 배열 하나와 아이템 하나를 받아 
배열 안에 아이템이 있으면 아이템의 위치를 반환하라
'''


def binary_search(p_list, p_item):
  from_idx = 0
  to_idx = len(p_list) - 1

  while from_idx <= to_idx:
    mid_idx = (from_idx + to_idx) // 2
    print(f"from_idx : {from_idx}, to_idx : {to_idx}, mid_idx : {mid_idx}")
    guess_num = p_list[mid_idx]
    print(f"p_list[{mid_idx}] : {guess_num}")

    if guess_num == p_item:
      print(f">>> guess_num({guess_num}) == p_item({p_item})")
      return mid_idx
    if guess_num > p_item:
      print(f">>> guess_num({guess_num}) > p_item({p_item})")
      to_idx = mid_idx - 1
    else:
      print(f">>> guess_num({guess_num}) < p_item({p_item})")
      from_idx = mid_idx + 1
    print("=" * 30)

  return None


my_list = [1, 3, 5, 7, 9]
print(">>> index : ", binary_search(my_list, 10))
