"""
def mean(myList):
  #  if type(myList)==dict:
    if isinstance(myList,dict):
      result=sum(myList.values())/len(myList)
    else:
      result=sum(myList)/len(myList)
    return result

myList=[1,2,3]
myDict={"a":1,"b":2,"c":3}
print(int(mean(myList)))
print(int(mean(myDict)))
"""
"""
def weather(temp):
    if temp > 15:
        return "hot"
    else:
        return "cold"

temp=int(input("Enter Temprature:")) 

print(weather(temp))

#default value
def weather(temp=3):
    if temp > 15:
        return "hot"
    else:
        return "cold"

temp=int(input("Enter Temprature:")) 
print(weather())

def cel_to_fahr(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
print(cel_to_fahr(30))
"""

"""
name=input("enter name: ")
#py 2,3.1,.2,.3
message="hello %s!" %name
#py>=v 3.6
message2=f"hello {name}!"
print(message,message2)
"""
"""
fname=input("enter firstname: ")
lname=input("enter lastname: ")
#py 2,3.1,.2,.3
message="hello %s %s!" %(fname,lname)
#py>=v 3.6
message2=f"hello {fname} {lname}!"
print(message,message2)
"""

