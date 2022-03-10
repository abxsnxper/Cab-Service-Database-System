import pickle                                          #IMPORTING REQUIRED MODULES
import random




def feed(emailid):                                     #USER DEFINED FUNCTION FOR SUBMITTING FEEDBACK
    fh=open("feedback.dat","ab")
    fe={}
    fedb=input("Please enter your feedback")
    fe[emailid]=fedb
    pickle.dump(fe,fh)
    print("Thank you for submitting your valuable feedback and we look forward to review it")
    fh.close()



    

def comp(emailid):                                      #USER DEFINED FUNCTION FOR SUBMITTING COMPLAINT
    fin=open("complaint.dat","ab")
    fi={}
    compl=input("Please enter your complaint")
    fi[emailid]=compl
    pickle.dump(fi,fin)
    print("Your complaint has been successfully registered and we will review it at the earliest")
    fin.close()




    

def trip(userid):                                       #USER DEFINED FUCTION FOR SAVING TRIP INFORMATION
    pick=input("Please enter your pickup location")
    drop=input("Please enter your drop off location")
    pay=input("Please enter your payment method.\n \t\t NET BANKING \n\t\t CARD \n \t\t CASH")
    fh6=open("trip.dat","ab")
    di={}
    li=[]
    lis=[pick,drop,pay]
    li.append(lis)
    di[userid]=li
    pickle.dump(di,fh6)
    print("Thank you for riding with us. We hope you had a great experience and we look forward to you riding with us again")
    fh6.close()



    
    
    
def past(userid):                                        #USER DEFINED FUCTION FOR VIEWIN PAST TRIP INFORMATION
    fh3=open("trip.dat","rb")
    while True:
       try:
          fie=pickle.load(fh3)
       except:
          break
    lis1=fie[userid]
    for b in lis1:
        print(b)
    fh3.close()    
    
    
    
    

