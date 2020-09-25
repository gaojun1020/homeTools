from prettyTime import pretty_time_delta
from mathLib import Question

test = []

q1 = Question(1, 2, 'ADD')
q2 = Question(1, 3, 'ADD')
q3 = Question(1, 4, 'ADD')
q4 = Question(1, 5, 'ADD')
q5 = Question(2, 3, 'ADD')

test.append(q1)
test.append(q2)
test.append(q3)
test.append(q4)

print(q5 in test)