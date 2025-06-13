total_records=int(input('Enter No of records- '))
students=[]
for i in range(total_records):
    print(f'Enter Details of student-{i+1}')
    name=input('Enter Student name-')
    hi_ed=input('Enter Higher Education-')
    skill=input('Enter Primary Skill-')
    year=input('Enter Year of Graduation-')
    students.append((name,hi_ed,skill,year))

print('\n\nEnter Job Role Requirement')
j_skill=input('Enter Skill-')
j_hi_ed=input('Enter Higher Education-')
j_year=input('Enter Year of Graduation-')

output=[]
for i in range(len(students)):
    if(students[i][1].upper()==j_hi_ed.upper() and students[i][2].upper()==j_skill.upper() and students[i][3].upper()==j_year.upper()):
        output.append(students[i])

if output:
    print('\nMatched-Candidates')
    for i in output:
        print(i)
else:
    print('\nNo such candidate')