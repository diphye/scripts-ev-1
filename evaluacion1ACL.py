aclNum = int(input("Cual es el número IPV4 ACL?"))
if aclNum >=1 and aclNum <=99:
    print("Este es una ACL IPV4 estandar.")
elif aclNum >=100 and aclNum <= 199:
    print("Este es una ACL IPV4 extendida")
else:
    print("Eta es una ACL IPV4 no es una ACL extendida o estandar.")
