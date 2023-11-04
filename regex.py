# import re
# s="pet:cat i love cats"
# m=re.match(r"pet:\w\w\w",s)
# print(m.group(0))
# if m:
#     print("match")
# else:
#     print("no match")

# import re
# s="john@abc.com and mike@pqr.com"
# o=re.sub(r"@[a-z]+","@gmail",s)
# print(o)

# import re
# s="python is a programming language"
# o=re.split(r"\s",s)
# print(o)

# import re
# p=input("enter password")
# o=re.search(r"[A-Z]*[a-z]*[@$]?[0-9]+",p)
# if o:
#     print("valid")
# else:
#     print("invalid")

import re
e=input("enter email")
g=re.search(r"[a-z]+[0-9]*[@][a-z]+[.][a-z]{2,3}",e)
if g:
    print("valid")
else:
    print("invalid")