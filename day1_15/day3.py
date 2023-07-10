#day3:分支结构
#Conversion of cm and inch
"""
l = int(input('please enter the length '))
u = str(input('please enter the unit, cm/inch '))
if u == 'cm':
    print('{}cm is converted {:.2f}inch'.format(l, l/2.54))
elif u == 'inch':
    print('{}inch is converted to {:.2f}cm'.format(l, l*2.54))
else:
    print('Please follow the rule, enter the correct unit')
"""

#Conversion of score
"""
ss = int(input('please enter the score'))
if ss >= 90:
    grade = 'A'
elif ss >= 80:
    grade = 'B'
elif ss >= 70:
    grade = 'C'
elif ss >= 60:
    grade = 'D'
else:
    grade = 'E'
print("the grade is {}".format(grade))
"""

#triangle
l1 = int(input('please enter the first length of the triangle '))
l2 = int(input('please enter the second length '))
l3 = int(input('please enter the third length '))
if l1+l2 > l3 and l1+l3 > l2 and l2+l3 > l1:
    l = l1+l2+l3
    p = 0.5*l
    s = math.sqrt(p*(p-l1)*(p-l2)*(p-l3))
else:
    print("this isn\'t a triangle")
print('The circumference is %d and the area is %.2f' % (l,s))
