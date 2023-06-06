email= "ali@outlook.com"
# email= "hasnat123@gmail.com"

# Using built-in methods
# username=email.split('@')[0]
# domain=email.split('@')[1]
# domain_extention=email.split('.')[1]
# print(username, domain, domain_extention)

# Using while loop
# i=0
# username=[]
# domain=[]
# domain_extension=[]
# breakpoints=[]
# while i < len(email):
#     if '@' not in breakpoints:
#         username.append(email[i])
#     else:
#         domain.append(email[i])
#     if '.' in breakpoints:
#         domain_extension.append(email[i])    
#     if email[i] == '@' or email[i] == '.':
#         breakpoints.append(email[i])
#     i+=1
# else:
#     username =''.join(username)[:-1:]
#     domain = ''.join(domain)
#     domain_extension = ''.join(domain_extension)
# print(username, domain, domain_extension)

# Using for loop
# username=[]
# domain=[]
# domain_extension=[]
# breakpoints=[]
# for item in email:
#     if '@' not in breakpoints:
#         username.append(item)
#     else:
#         domain.append(item)
#     if '.' in breakpoints:
#         domain_extension.append(item)
#     if item == '@' or item == '.':
#         breakpoints.append(item)
# username=''.join(username)[:-1:]
# domain=''.join(domain)
# domain_extension=''.join(domain_extension)
# print(username, domain, domain_extension)

breakpoints=[]
username=domain=domain_extension=''
for item in email:
    if '.' in breakpoints:
        domain_extension+=item
    if '@' in breakpoints:
        domain+=item
    if item == '@' or item == '.':
        breakpoints.append(item)
    if '@' not in breakpoints:
        username+=item
print(username, domain, domain_extension)

# Using user-defined function
# def email_parser(email):
#     username=[]
#     domain=[]
#     domain_extension=[]
#     breakpoints=[]
#     for item in email:
#         if '@' not in breakpoints:
#             username.append(item)
#         else:
#             domain.append(item)
#         if '.' in breakpoints:
#             domain_extension.append(item)
#         if item == '@' or item == '.':
#             breakpoints.append(item)
#     username=''.join(username)[:-1:]
#     domain=''.join(domain)
#     domain_extension=''.join(domain_extension)
#     return username, domain, domain_extension

# username,domain, domain_extension = email_parser('ali@outlook.com')
# print(username,domain,domain_extension)