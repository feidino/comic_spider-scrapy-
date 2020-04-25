import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for num in range(35):
    with open (r'E:\vscode 文件\作业\测验试卷\capitaltest %d.txt'%(num+1),'w',encoding='utf-8') as testfile:
        testfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        testfile.write((' ' * 20) + 'State Capitals Quiz (Form %d)' % (num + 1))
        testfile.write('\n\n')
    answerfile = open (r'E:\vscode 文件\作业\测验试卷\capitaltest %d.txt'%(num+1),'a',encoding='utf-8')
    states = list(capitals.keys())
    random.shuffle(states)
    qn = 0
    for state in states:
        qn += 1
        citys = list(capitals.values())
        del citys[citys.index(capitals[state])]
        random.shuffle(citys)
        cap_city = [capitals[state],citys[0],citys[1],citys[2]]
        random.shuffle(cap_city)
        answerfile.write('%d、%s 的首府是：\n\nA、%s  B、%s  C、%s  D、%s\n\n'%(qn,state,cap_city[0],cap_city[1],cap_city[2],cap_city[3]))




