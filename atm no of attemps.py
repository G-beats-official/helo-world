t=0
while t<1:
  print("welcome to sbi atm")
  a=3
  while a<5:
    x=int(input("enter the pin:"))
    if(x==1234):
      print("press 1 for cardless transcation")
      y=int(input("enter the number:"))
      if(y==1):
        kk=1
      while kk<3:
        print("enter acc number:")
        g=int(input("enter acc number:"))
        a=len(str(g))
        if(a!=10):
            print("try again")
            kk=kk+1
            continue
        if(a==10):
           print("correct")
           t=2
           break
   
      

        
      
    else:  
      print("you have enter the wrong option please try again")
      a=a-1
    if(a==2):
      print("2 attemps left")
    if(a==1):
      print("1 attemps left")
    if(a==0):
      print("to many attemps start from begining thank you ")
      break

  break
    
