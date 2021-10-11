class BaseConverter:

    print('Hello!, this is a base converter that can convert one base to any other base.')
global start_base
global numtoconvert
global end_base
''' This is where information for what to convert from and to are taken'''

print("Please type the base that your number is in (i.e. \'10\')  ")
start_base = input()
start_base = int(start_base)
print('What number are you converting?')
numtoconvert = input()
numtoconvert = int(numtoconvert)

for i in str(numtoconvert) :
   if i >= str(start_base):
      print("What is wrong with you")
      exit()

print('What base do you want to convert your number to: ')
end_base = input()
end_base = int(end_base)

'''This is where the functions will be put '''

def Base(n):
    ListofModulo = []
    #lets work off the octal example
    if start_base != 10:
       n = list(str(n)) #n is now a list
       mkeys = []
       e = 0
       n = n[::-1]
       for i in n:
          mkeys.append(int(i)*(start_base**e))
          e += 1
       n_sum = 0
       for i in mkeys:
           n_sum += i
       n = n_sum


    while n>0:
        m = n % end_base
        ListofModulo.append(m)
        n = n // end_base #use of floor division
        number = ListofModulo[::-1]
        stringofnum = [str(number) for number in number] #gives this individual strings in a listformat 
        joinofnum = ''.join(stringofnum) #joins all string into one string
        number = int(joinofnum) #turn string to int
    return number


#If endbase is equal to this base
#call this base's  function

print(Base(int(numtoconvert)))












