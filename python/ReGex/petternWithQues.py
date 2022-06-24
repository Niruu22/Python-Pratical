import re 
QuesReg = re.compile(r'bat(wo)?man')
mo=QuesReg.search('Ronny is a batman  ')
print(mo.group())