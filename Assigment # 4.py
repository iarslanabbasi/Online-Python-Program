#!/usr/bin/env python
# coding: utf-8

# In[39]:


#Make a calculator using Python with addition , subtraction ,multiplication ,division and power

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("Enter the operator you want to perform");
operator=input("Enter any operator for operation +, -, *, /,**  ")
result=0
if operator=='+':
   result=num1+num2;
elif operator=='-':
   result=num1-num2;
elif operator=='*':
   result=num1*num2;
elif operator=='/':
   result=num1/num2;
elif operator=='**':
   result=num1**num2;
else:
  print("Your input is not supported");
print(num1,operator,num2,": ",result)


# In[3]:


#Print integer value in list
thislis = ["mango","aam",14,15,"bannan","laddo"]

for i in thislis:
    if type(i)==int:
     print(i)


# In[5]:


# write scrip to add a key
thisdic={ "car" : "corola","make":"toyota","model":2001,}

thisdic["color"]="White"

print(thisdic)


# In[ ]:


#sum integer in the dic
dict = {"a":8, "b":2, "c": 3}
nums = dict.values()

total = sum(nums)

print(total)


# In[24]:


# Duplicate value from the list

list=[1,2,3,4,5,2,3,4,7,9,5]
l1=[]
for i in list:
    if i not in l1:
        l1.append(i)
    else:
        print(i,end=' ')


# In[62]:


#Q6-Write a Python script to check if a given key already exists in a dictiona
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
  if x in d:
      print('Key is present in the dictionary')
  else:
      print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

