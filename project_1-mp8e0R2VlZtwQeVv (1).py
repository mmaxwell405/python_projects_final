import random

#Lists containing possible password characters
items_list_cap=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
items_list_lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
items_list_punc=['!','@','%',"$","*",'#','?','&','~']
items_list_nums=['1','2','3','4','5','6','7','8','9','0']

again=True
total_length=0

#Prompt asking for the length of the password

length_pass=int(input("How long do you want your password? "))

#Loop for asking how many of each charater type the user wants.
#If less than or greater than given length, user has to retry 
while again==True:
    char_left=length_pass
    total_length=0

    length_sc=int(input('How many special characters? ('+str(char_left)+' characters left): '))
    char_left=char_left-length_sc
    
    if char_left>0:
      length_lower=int(input('How many lowercase letters?('+str(char_left)+' characters left): ' ))
      char_left=char_left-length_lower
    else:
      length_lower=0
    
    if char_left>0:
      length_caps=int(input('How many capital letters? ('+str(char_left)+' characters left): '))
      char_left=char_left-length_caps
    else:
      length_caps=0

    if char_left>0:
      length_nums=int(input('How many numbers? ('+str(char_left)+' characters left): '))
    else:
      length_nums=0

    total_length=length_sc+length_caps+length_nums+length_lower

    #Check to see if user is under or over stated password length
    if  total_length>length_pass:
        print('Thats more than the password length, you must have less than',length_pass,'characters, try again')
    elif total_length<length_pass:
       print('Thats less than the password length, you must have at least',length_pass,'characters, try again')
    else:
        again=False

#Outfile to store password
outfile=open(r'D:\Random stuff\project.txt', 'w')

#List to store random characters
pass_list=[]

#Loops for selecting characters 
for i in range(length_sc):
    r_sc=random.choice(items_list_punc)
    pass_list.append(r_sc)

for i in range(length_lower):
    r_lower=random.choice(items_list_lower)
    pass_list.append(r_lower)

for i in range(length_caps):
    r_caps=random.choice(items_list_cap)
    pass_list.append(r_caps)

for i in range(length_nums):
    r_nums=random.choice(items_list_nums)
    pass_list.append(r_nums)

#Shuffles list so that charaters are in a random order
random.shuffle(pass_list)

#Puts each character into outfile 
for i in pass_list:
        outfile.write(i)

outfile.close()

#Read the password in saved file
infile=open(r'D:\Random stuff\project.txt', 'r')

read_file=infile.read()

infile.close()

print('Your generated password is: '+read_file)