#Samantha Stinson
#MAy 4,2015
#Mr.Cardinale

#Exam Project-Part 2
#Medical File Search Program

#lists for the patients info
patient=['Choal','Emma','Timothy','Maddie']
lastname=['Riggens','Smith','Sanders','Everstone']
birthdate=['02/03/1997','15/12/2002','24/08/2011','06/10/2009']
age=[18,12,3,5]
height=['147.5 inches','59.0 inches','37.5 inches','39.5 inches']
weight=['147.5 pounds', '91.5 pounds','31.0 pounds','42.5 pounds']
blood=['O-','A-','B+','AB+']
pressure=['120/85 mmHg','126/82 mmHg','80/34 mmHg','88/47 mmHg']
eyes=['20/30','20/35','20/20','20/20']
shots=[61,57,32,43]
ph=['chicken pox, broken leg,','fractured ankle, broken arm, mono. ','fever','strep throat']
fh=['father has Herpes gene','grandfather had the Autism gene','mother had diabetes','grandmother had breast cancer']

#function:edit
#@param:
#@return:
def edit():
    print "\nYou choose to edit the medical files.\n"
    state=False
    while state==False:
        print "Here are the patients on file:",patient
        files=raw_input("Please enter the name of the patient who's file you want to edit. \n(With the first letter capititalized)\n: ")
        if files in patient:
            state=True
            person=patient.index(files)
        else:
            print "\nThat name is not on the files.\n Please enter another name.\n"
            state=False
        
        #THOUGHT PROCESS
        
        #thought that I could use the length then a range loop to see if the value is at any index point in the list
        
        #length=len(patient)-1
        #no=length
        #for count in range(0,length):
        #    if files==patient[no]:
        #        person=patient.index(name)
        #        state=True
        #        no=length-1
        #    else:
        #        print "\nThat name is not on file.\nPlease enter another name.\n\n"
        #        state=False
        
        #this one still works, but I wanted to make a version that could include newer files as well
        
        #if files=='Choal' or 'choal':
        #    person=0
        #    state=True
        #elif files=='Emma' or 'emma':
        #    state=True
        #    person=1
        #elif files=='Timothy' or 'timothy':
        #    state=True
        #    person=2
        #elif files=='Maddie' or 'maddie':
        #    person=3
        #    state=True
        #if patient.index(files)>=0:
        #    person=patient.index(files)
        #    state=True
        #else:
        #    print "That name is not on the files.\n Please enter another name."
        #    state=False

    states=False
    while states==False:
        option=raw_input("\nPlease enter what you would like to edit on this patients file.\n(i.e last name, age, birthdate, blood type, height, weight, blood pressure,\neyesight, shots, previous history, family history)\n:")
        if option=='last name' or option=='Last Name' or option=='Last name':
            print "\nHere is the old files record of their last name:",lastname[person]
            edit=raw_input("Please enter the edit for their last name:")
            lastname[person]=edit
            states=True
        elif option=='height' or option=='Height':
            print "\nHere is the old files record of their height:", height[person]
            edit=raw_input("Please enter the edit of their height in inches:")
            height[person]=edit
            states=True
        elif option=='birthdate' or option=='Birthdate':
            print "\nHere is the old files record of their birthdate:", birthdate[person]
            edit=raw_input("Please enter the edit for their birthdate in day/month/year:")
            birthdate[person]=edit
            states=True
        elif option=='age' or option=='Age':
            print "\nHere is the old files record of their age:", age[person]
            edit=input("Please enter the edit for their age:")
            age[person]=edit
            states=True
        elif option=='weight' or option=='Weight':
            print "\nHere is the old files record of their weight:", weight[person]
            edit=raw_input("Please enter the edit for their weight:")
            weight[person]=edit
            states=True
        elif option=='blood pressure' or option=='Blood Pressure' or option=='Blood pressure':
            print "\nHere is the old files record of their blood pressure(systolic BP over Diastolic BP):", pressure[person]
            edit=raw_input("Please enter the edit for their blood pressure in systolic BP over Diastolic BP in mmHg:")
            pressure[person]=edit
            states=True
        elif option=='blood type' or option=='Blood Type' or option=='Blood Type':
            print "\nHere is the old files record of their blood type:", blood[person]
            edit=raw_input("Please enter the edit for their blood type:")
            blood[person]=edit
            states=True
        elif option=='eye sight' or option=='Eye Sight' or option=='Eye sight':
            print "\nHere is the old files record of their eye sight:", eyes[person]
            edit=raw_input("Please enter the edit for their eye sight:")
            eyes[person]=edit
            states=True
        elif option=='shots' or option=='Shots':
            print "\nHere is the old files record of their shot count:", shots[person]
            edit=raw_input("Please enter the edit for their shot count:")
            shots[person]=edit
            states=True
        elif option=='previous history' or option=='Previous History' or option=='Previous history':
            print "\nHere is the old files record of their previous history:", ph[person]
            edit=raw_input("Please enter the edit for their previous medical history\n(retype the other info if wanted to refer to as well in the future):")
            ph[person]=edit
            states=True
        elif option=='family history' or option=='Family History' or option=='Family history':
            print "\nHere is the old files record of their family history:", fh[person]
            edit=raw_input("Please enter the edit for their family history (retype the other info if wanted to refer to as well in the future):")
            fh[person]=edit
            states=True
        else:
            print "That is not an option, please try again."
            states=False

