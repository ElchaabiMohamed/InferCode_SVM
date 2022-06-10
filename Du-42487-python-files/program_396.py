print("Enter an age in digits to see if a person of that age may climb everest")
age = int(eval(input()))
may_climb_everest = age < 75 and age > 18

print(("A person of age", age, "may climb Everest:", may_climb_everest))
