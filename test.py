from grail import *

# Python dictionary is considered a hashmap has avarage time complexity of 
# 0(1) or worst case of 0(n)
info = {'TK1':{'Name': 'Vagif',
        'Date of Birth':'12/02/1992',
        'Phone Number':8249293,
        'Address': '12 Apple street'},
        'TK2':{'Name': 'Aliyev',
        'Date of Birth':'13/03/1993',
        'Phone Number':7243952,
        'Address': '12 Pear street'},}

def main():
    print(info)
    # ref = input("Enter reference number: ") 
    ref = "TK2"
    # sec = input("Enter section name: ") 
    sec = "Name"

    add(info,ref,sec)
    retrive(info,ref)
    update(info,ref,sec)
    retrive(info,ref)
    remove(info,ref,sec)
    retrive(info,ref)

if __name__ == "__main__":
    main()