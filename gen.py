#!/usr/bin/env python3
import os

print("begin = ",end='')
begin = int(input())
print("end = ",end='')
end = int(input())

for i in range(begin,end+1):
	d = '{}/{}'.format(i//10000,i//100)
	os.makedirs(d, exist_ok=True)
	f = open('{}/{}/{}.md'.format(i//10000,i//100,i), 'w', encoding='utf-8')
	s = """# ギター練習日記

[Top](../README.md)  
[{year} 年 {month} 月](./{year}{month:02}.md)

## {month}/{day}  

""".format(year=i//10000,month=i//100%100,day=i%100)
	f.write(s)
	f.close()

f = open('{0}/{1}/{1}.md'.format(i//10000,i//100),'w', encoding='utf-8')
s = """# ギター練習日記

[Top](../../README.md)

"""
for i in range(begin,end+1):
	s += "[{}年{}月{}日](./{}.md)\n".format(i//10000,i//100%100,i%100,i)

f.write(s)
f.close()


