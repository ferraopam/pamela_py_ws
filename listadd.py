lst = []
def add(ele):
    lst.append(ele)
def pop():
    if(len(lst) == 0):
        print("list empty!")
    else:
        ele = lst.pop()
        print(f"element {ele} removed")
def search(ele):
    if len(lst) == 0:
        print("List is empty")
    else:
        if ele in list:
            index = lst.index(ele)
            print(f"element {ele} is found at {index}")
        else:
            print(f"given {ele} is not found")
def display():
    pass 
while True:
    print("*****1.Add 2.Delete 3.Search 4.display 5.exit*****")
    ch = int(input("Enter the choice:"))
    if ch == 1:
        ele = int(input("Enter the element to add:"))
        add(ele)
    elif ch == 2:
        pop()
    elif ch == 3:
        ele = int(input("Enter the element to serch:"))
        search(ele)