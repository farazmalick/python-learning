"""
temp=[1.1,2.2,3.3,4.4]
for t in temp:
    print(round(t))

for letter in "ali":
    print(letter.upper())

dic={"a":1,"b":2}

for d in dic.items():
    print(d)
for d in dic.keys():
    print(d)
for d in dic.values():
    print(d)


name=""
while name!="pypy":
    name=input("enter string: ")
"""
"""
def sent_maker(p):
    data=("how","when","where","why","what")
    cap_phrase=p.capitalize()
    if p.startswith(data):
        return "{}?".format(cap_phrase)
    else:
        return "{}.".format(cap_phrase)

result=[]

while True:
    user_input=input("enter phrase: ")
    if user_input=="\end":
        break
    else:
        phrase=sent_maker(user_input)
        result.append(phrase)

for phrase in result:
    print(phrase)
"""