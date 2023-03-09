import week_1.me as me
import week_1.lecture as lecture

input = [3, 5, 6, 1, 2, 4]

print("[me.find_max_num]")
print("-" * 50)
result = me.find_max_num(input)
print("=" * 50)
print('>> Max Num is : ', str(result))
print("=" * 50, end="\n")

print("[me.find_max_num2]")
print("-" * 50)
result = me.find_max_num2(input)
print("=" * 50)
print('>> Max Num is : ', str(result))
print("=" * 50, end="\n")

print("[lecture.find_max_num]")
print("-" * 50)
result = lecture.find_max_num(input)
print("=" * 50)
print('>> Max Num is : ', str(result))
print("=" * 50, end="\n")
