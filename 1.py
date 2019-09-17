# -*- coding: UTF-8 -*- 

#李四,福建省福州13756899511市鼓楼区鼓西街道湖滨路110号湖滨大厦一层.

import re
import json

###数据
userInput=input()


area1=['省',"(市|自治州)",'(县|区|市)','(镇|街道|乡)',]
area2=['省','(市|自治州)','(县|区|市)','(镇|街道|乡)','(街|路|巷)','号',]
output={
    "姓名":"",
    "手机":"",
    "地址":[]
}

#r'\w+?市|自治州'
output['姓名']=re.search(r'\d!(.*),',userInput).group(1)
output['手机']=re.search(r'\d{11}',userInput).group()
rank=userInput[0]#难度级别
area=locals()['area'+rank]#area1或area2
address=re.sub(r'\d{11}','',userInput).split(',')[1].strip('[.]')#完整地址

for index in range(len(area)):
    result=re.search(r'\w+?'+area[index],address)
    if result:
        address=re.sub(result.group(),'',address)
        print(address)
        output['地址'].append(result.group())
    else:
        output['地址'].append('')
output['地址'].append(address)
print(output)