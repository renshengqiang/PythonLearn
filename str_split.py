import os.path
sStr1 = 'ab,cde,fgh,ijk'
sStr2 = ','
sStr1 = sStr1[sStr1.find(sStr2) + 1:]
print(sStr1)
s = 'ab,cde,fgh,ijk'
print(s.split(','))
path1='/home/tnqiangren/killer_data.ifs'
print(os.path.split(path1)[-1])
print(os.path.split(path1))
path2='killer_data.ifs'
print(os.path.split(path2)[-1])
print(os.path.split(path2))
print(os.path.split(path2)[0])
if(os.path.split(path2)[0] == ""):
	print("eq")
else:
	print("neq")
