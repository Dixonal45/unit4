# # project euler problems
#
# # project euler problem 1 (multiples of 3 and 5)
#
# multiples = 0
# for x in range(3, 1000):
#     if (x % 3) == 0 or (x % 5) == 0:
#         multiples = multiples + x
#
# print(multiples)
#
# # project euler problem 2 (even fibonacci numbers)
#
# sum = 0
# a = 1
# b = 1
# for x in range(1, 500):
#     c = a + b
#     if (c % 2) == 0 and c <= 4000000:
#         sum = sum + c
#     a = b
#     b = c
#
# print(sum)

# project euler problem 3

root = (float(600851475143 ** (1/2)))
for x in range(1, root):
