employees = [
{
'fname':'Nitish',
'lname':'Singh',
'age' : 33,
'grade':'skilled'
},
{
'fname':'Ankit',
'lname':'Verma',
'age' : 34,
'grade':'semi-skilled'
},
{
'fname':'Neha',
'lname':'Singh',
'age' : 35,
'grade':'highly-skilled'
},
{
'fname':'Anurag',
'lname':'Kumar',
'age' : 30,
'grade':'skilled'
},
{
'fname':'Abhinav',
'lname':'Sharma',
'age' : 37,
'grade':'highly-skilled'
}
]

print(list(map(lambda j:j['fname']+' '+j['lname'],(list(filter(lambda i:i['grade']=='highly-skilled', employees))))))