email= "ali@outlook.com"
# email= "hasnat123@gmail.com"

# Using built-in methods
# username=email.split('@')[0]
# domain=email.split('@')[1]
# domain_extention=email.split('.')[1]
# print(username, domain, domain_extention)

# Using while loop
# i=0
# breakpoints=[]
# username=domain=domain_extension=''
# while i < len(email):
#     if '.' in breakpoints:
#         domain_extension+=email[i]
#     if '@' in breakpoints:
#         domain+=email[i]
#     if email[i] == '@' or email[i] == '.':
#         breakpoints.append(email[i])
#     if '@' not in breakpoints:
#         username+=email[i]
#     i+=1
# print(username, domain, domain_extension)

# Using for loop

# breakpoints=[]
# username=domain=domain_extension=''
# for item in email:
#     if '.' in breakpoints:
#         domain_extension+=item
#     if '@' in breakpoints:
#         domain+=item
#     if item == '@' or item == '.':
#         breakpoints.append(item)
#     if '@' not in breakpoints:
#         username+=item
# print(username, domain, domain_extension)

# Using user-defined function
# def email_parser(email):
#     username=domain=domain_extension=''
#     breakpoints=[]
#     for item in email:
#         if '.' in breakpoints:
#             domain_extension+=item
#         if '@' in breakpoints:
#             domain+=item
#         if item == '@' or item == '.':
#             breakpoints.append(item)
#         if '@' not in breakpoints:
#             username+=item
#     return username, domain, domain_extension

# username,domain, domain_extension = email_parser('ali@outlook.com')
# print(username,domain,domain_extension)