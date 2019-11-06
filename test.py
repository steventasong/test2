# 1 - create a list, then fill it with 30 random mbers ######################################################
import random
alist=[]
for x in range(30):
    i = random.randint(1, 100)
    alist.append(i)

print(alist)
print("End of 1 ========================================================================")

# 2 - create method (in a class) that returns the name and id of the instance of the object ##################
print()
class User:
    def __init__(self, f_name, l_name, id):
        self.f_name = f_name
        self.l_name = l_name
        self.id = id
    def fullname(self):
        return '{} {}'.format(self.f_name, self.l_name)

user1 = User('steven', 'song', '12345')
print(user1.fullname())
print(user1.id)
print("End of 2 ========================================================================")
# 3 - given an interger array, find the smallest missing positive integer ###################################
print()
inputArray = [1, 2, 3, 4, 0, 0, 0]

for i in range(1, len(inputArray)+2):
    # print(i)
    if i not in inputArray:
        print(i)
        break
print("End of 3 ========================================================================")
# 4 - what is the difference between yield and return ########################################################
print()
print("Return - cause a function to exit")
print("Return - all local variables are destroyed")
print("Return - is used when a function is ready to send a value back to its caller")
print("Yield - is used to define generators")
print("Yield - it replace the return value of a function to suspend its execution without destroying local variables")
print("Yield - this is used when the generator returns an intermediate result to the caller")

print("End of 4 ========================================================================")
print()
# 5 - remove duplicate
weekdays = ['sun', 'mon', 'tue', 'sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
unique = []
for i in weekdays:
    if i not in unique:
        unique.append(i)
print(unique)
print("End of 5 ========================================================================")
print()
# 6 - read a file in python
print("python code to read a text file")
print("opened_file = open('Documents/shakespeare.txt')")
print("text_data = list(opened_file)")

print("End of 6 ========================================================================")
print()
# 7 - write csv in python, write csv in scala
print("python code to write into a CSV file")
print(r"with open('shakes_word_count.csv', 'w') as csv_file:")
print(r"    [csv_file.write('{0},{1}\n'.format(key, value)) for key, value in sorted_word_counting.items()]")


print("End of 7 ========================================================================")
