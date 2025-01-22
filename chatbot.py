# Chat Bot
#Q1
print("This ChatBot is developed by PAWAN KUMAR of class 12-A2 session 2022-2023")
print("Hi ! Visitor","Please type hi to proceed.")
ans= input()
if ans=="hi":
 print("How may i help you")
 print("**ask me anything from bellow**")
 print("About School info , Press : 1") 
 print("About Admission Procedure , Press :2")
 print("About School Infrastructure , Press :3")
 print("About Academic , Press :4")
 print("About Latest News , Press :5")
 print("For: submit the fees, Press :6")
 print("About the documents requiered for admission, press :7")
 print("For: bye bye bro!!, Press :8")
else:
 print("Ok see you Later buddy!")
 print("Hope!""you will have query next time.")
 print("Please press 8!")
# 
qna ={
    "1":"https://apsambala.edu.in/pages.php?pageid=61",
    "2":"https://apsambala.edu.in/pages.php?pageid=91",
    "3":"https://apsambala.edu.in/pages.php?pageid=74",
    "4":"https://apsambala.edu.in/pages.php?pageid=69",
    "5": "https://www.eduindianews.com/army-public-school-ambala",
    "6": "https://www.apsdigicamps.com/",
    "7":"**FOR ARMY PERSON**:- copy of birth certificate, adhar card, part to order, adhar card of parents, marksheet of previos class, T.C. from the previos school if taken, if any diability medical certificate, passportsized photos of students                                                                                                  **FOR CIVILLIAN** :- copy of birth certificate, adhar card, adhar card of parents, marksheet of previos class, T.C. from the previos school if taken, if any diability medical certificate, passportsized photos of students",
    "":"",
    }

while True:
    question = input()
 
    if (question == "8"):
      print("Ok see you Later buddy!")

      break 
    else:
        print(qna[question])

print("Do you want to reserve a seet in advance? type(y/n)")
Pn = input()
if Pn =="y" :
  print("**Please fill the form below**")
  Name = input("please enter your name :-")
  Father_name = input("please enter your father name :-")
  Mother_name = input("please enter your mother name :-")
  Blood_group = input("please enter your blood group :-")
  Age = int(input("please enter your age :-"))
  Birth_date =input("please enter your birth date :-")
  Gender = input("please enter your gender :-")
  Category = input("please enter your category (Genral/ST/SC/OBC) :-")
  Phone_no = input("please enter your phone no. :-")
  Hobbies = input("please enter your hobbies :-")
  Achivements = input("please enter your achivements :-")
  Intrested_Sport = input("please enter your intrested sport :-")
  Adhar_card_number = input("please enter your adhar card no. :-")
  Any_Disability = input("please enter any physical/mental disability if you have :-")
  print("Welcome",Name,"!")

else :
  print ("ok see you later may you reserve seet for your child")

print("please give some review or any question to be added. ")
input()
print(" **THANK's FOR REVIEW** ")
print("please give a feedback to us by rating out of 10 : ")
input(int())
print(" **THANK's FOR RATING** ")
