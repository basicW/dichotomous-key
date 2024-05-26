print("Welcome to The Dichotomous Key For Insects.")
print("The insects are: Ladybug, Firefly, Dragonfly, Bee.")

print("1. yes")
print("2. no")

choice = int(input("Are the wings covered by an exoskeleton?(1 OR 2)"))
if choice == 1:
    print("1. yes")
    print("2. no")

    choice_1a = int(input("Does the body have a round shape?(1 OR 2)"))

    if choice_1a == 1:
            print("It's a ladybug.")
    if choice_1a == 2:
          print("It's a firefly")
          print("Since it has an elongated shape")
if choice == 2:
      print("1. yes")
      print("2. no")
      choice_2a = int(input("Do the wings point outward from the body(1 OR 2)"))

if choice_2a == 1:
      print("It's a dragon fly")
if choice_2a == 2:
      print("Wings point toward the rear of the body")
      print("It's a bee")