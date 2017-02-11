# nam =raw_input(1)
# print "Welcome",nam

# inp=raw_input("Europe floor")
# usf=int(inp)+1
# print "US Floor",usf


# hours = input ("Hours per week: ")
# rate = input ("Rate per hour: ")
# pay = hours * rate
# print 'Pay:',pay

# try:
    # ival = input('Enter a number ')
    # ival = ival + 0
# except:
    # ival = -2
    
# if ival > 0:
    # print 'Nice work'
# else:
    # print 'Not a positive number'
    
# try: 
    # hours1 = input ("Hours per week: ")
    # rate = input ("Rate per hour: ")  
# except:
    # hours1 = 10
    # rate = 10

# if hours1 > 40:
    # print hours1 * rate + (hours1 -40) * rate *1.5
# else:
    # print hours1 * rate
    
# def hallo():
    # print('hallo')
    
# hallo()

# big = max('HelloWorld')
# print big

# def greet(lang):
    # If lang == 'es':
        # print 'Holla'
    # else:
        # print 'Hallo'

# def computepay():
    # if hours1 > 40:
        # print hours1 * rate + (hours1 -40) * rate *1.5
    # else:
        # print hours1 * rate
        
# hours1 = input ("Hours per week: ")
# rate = input ("Rate per hour: ")

# computepay()

# inp = input("Number to compare ")
# while (inp < 100):
    # if inp > 10:
        # print ("Ole")
    # else:
        # print ("Fuck off")
    # # print ("Why is this happening?")
    # inp = input("Number to compare ")
# print "Good Buy"


# while True:
    # line = raw_input()
    # if line[0]  == '#':
        # continue
    # if line == 'done':
        # break
    # print line
# print 'Done' 

# for i in [5,4,3]:
    # print i
# print 'finish'    


# largest_temp = None
# print 'Before' , largest_temp
# for thing in [9,41,12,3,74,15]:
    # if largest_temp is None:
       # largest_temp = thing
    # elif largest_temp > thing:
       # largest_temp = thing
    # print largest_temp , thing    
# print 'after', largest_temp    


# fruit = 'banana'
# print len(fruit)

# zot = 'abc'
# print zot[1]

# fruit = 'banana'
# for letter in fruit:
    # print letter
    
# s = 'qwertyuiop'
# print s[0:5]

# data = 'X-DSPAM-Confidence:    0.8475'
# x = data.find(':')
# number = data [x +1 : ]
# final = number.strip()
# next = float(final)
# ole = int(next)
# print ole

# y = 0
# fhand = open('mbox.txt')
# for line in fhand:
    # x = line.find('From')
    # if x == -1:
        # y = y + 1
# print y        
   


# fname = raw_input('name of the file: ') 
# fhand = open(fname)
# for line in fhand:
    # line = line.rstrip()
    # line = line.upper()
    # print line
    
    
# fname = raw_input('name of the file: ') 
# y = 0
# z = 0
# broi = 0
# fhand = open('mbox.txt')
# for line in fhand:
    # line = line.rstrip()
    # if line.startswith('X-DSPAM-Confidence:'):
        # broi = broi + 1
    # if line.startswith('X-DSPAM-Confidence:'):
        # f = line.find(':')
        # x = line [f+2 :]
        # z = float(x)
        # y = z + y
        
# result = y / broi        
# print result

# print range(4)     


# numlist = list()
# while True:
    # inp = raw_input('name of the file: ')
    # if inp == 'done': break
    # value = float(inp)
    # numlist.append(value)
# average = sum(numlist)/len(numlist)
# print numlist
# print average


# abc = 'with three words'
# stuff = abc.split()
# print stuff
# print len(stuff)
# print stuff[0]
# for w in stuff:
    # print w
    
# fhand = open('mbox.txt')
# for line in fhand:
    # line = line.rstrip()    
    # if not line.startswith('From '): continue
    # words = line.split()
    # email = words[1]
    # piece = email.split('@')
    # print piece[1]

# numlist = list()
# fhand = open('romeo.txt')
# for line in fhand:
    # s = len(line.split())
    # line = line.rstrip()
    # pieces = line.split()
    # while s > 0:
        # if pieces[s-1] not in numlist:
            # numlist.append(pieces[s-1])
        # s = s - 1
# numlist.sort()
# print numlist 


# inp = input("Number to compare ")
# while (inp < 100):
    # if inp > 10:
        # print ("Ole")
    # else:
        # print ("Fuck off")
    # # print ("Why is this happening?")
    # inp = input("Number to compare ")
# print "Good Buy"



    # reslt = pieces[0:]
    # numlist.append(reslt)
    # print numlist
    # final = final.rstrip()
    # peice = final.split()
    # numlist.append(final)
    # print final
    
    
# line = 'a'
# combine = 'b'
# test = line + combine
# print test


# purse = dict()
# purse['money']=12
# purse['candy']=3
# print purse



# counts = dict()
# print 'Enter a line of text'
# line = raw_input('')

# words = line.split()
# print 'Words', words

# print 'Counting'

# for word in words:
    # counts[word]= counts.get(word,0) + 1
    
# print 'Counts', counts

# numlist = list()
# fhand = open('mbox.txt')
# for line in fhand:
    # line = line.rstrip()
    # if line.startswith('From'):
        # words = line.split()
        # print line
        
# counts = dict()        
# newlist = list()    
# fhand = open('mbox.txt')
# for line in fhand:
    # line = line.rstrip()
    # if line.startswith('From '):
        # words = line.split()
    # else: 
        # continue
    # # if not line.startswith('From '): continue
    # # words = line.split()
    # email = words[1]
    # newlist.append(email)

# for x in newlist:
    # counts[x] = counts.get(x,0)+ 1
    
# bigcount = None
# bigword = None
# for y,z in counts.items():
    # if bigcount is None or z > bigcount:
        # bigword = y
        # bigcount = z
# print bigword,bigcount


# counts = dict()    
# fhand = open('romeo.txt')
# for line in fhand:
    # words = line.split()
    # for word in words:
        # counts[word] = counts.get(word,0) + 1
# lst = list()
# for key, val in counts.items():
    # lst.append((val,key))
# lst.sort(reverse=True)
# for val,key in lst[:10]:
    # print key,val

    
# counts = dict()
# newlist = list()    
# fhand = open('mbox.txt')
# for line in fhand:
    # line = line.rstrip()
    # if line.startswith('From '):
        # words = line.split()
    # else: 
        # continue
    # email = words[5]
    # piece = email.split(':')
    # newlist.append(piece[0])
    
# for hour in newlist:
    # counts[hour] = counts.get(hour,0) + 1

# lst = list()
# for x,y in counts.items():
    # lst.append((x,y))
# lst.sort(reverse=False)

# for r,t in lst:
    # print r,t
    
# hand = open('mbox.txt')
# for line in hand:
    # line = line.rstrip()
    # if line.find('From ') >=0:
        # print line   

# import re
# hand = open('mbox.txt')
# for line in hand:
    # line = line.rstrip()
    # if re.search('^X-\S+:',line):
        # print line
        
# import re
# s = 0
# numlist = list()
# numlist2 = list()
# hand = open('regex_sum_336708.txt')
# for line in hand:
    # line = line.rstrip()
    # # line = line.split()
    # y = re.findall('([0-9]+)',line)
    # if len(y) == 0: continue
    # for t in y:
        # numlist.append(t)
# print numlist        
# for z in numlist:
    # j = int(z)
    # numlist2.append(j)
    # s = j + s
# print numlist2    
# h = sum(numlist2)
# print 'Sum 1', h
# print 'Sum 2', s    

import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print tree
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')