import numpy as np

a = np.arange(27).reshape(3,3,3)  # arange : 0~14 배열 생성, reshape : 3행 5열로 정렬

#print(a)
#print(a.shape)      # shape 행렬 모양 data화
#print(a.ndim)       # 배열의 차원수 (예제는 2차원)


# a_arr = np.array(range(1,11), dtype = 'int32')
# print(a_arr.size)
# print(a_arr.itemsize)
# print(a_arr)

# p_num = np.random.rand(6)
# print(p_num)

n = int(input("n 입력해"))
a = np.ones((n,n),dtype = 'int64')

for i in range(0,n):
    if(i % 2==1):
        for j in range(0,n):
            if(j % 2 == 1):
                a[i,j] = "1"
            else:
                a[i,j] = "0"
    else:
        for j in range(0,n):
            if(j % 2 == 0):
                a[i,j] = "1"
            else:
                a[i,j] = "0"

print(a)           # 바둑판 생성

