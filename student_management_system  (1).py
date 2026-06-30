
import json, os

FILE="students.json"

def load():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=2)

def grade(m):
    return "A" if m>=90 else "B" if m>=75 else "C" if m>=60 else "D" if m>=40 else "F"

def add(data):
    r=input("Roll: ")
    if any(s["roll"]==r for s in data):
        print("Roll exists"); return
    n=input("Name: ")
    m=float(input("Marks: "))
    data.append({"roll":r,"name":n,"marks":m,"grade":grade(m)})
    save(data)

def view(data):
    if not data:
        print("No records"); return
    print("-"*40)
    for s in data:
        print(s["roll"], s["name"], s["marks"], s["grade"])

def search(data):
    r=input("Roll: ")
    for s in data:
        if s["roll"]==r:
            print(s); return
    print("Not found")

def update(data):
    r=input("Roll: ")
    for s in data:
        if s["roll"]==r:
            s["name"]=input("New name: ")
            s["marks"]=float(input("New marks: "))
            s["grade"]=grade(s["marks"])
            save(data); return
    print("Not found")

def delete(data):
    r=input("Roll: ")
    for i,s in enumerate(data):
        if s["roll"]==r:
            data.pop(i); save(data); print("Deleted"); return
    print("Not found")

def main():
    data=load()
    while True:
        print("\n1.Add\n2.View\n3.Search\n4.Update\n5.Delete\n6.Exit")
        ch=input("Choice: ")
        if ch=="1": add(data)
        elif ch=="2": view(data)
        elif ch=="3": search(data)
        elif ch=="4": update(data)
        elif ch=="5": delete(data)
        elif ch=="6": break
        else: print("Invalid")
if __name__=="__main__":
    main()
