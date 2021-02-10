with open('students.txt') as students:
   lines = students.readlines()

print(lines)

clean = []

for line in lines:
   clean.append(line.split('\t'))

print(clean)

stripped = []

for student in clean:
   for word in student:
      stripped.append(word.strip())

print(stripped)

student_data = list(filter(lambda x: len(x) > 0, stripped))[3:]

print(student_data)

stu = []

for i in range(0,len(student_data), 3):
   chunk = student_data[i: i+3]
   stu.append(tuple(chunk))

print(stu)
