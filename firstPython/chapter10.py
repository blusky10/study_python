# import os
# THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(THIS_FOLDER, 'pi_digits.txt')

# print(my_file)

# open 경로는 무조건 소문자???
filepath = 'D:\\STUDY\\study_python\\firstPython\\pi_digits.txt'
with open(filepath) as file_object:
    contents = file_object.read()

print(contents)

filepath = 'D:\\STUDY\\study_python\\firstPython\\pi_digits.txt'
try:
    with open(filepath) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    print("not found")
else:
    print(lines)

    for line in lines:
        print(line.rstrip())

