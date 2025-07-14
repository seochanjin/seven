# a = int(input())
# b = []

# for i in range(a):
#     b.append(int(input()))

# c = max(b)
# d=[]

# for i in range(2, c+1):
#     idx = 1
#     for j in range(2, i):
#         if i%j == 0:
#             if i == j:
#                 break
#             idx = 0

#     if idx == 1:
#         d.append(i)
# #d는 최댓값 이하의 소수들
# #c = 16 일때 [2, 3, 5, 7, 11, 13]

# f=[]

# for i in range(a):
#     g=[]
#     for j in range(len(d)):
#         for k in range(len(d)):
#             if b[i]==d[j]+d[k] and d[j]<=d[k]:
#                 g.append([d[j], d[k]])
#                 #[[3, 5], [3, 7], [5, 5], [3, 13], [5, 11]]
#     f.append(g)
# #[  [[3, 5]],   [[3, 7], [5, 5]],   [[3, 13], [5, 11]]  ]
# # i가 3개, j가 1, 2, 2개 , K가 2개씩

def get_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit+1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

a = int(input())
b = [int(input()) for _ in range(a)]
c = max(b)
d = get_primes(c)

f = []
for i in range(a):
    g = []
    for j in range(len(d)):
        for k in range(j, len(d)):  # d[j] <= d[k] 조건 만족을 위해 k 시작은 j
            if b[i] == d[j] + d[k]:
                g.append([d[j], d[k]])
    f.append(g)




for i in range(a):
    if len(f[i]) == 1:
        print(f[i][0][0], f[i][0][1])
    else:
        # for j in range(len(f[i])):
        #     for k in range(len(f[i][j])):
        #         min_0 = f[i][j][0]
        #         min_1 = f[i][j][1]
        #         min_s = abs(min_0-min_1)
        #         if min_s >= abs(f[i][0][0] - f[i][0][1]):
        #             min_0 = f[i][j][0]
        #             min_1 = f[i][j][1]
        # print(min_0, min_1)
        min_pair = f[i][0]
        min_diff = abs(f[i][0][0] - f[i][0][1])
        for j in range(1, len(f[i])):
            diff = abs(f[i][j][0] - f[i][j][1])
            if diff < min_diff:
                min_diff = diff
                min_pair = f[i][j]
            print(min_pair[0], min_pair[1])