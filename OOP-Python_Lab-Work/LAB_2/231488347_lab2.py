#Q1
'''

mys={"al":53, "ah":23,"ab":62}


def ageing(dictt):
     for i in dictt:
          dictt[i]=dictt[i]+1
     print(dictt)
ageing(mys)


#Q2
#input doc is, "input_count.txt"
user_file=input("Please enter your file:")
infile=open(user_file, "r")
line=infile.readline()
word_list=[]
counter=0
length=0
count=0

while line!="":
     word_list.append(line)
     counter+=1
     
     line=infile.readline()
     

for i in range(0,len(word_list)):
     count+=1
     length=len(word_list[i])+length
     

print("char count is:",(length-count)+1)     
print("word count is:",len(word_list))
print("line count is:",counter)

infile.close()

'''
#Q3

infile=open("input_censor.txt","r")
outfile=open("censored_txt","w")
line=infile.readline()

censor_list=[]

while line!="":
     sen_list=line.split(" ")
     line=infile.readline()
     
for i in range(0,len(sen_list)):
     if sen_list[i]== "abuse"  or sen_list[i]== "drugs"  or sen_list[i]== "C++":
          censor_list.append(sen_list[i])
print(censor_list)

##this only adds bad words from a file to a list. Wasnt able to write and censor the bad words in
##a new file in time.

     


          
infile.close()
outfile.close()




