print("WELCOME TO GoMobility. WE HOPE TO PROVIDE YOU WITH THE BEST EXPERIENCE POSSIBLE.")               #INTRO
print("\t\t 1.USER REGISTRATION")
print("\t\t 2. USER LOGIN")
print("\t\t 3.TO PROVIDE FEEDBACK")
print("\t\t 4.TO REGISTER A COMPLAINT")
print("\t\t 5.DRIVER REGISTRATION")
print("\t\t 6.ABOUT US")
option=int(input("Please provide your option"))
while True:
    if option==1:                                       #USER REGISTRATION
        fh=open("user.dat","ab")
        user={}
        ans="Y"
        while ans in ["Y","y"]:
             name=input("Please enter your name")
             phno=int(input("Please enter your 10 digit mobile number"))
             while len(str(phno))!=10:
                 phno=int(input("Please enter a correct mobile number"))
                 continue
             age=int(input("Please enter your age"))
             if age<18:
                 print("You are below the age limit and is you will not be able to create an account")
                 break
             email=input("Please enter your email ID")
             while "@" and ".com" not in email:
                     print("You have entered an incorrect email id. Please try again")
                     email=input("Please enter your email id")
                     continue       
             coun=input("Please enter yout country of residence")
             idno=random.randint(100000,999999999)
             paw=input("Please enter a password")
             psw=input("Please enter the your password again")
             while paw!=psw:
                 print("The password you have entered is not matching")
                 psw=input("Please enter your password again")
                 continue
             user[email]=[name,phno,age,idno,coun,paw]
             pickle.dump(user,fh)
             ans=input("Continue Y/N")
             if ans in ["N","n"]:
                 print("You have been successfully registered. A confiramtion has been sent to your email id and please note your id",idno)
                 break
        fh.close()

        fin=open("user.dat","rb")
        empdct={}
        while True:
           try:
                empdct=pickle.load(fin)
           except:
                break
        print("#"*20,"DETAILS","#"*20)
        for i in empdct:
            print(empdct[i][3],"\t\t\t",empdct[i][0],"\t\t\t",empdct[i][1],"\t\t\t",empdct[i][2],"\t\t\t",i,"\t\t\t",empdct[i][4])
        fin.close()
        ans=input("Would you like to continue?Y/N")
        if ans=='Y' or ans=='y':
             print("\t\t 1.USER REGISTRATION")
             print("\t\t 2.USER LOGIN")
             print("\t\t 3.TO PROVIDE FEEDBACK")
             print("\t\t 4.TO REGISTER A COMPLAINT")
             print("\t\t 5.DRIVER REGISTRATION")
             print("\t\t 6.ABOUT US")
             option=int(input("Please provide your option"))
             continue
        else:
             break






            
    elif option==2:                                                            #USER LOGIN
        userid=input("Please enter your registered email ID")
        passw=input("Please enter your password")
        fh2=open("user.dat","rb")
        file={}
        while True:
            try:
                file=pickle.load(fh2)
            except:
                break
        a=0    
        while True:    
            if userid in file.keys():
                  if file[userid][5]==passw:
                        print("You have been succefully logged in.\n Hvae a great experience.")
                        print("\t\t\t OPTIONS")
                        print("\t 1.BOOK A TRIP")
                        print("\t 2.PAST TRIPS")
                        opt=int(input("Please select your option"))
                        while True:
                            if opt==1:
                                trip(userid)
                                break
                            elif opt==2:
                                past(userid)
                                break
                            else:
                                opt=int(input("Please enter a correct option"))
                                continue
                        log=input("Do you wish to log out of your account? Y/N")
                        if log=="Y" or log=="y":
                            fh2.close()
                            print("Thank you for using our service. We hope you had a great experience")
                            break
                  else:
                        print("You have entered an incorrect password. You will have a maximum of 5 attempts.")
                        a+=1
                        if a==5:
                            break
                        else:
                            passw=input("Please enter the correct password")
                            continue
            else:
                  print("This account does not exist.Y")
                  userid=input("Please enter the correct email ID")
                  continue
                  
                
                      
                 
                        
    

        
    elif option==3:                                  #FEEDBACK SECTION
        emailid=input("Please enter your emailid")
        feed(emailid)


        
    elif option==4:                                   #COMPLAINT SECTION
        emailid=input("Please enter your emailid")
        comp(emailid)


        
    elif option==5:                                   #DRIVER REGISTRATION
        fh=open("driver.dat","ab")
        dri={}
        ans=input("Y/N")
        while ans in ['Y','y']:
             name=input("Please enter your name")
             phno=input("Please enter your phone number")
             vehi=input("Enter your vehicle name")
             vehino=input("Please enter your vehicle registration number")
             age=input("Enter your age")
             gender=input("M/F")
             loc=input("Enter your locality")
             idno=str(random.randint(10000000,99999999))
             dri[idno]=[name,phno,vehi,vehino,age,gender,loc]
             pickle.dump(dri,fh)
             ans=input("Continue Y/N")
             if ans=="N" or ans=="n":
                   print("You have been successfully registered.Please note your identification number is",idno)
                   break
                   fh.close()

        fh1=open("driver.dat","rb")
        empdct={}
        while True:
             try:
                   empdct=pickle.load(fh1)
             except:
                   break
        print("#"*30,"Details","#"*30)
        print('IDNO','Name','Phone','Vehicle','VehiNo','age','gender','Locality',sep="\t\t\t")
        for i in empdct.keys():
             print(i,"   ",empdct[i][0],empdct[i][1],empdct[i][2],empdct[i][3],empdct[i][4],empdct[i][5],empdct[i][6],sep="\t\t")
        fh1.close()




        
    elif option==6:                                         #ABOUT US SECTION
        print('''GoMobility was started in 2012 with the ambition of making every ride the best ever for the consumer.\n
              Our mission statement is 'To improve people's lives with the world's best transportation. '\n
              And one of Lyft's “big picture visions” is to reinvent cities “around people instead of cars,\n
              and replace parking lots with green spaces and parks.”\n
              Lyft is committed to effecting positive change for our cities by offsetting carbon emissions from all rides,\n
              and by promoting transportation equity through shared rides,\n
              bikeshare systems, electric scooters, and public transit partnership.''')
        break





        
    
                     

