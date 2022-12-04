input = open('day-4.input', 'r').readlines()

#####################
##  Start of Code  ##
#####################

p=0
for l in input:
  a,b=[tuple(map(int,x.split('-')))for x in l.split(',')]
  if a[0]<=b[0]<=a[1]or b[0]<=a[0]<=b[1]:p+=1
print(p)

################
##  Part Two  ##
################

p=0
for l in input:
  a,b=[tuple(map(int,x.split('-')))for x in l.split(',')];p+=(a[1]>=b[0]and a[0]<=b[1])
print(p)
