result_list = [-1] *26  #소문자 index를 담을 리스트

word = list(input())  # !!!!!!! 받을 때부터 list로 받자!!!!!!!

j  = 0 #list의 index, 즉, c의 위치

for i in word :
    index = ord(i) - 97
    if(result_list[index] == -1):
        result_list[index] = j
    j +=1
    
for i in result_list:
    print(i)
