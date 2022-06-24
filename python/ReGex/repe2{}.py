import re 
haRegex = re.compile(r'(Ha){3}')
mo1=haRegex.search('HaHa')==None
print(mo1)