# a = input()
# b = input()
# # run the membership test below
# print(b in a)

email = "My e-mail is: this@example.com"
email3 = "good.email@examplecom"
email2 = "good.email@example.com"

def check_email(string):
    dotIdx = string.rfind(".")
    atIdx = string.rfind("@")
    #  or (dotIdx < atIdx and atIdx > dotIdx+1)
    truth = (dotIdx > atIdx and dotIdx > atIdx+1)
    return ("@" in string and " " not in string and "." in string and truth)

print(check_email(email))
print(check_email(email2))
print(check_email(email3))