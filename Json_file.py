def readi():
	#importing json
import json
number = [1,2,3,4,5,6,7,8]
file_name = 'number.json'#creating a file
with open(file_name,'w') as file_obj:
	json.dump(number,file_obj)#store the info into a file
