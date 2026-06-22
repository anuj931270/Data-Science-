#  Create Your Own KBC Game
points=0
attempt=0
print('''
Q1.WHO IS THE INVENTOR OF COMPUTER?
      a.xyx
      b.x
      c.y
      d.charles babage
      ''')
choice=input("Do you want to attempt : (yes/no)").strip
if choice == "yes":
     attempt+=1
     opt=input("Enter your choice . (a/b/c/d)")
     if opt=="d":
        print("Correct")
        points=points+1000
     else:
        print("Wrong")
else:
    print("Best of luck....!")
    print('''
Q2.WHO IS THE INVENTOR OF COMPUTER?
      a.xyx
      b.x
      c.y
      d.charles babage
      ''')
choice=input("Do you want to attempt : (yes/no)").strip
if choice == "yes":
     attempt+=1
     opt=input("Enter your choice . (a/b/c/d)")
     if opt=="d":
        print("Correct")
        points=points+2000
     else:
        print("Wrong")
else:
    print("Best of luck....!")
print(points)
print(attempt)
    
