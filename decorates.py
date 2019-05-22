# decorates extends the behaviour of a function without modifying the
#function itself

def cough_dec(func):

   def func_wrapper():
      #code before function
       print ('*cough*')
       #code after function
       print('*cough*')

   return func_wrapper





@cough_dec
def question():
   print('can you give me a discount on that?')

@cough_dec
def answer():
    print("it'sonly 50p you cheapskate")

question()