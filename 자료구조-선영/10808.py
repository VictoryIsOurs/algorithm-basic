def count(c, c_list):
    if c.islower() == True:
        c_list[ ord(c) - 97] += 1    #ord() : char->int형 변환
        return c_list


word = list(input())  # !!!!!!! 받을 때부터 list로 받자!!!!!!!

result_list = [0] *26  #소문자를 담을 리스트

for i in word :
    result_list = count(i, result_list)

for i in result_list:
    print(i)
