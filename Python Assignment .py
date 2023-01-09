#%%     
def problem2_1():
    lis = list(range(20,30))
    print(lis[3])
    print(lis)
    sum_=0
    for i in range(len(lis)):
        sum_ = sum_ + lis[i]
        print(lis[i], end=" ")
    print()

#%%
#%%  

alist = ["a","e","i","o","u","y"]
blist = ["alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta"] 

def problem2_2(my_list):
    print(my_list)
    print(my_list[0])
    print(my_list[-1])
    print(my_list[3:5])
    print(my_list[:3])
    print(my_list[3:])
    print(len(my_list))
    my_list.append("z")
    print(my_list)
    
#%%
newEngland = ["Maine","New Hampshire","Vermont", "Rhode Island", 
"Massachusetts","Connecticut"]

def problem2_3(ne):
    for i in ne:
        print(i,"has",len(i),"letters.") 
        
#%%
import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    num = []
    for i in range(0,10):
        num.append(random.uniform(30,35))
    print(num)
#%%
import random

def problem2_5():
    """ Simulates rolling a die 10 times."""
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(171)  # don't remove when you submit for grading
    for i in range(10):
        num=(random.randint(1,6))
    print(num)
#%%
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed()  # don't remove when you submit for grading
    for i in range(100):
        die1=random.randint(1, 6)
        die2=random.randint(1, 6)
        print(die1+die2)
#%%

def problem2_7():
    """ computes area of triangle using Heron's formula. """
    a=float(input("Enter length of side one: "))
    b=float(input("Enter length of side two: "))
    c=float(input("Enter length of side three: "))
    s = .5*(a + b + c)
    x=(s*(s-a)*(s-b)*(s-c))
    #if x > 0:
    area=(x**.5)
    #else:
        #area=0
    print("Area of a triangle with sides ", a, b, c, "is",area)
#%%
hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]
    
def problem2_8(temp_list):
    sum_=0
    for i in temp_list:
        sum_=sum_+ i
    print("average:",sum_/len(temp_list))
    print("High:",max(temp_list))
    print("Low:",min(temp_list))
    
#%%
def problem3_1(txtfilename):
    pass # replace this pass (a do-nothing) statement with your code
    text_file = open(txtfilename)     # open the file for reading

    # initialize line, word, and char counters to 0
        
    letters = 0

    for line in text_file: 
          # step through each line in the text file
        print(line,end="")
        letters = letters + len(line)
        

    text_file.close()
    print("\n")                
    print("There are",letters,"letters in the file." )


#%%
nlis = [23,64,23,46,12,24]          # list
atup = ("c","e","a","d","b")        # tuple
str1 = "Rumplestilskin"             # string

#%%
def problem3_2(collection):
    for i in collection:
        print(i)

#%%
def problem3_3(month, day, year):
    
    """ Takes date of form mm/dd/yyyy and writes it in form June 17, 2016 
        Example3_3: problem3_3(6, 17, 2016) gives June 17, 2016 """
    pass # replace this pass (a do-nothing) statement with your code
    month_name=("January","February","March","April","May","June","July","August",
           "September","October","November","December")
    monthStr = int(month) - 1
    print(month_name[monthStr], str(day) + ",", year)
    

#%%
def problem3_4(mon, day, year):
    """ Takes date such as July 17, 2016 and write it as 7/17/2016 """
    pass # replace this pass (a do-nothing) statement with your code
    months={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
            "August":8,"September":9,"October":10,"November":11,"December":12}
    print(str(months[mon]),str(day),year,sep="/")

#%%

def problem3_5(name):
    """ Looks up the phone number of the person whose name is name """
    
    phone_numbers = {"abbie":"(860) 123-4535", "beverly":"(901) 454-3241", \
                      "james": "(212) 567-8149", "thomas": "(795) 342-9145"}
    print(phone_numbers[name])


#%%
import csv
def problem3_7(csv_pricefile, flower):
    infile = open(csv_pricefile)
    reader = csv.reader(infile)
    for row in reader:
        if row[0] == flower:
            print(row[1])    
#%%