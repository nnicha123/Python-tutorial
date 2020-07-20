# name = input()
# def hello(strInput):
#     return "Hello, world! Hello, " + strInput
# print(hello(name))

def mi_to_km(numMiles):
    return numMiles*1.609

print(mi_to_km(100))
print(mi_to_km(14))

def code(language="Python"):
    return "We code in" + language
print(code())

def create_url(host="localhost",port=443):
    return "https://" + host + ":" + str(port)
print(create_url())