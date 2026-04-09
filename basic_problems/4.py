check_list = [1,2,3,5,3,5,6,3,7,9,4,2,4,6,7,8,1,3,6,8,9,5,4,2,3,5,6,7]

n= len(check_list)

freq_map = {}

for i in range(0,n):
    if check_list[i] in freq_map:
        freq_map[check_list[i]]+=1
    else:
        freq_map[check_list[i]]=1    


print(freq_map)