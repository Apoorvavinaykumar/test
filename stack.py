q=[]
def stack():
  item=input("Enter the element:")
  q.append(item)
def destack():
 if not q:
  print("stack is Empty")
 else:
  item=q.pop(0)
  print("Element removed is:",item)
def display():
    if not q:
      print("stack is Empty")
    else:
      print(q)
while True:
 choice=int(input("1.Insert 2.Delete 3. Display 4. Quit Enter your choice:"))
 if choice==1:
  stack()
 elif choice==2:
  destack ()
 elif choice==3:
  display()
 else:
  break