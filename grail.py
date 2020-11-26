#check if Reference number and The section requested exist
def verify(info,ref,sec):
    ref_check = True
    sec_check = True
    if info.get(ref) is None:        
        ref_check = False
        print("Reference | "+ str(ref) +" | does not exist.")
    elif info[ref].get(sec) is None:
        sec_check = False
        print("Section | "+ str(sec) +" | does not exist.")
    return sec_check,ref_check

# Add
def add(info,ref,sec):
    verify(info,ref,sec)
    if  all(verify(info,ref,sec)):
        default = info[ref][sec]
        dir = input("Add to " + str(default)+ "->")
        info[ref][sec] = str(default)+dir
        print("Changed to: "+info[ref][sec])
    return

# Update
def update(info,ref,sec):
    if  all(verify(info,ref,sec)):
        default = info[ref][sec]
        dir = input("Update " + str(default)+ "->")
        info[ref][sec] = dir
        print("Updated to: "+info[ref][sec])
    return

# Remove
def remove(info,ref,sec):
    if  all(verify(info,ref,sec)):
        print("Removed: "+info[ref][sec])
        info[ref][sec] = None
    return

# Retrive
def retrive(info,ref):
    if info.get(ref) is not None: 
        print("Retrived: "+str(info[ref]))
        return info[ref]
    return
