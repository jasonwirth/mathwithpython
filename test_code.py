# Sample Code


#-----------
def toss_till_value(value, sides):
    tosses = []
    while 1:
        face = random.choice(sides)
        tosses.append(face)
        if face == value:
            break
    return len(tosses)

#-----------

value = 2
#sides = [1, 2, 3, 4, 5, 6]
sides = [1, 1, 1, 1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9, 10]
trials = 100000
results = []
for i in range(trials):
    count = toss_till_value(value, sides)
    results.append(count)
    
print "Average number of tosses:", sum(results) / float(trials)
print "Occurances:", sides.count(value)
print "Number of sides:", len(sides)
print float(len(sides)) / sides.count(value)


#=======================
# CSS SNIPPET NEEDED TO FIX HTML NOTEBOOKS
#=======================

# div.code_cell pre {
# 	padding-top: 0px;
# 	padding-bottom: 0px;
# 	margin-top: 0px;
# 	margin-bottom: 0px;
# }