#function:new
#@param: 
#@return:
def new():
    print "\nYou choose to make a new medical file.\n\nPlease input the following medical information of your new patient..."
    state=False
    while state==False:
        name=raw_input("Please enter their first name(With the first letter capitialized):")
        patient.append(name)
        last=raw_input("Please enter their last name(With the first letter capitalized):")
        lastname.append(last)
        bday=raw_input("Please enter their birthdate (Day/Month/Year):")
        birthdate.append(bday)
        old=input("Please enter their age:")
        age.append(old)
        mass=raw_input("Please enter their weight (pounds):")
        weight.append(mass)
        tall=raw_input("Please enter their height (inches):")
        height.append(tall)
        b=raw_input("Please enter their blood type:")
        blood.append(b)
        press=raw_input("Please enter their blood pressure:")
        pressure.append(press)
        sight=raw_input("Please enter their eyesight (20/__):")
        eyes.append(sight)
        shot=input("Please enter the amount of required shots they have recived:")
        shots.append(shot)
        previous=raw_input("Please enter all previous medical history:")
        ph.append(previous)
        family=raw_input("Please enter any notable family medical history:")
        fh.append(family)
        state=True
 
#function:search
#@param:
#@return: 
def search():
    print "\nYou choose to search the medical files."
    state=False
    while state==False:
        print "\nHere are the patients on file:", patient
        name=raw_input("Please enter the first name of the patient \n(With their first letter captitalized )\n:")
        
        if name in patient:
            state=True
        else:
            print "\nThat name is not on the files.\n Please enter another name."
            state=False
        person=patient.index(name)
 
    print "\n", patient[person],lastname[person],"'s file"
    print "\nfirst name:",patient[person]
    print "last name:", lastname[person]
    print "birthdate:", birthdate[person]
    print "age:", age[person]
    print "height:", height[person]
    print "weight:", weight[person]
    print "blood type:", blood[person]
    print "blood pressure(systolic BP over Diastolic BP):", pressure[person]
    print "eye sight:", eyes[person]
    print "shot count:", shots[person]
    print "previous history:", ph[person]
    print "family history:", fh[person]

#function:instruction
#@param:
#@return: choice(string)
def instructions():
    choice=raw_input("\nWould you like to edit, search, make a new file, or exit?\n(please type your choice: \"edit\",\"search\",\"new\", or \"exit\")\n:")
    return choice

#function:main
#@param:
#@return: 
def main():
    print "                                  MedFi"
    print "\nHello Doctor, I am  MedFi, I contain all of your patients medical files. \nI care, because you care. \nYou can edit your patients files with me, create a new patient file with me \nor search for your patients files with me.\nI want to help.\nEnter the patients first name to look them up...\nI can show you your patients; last name, age, blood type, height, weight, blood pressure, health issues and if there are any recent health problems."
    
    begin=False
    while begin==False:
        choice=instructions()
        if choice=="new" or choice=="new file" or choice=="New":
            new()
            begin=False
        elif choice=="search" or choice=="search file" or choice=="Search":
            search()
            begin=False
        elif choice=="edit" or choice=="edit file" or choice=="Edit" :
            edit()
            begin=False
        elif choice=="exit" or choice=="exit program" or choice=="Exit":
            print "\n\nThank you for using MedFi!\n\n\nPROGRAM IS DONE"
            begin=True

    
main()
