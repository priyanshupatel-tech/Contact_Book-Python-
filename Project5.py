import json
contact=[]
def save_data(contact):
    with open("contact.json","w") as file:
        json.dump(contact,file,indent=4)

def load_data():
    try:
        with open("contact.json","r") as file:
            return json.load(file)
    except:
        return []
    
def menu():
    print("===============Menu===============")
    print("1.Add Contact \n2.View Contact \n3.Search Contact \n4.Update Contact \n5.Delete Contact \n6.Exit")

def add_contact():
    contact=load_data()
    name1=input("Enter Name=").strip()
    name=name1.title()
    for check in contact:
        if check["Name"]==name:
            return print("Name Allready Saved in  Contact Book")
    else:         
        phone=int(input("Enter Mobile Number="))
        email=input("Enter Email ID=").strip()
        contact.append(
            {
            "Name":name,
            "Phone":phone,
            "Email":email
        }
        )
        save_data(contact)
        print("Contact Added!")
        return contact

def view_contact():
    contact=load_data()
    print(f"{'Name':<30}{'Phone':<25}{'Email ID'}")
    print("-"*70)
    for contacts in contact:
        print(f"{contacts['Name']:<30}{contacts['Phone']:<25}{contacts['Email']}")

def search_contact():
    contact=load_data()
    search1=input("Enter Name=")
    search=search1.title()
    for searches in contact:
        if searches['Name']==search:
            return print(f" Contact Found!\n{searches}") 
    else:
        print("Contact Not Found!")

def update_contact():
    contact=load_data()
    name1=input("Enter Name=")
    name=name1.title()
    found=False
    for item in contact:
        if item['Name']==name:
            found=True
            print("What do you want to update \n1.Name\n2.Phone\n3.Email")
            try:
               update=int(input("Enter choice="))
            except:
                print("Invalid Input!")
            if update==1:
                new_name=input("Enter New Name=").title()
                item['Name']=new_name
            elif update==2:
                new_phone=int(input("Enter new phone number="))
                item['Phone']=new_phone
            elif update==3:
                new_email=input("Enter new Email ID=").strip()
                item['Email']=new_email
            else:
                print("Please give correct input!")
            print("Contact Update")
            break
    if not found:
        print("Name not Found in Conatct Book")
    save_data(contact)
    
def delete_contact():
    contact=load_data()
    name=input("Enter contact Name you want to delete= ").title()
    for contacts in contact:
        if contacts['Name']==name:
            contact.remove(contacts)
            print("Contact Deleted Successfully!")
            break
    save_data(contact)
    


print("==============Contact Book===============")
choice=0
while True:
    menu()
    try:
        choice=int(input("ENter Choice Number="))
    except:
        print("Invalid Input!")
    if choice==1:
        add_contact()
    elif choice==2:
        view_contact()
    elif choice==3:
        search_contact()
    elif choice==4:
        update_contact()
    elif choice==5:
        delete_contact()
    elif choice==6:
        print("Thanks You \nVisit Again!")
        break
    else:
        print("Please give right choice number")




















