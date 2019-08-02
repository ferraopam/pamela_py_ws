from contact import Contact
class ContactBook:
   contacts= []
   @staticmethod 
   def addContact():
       nam = input("Enter the name:")
       email = input("Enter the email:")
       mobile = input("Enter the mobil:")
       ContactBook.contacts.append(Contact(name,email,mobile))
    @staticmethod 
    def searchContact():
        name = input("Enter the name to search:")
        //LOGIC

    @staticmethod
    def deleteContact():
        name = input("Enter the name to delete:")
        //LOGIC
    @staticmethod 
    def viewAll():
        pass
    @staticmethod 
    def updateContact():
        name = input("enter the contact name to update")
        contact = getContact(name)
        print("1.Email 2.Name 3.Mobile")
        ch = input("Enter the choice:")
