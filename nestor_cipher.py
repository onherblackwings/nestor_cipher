#rule 1 must be mapped manually
#no way for Python to recognize letters w/curves or w/o curves

first_rule='AEFHIKLMNTVWXYZBCDGJOPQRSU ' #list all letters w/o curves first


#mapping rule 2

even=[]
odd=[]
cipher=''

c=0

#places all even letters in var even and odd in variable odd
#variable second_rule contains even+odd

while c<len(first_rule):
    if c%2!=0:

        odd.append(first_rule[c])
        
        c+=1
    elif c%2==0:
        even.append(first_rule[c])
        c+=1
    else:
        c+=1
    
second_rule=''.join(odd+even) #even listed first followed by odd

message=raw_input("Enter your message: ").upper()
for i in message:
    if i in first_rule:
        num=first_rule.find(i)
        cipher=cipher+second_rule[num]

print "Your encrypted message is: ", cipher
