import math

pupils_in_class_1 = int(input("Enter pupils in class 1: "))
pupils_in_class_2 = int(input("Enter pupils in class 2: "))
pupils_in_class_3 = int(input("Enter pupils in class 3: "))
pupils_at_the_desc_max = 2

print("Descs_in_class_1: ", math.ceil(pupils_in_class_1 / pupils_at_the_desc_max))
print("Descs_in_class_2: ", math.ceil(pupils_in_class_2 / pupils_at_the_desc_max))
print("Descs_in_class_3: ", math.ceil(pupils_in_class_3 / pupils_at_the_desc_max))
