def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f'i am{key} and i am a {val} belt')


ninja_belts ={}


while True:
     ninja_name = input("enter your name")
     ninja_belt = input("enter your belt")
     ninja_belts[ninja_name] = ninja_belt

     another = input('add another ?(y/n)')
     if another == 'y':
        continue

     else:
         break

ninja_intro(ninja_belts)