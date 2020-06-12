# Write a program, which reads weights (lbs.) of N students into a list and convert
# these weights to kilograms in a separate list

n = int(input("Number of students: "))
l1= []
for i in range(n):
    l1.append(float(input("Weight: ")))

output= []
for x in l1:
    output.append(x*0.454)  # Converting lbs into KG

print(output)
