#creating a dictionary which is a key vale pair
student= {"Name": "Taarush", "Age": 12 , "Country": "UK", "Year": "IFA"}
print(student)
print (student ['Country'])
print (student['Name'])
print (student['Age'])
print (student['Year'])
#adding new element to the dictionary
student["height"]=155
print (student)
student["hobbies"]="cricket","art","video games"
print (student)
student["favourite colour"]="blue"
print (student)
print (student.keys())
print (student.values())
#find the number of elements/size of the dictionary
print (len(student))
#check if name exists in dictionary
print ("hobbies" in student) 
print ("favourite food" in student)


