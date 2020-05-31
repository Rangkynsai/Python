#get() method which hold two argument key and a fallback
picnic = {'apples':5,'cups':2}
print("I am bringing"+str(picnic.get('cups',0))+'cups')
print('I am bringing'+str(picnic.get('egg',0))+'egg')