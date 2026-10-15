# Exercise 1
# 202410370110388
# redefine variable

# Before redefine variable
student_id = '202410370110388'
semester = False

print("Before:")
print(student_id, type(student_id))
print(semester, type(semester))

# # Redefine variable
# student_id = 202410370110388
# semester = "Semester 4"

# print("\nAfter redefine variable:")
# print(student_id, type(student_id))
# print(semester, type(semester))

# # Exercise 2
# # Memory Size Experiment
# # 202410370110388

# import sys

# data1 = 123456.5
# data2 = 202410370110388.8

# print('Value = ', data1)
# print('Type  = ', type(data1))
# print('Size  = ', sys.getsizeof(data1), 'bytes\n')

# print('Value = ', data2)
# print('Type  = ', type(data2))
# print('Size  = ', sys.getsizeof(data2), 'bytes')

# # Exercise 3
# # # 202410370110388

# # #Experiment a

# # screen_resolution = (1920, 1080)
# # screen_resolution[0] = 2560

# # 202410370110388
# #Experiment b

# screen_resolution = 1920, 1080
# print(screen_resolution)
# print(type(screen_resolution))

# # Exercise 4

# # 202410370110388
# countdown = tuple(range(88, -1, -3))

# print(countdown)

# Exercise 5
# 202410370110388

# # 1. Create a dictionary with your own data
# student_info = {
#     "name": "Mohamad Akbar Noviandi",
#     "nim": "202410370110388",
#     "semester": 4
# }

# # 2. Add a new key-value pair for your "major"
# student_info["major"] = "Informatics"

# # 3. Try to update an EXISTING key (change semester to 5)
# student_info["semester"] = 5

# print("Current Dictionary:", student_info)

# # 4.  Uncomment the line below to see what happens
# print(student_info["gpa"])

# # Exercise 6
# # NIM: 202410370110388

# NIM = "202410370110388"


# nim_int = int(NIM)
# nim_float = float(NIM)

# print("NIM (int):", nim_int)
# print("Type:", type(nim_int))

# print("NIM (float):", nim_float)
# print("Type:", type(nim_float))


# try:
#     print(int("hello"))
# except ValueError as e:
#     print("Error int:", e)


# try:
#     print(float("hello"))
# except ValueError as e:
#     print("Error float:", e)

# Exercise 7
# # FIX THIS CODE!
# 202410370110388
# calculate_discount(price, discount):
# total = price - (price * discount)
# return total

#    result = calculate_discount(100000, 0.1)
# print("Final Price:", result)

# # 202410370110388

# # Write your fixed code here
# def calculate_discount(price, discount):
#     total = price - (price * discount)
#     return total

# result = calculate_discount(10000, 0.1)
# print("Final Price:", result)

# Exercise 8
#NIM = 202410370110388

def total_sum(n):
    print(f"Current n: {n}")
    if n == 1:
        return 1
    else:
        return n + total_sum(n - 1)

# Running the function
result = total_sum(3)
print("Final Result:", result)