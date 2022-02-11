import urllib.request
url = "https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt"
file = urllib.request.urlopen(url)

data = file.readlines()
print(len(data))
#for item in data:
 # item = item.decode()

for i in range(len(data)):
  data[i] = str(data[i], "utf-8").strip()
  #print(len(data[i]))
  
  #green = [] * 5  #has confirmed value/places
present = []   #has confirmed values
yellow = [[] for i in range(5)] #initializes five lists.  Each of these specifies the letters that Can't be in that space.
green = []
gray = [] #has nonexistent values
greenReject = 0
grayReject = 0
yellowReject = 0 
presentReject = 0

green = ['','l','','','']
present.extend(['c'])
gray.extend(['o','g','s'])
yellow = [['c'],[],[],['c'],[]]

for j in range(len(data)):
  good = True
  if good: 
    for i in [0,1,2,3,4]:         #checks to see if an item is in green, if it isn't, 
      if (green[i] != '' and data[j][i] != green[i]):
        #print(str(data[j][i]) + "  " + str(green[i]))
        greenReject +=1 
        data[j] = ''
        good = False
        break
  if good:
    for i in [0,1,2,3,4]:
      if data[j][i] in yellow[i]:
        #print(data[j])
        yellowReject += 1
        data[j] = ''
        good = False
        break
  if (good and len(present) != 0):
    for i in range(len(present)):
      if present[i] not in data[j]: #this operation only works letter by letter
        presentReject += 1
        data[j] = ''
        good = False
        break
  if good:
    for i in [0,1,2,3,4]:
      if data[j][i] in gray:
        grayReject += 1
        data[j] = ''
        good = False
        break

print(greenReject)
print(grayReject)
print(yellowReject)
print(presentReject)
newList = [i for i in data if i]
print(len(newList))
print(newList)
