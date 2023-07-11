class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.next = None

class PhoneDirectory:
    def __init__(self):
        self.head = None

    def addContact(self, name, phone_number):
        new_contact = Contact(name, phone_number)
        if self.head is None:
            self.head = new_contact
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_contact

    def searchContact(self, name):
        curr = self.head
        while curr:
            if curr.name.lower() == name.lower():
                return curr.phone_number
            curr = curr.next
        return None

    def deleteContact(self, name):
        if self.head is None:
            return

        if self.head.name.lower() == name.lower():
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.name.lower() == name.lower():
                curr.next = curr.next.next
                return
            curr = curr.next

    def displayDirectory(self):
        curr = self.head
        if curr is None:
            print("Phone directory is empty.")
        else:
            print("Phone Directory:")
            while curr:
                print(f"Name: {curr.name}, Phone Number: {curr.phone_number}")
                curr = curr.next

# Example usage
phone_dir = PhoneDirectory()
phone_dir.addContact("John Doe", "1234567890")
phone_dir.addContact("Jane Smith", "9876543210")
phone_dir.addContact("David Johnson", "5555555555")

phone_dir.displayDirectory()
# Output:
# Phone Directory:
# Name: John Doe, Phone Number: 1234567890
# Name: Jane Smith, Phone Number: 9876543210
# Name: David Johnson, Phone Number: 5555555555

search_result = phone_dir.searchContact("Jane Smith")
print(f"Phone number for Jane Smith: {search_result}")
# Output: Phone number for Jane Smith: 9876543210

phone_dir.deleteContact("Jane Smith")
phone_dir.displayDirectory()
# Output:
# Phone Directory:
# Name: John Doe, Phone Number: 1234567890
# Name: David Johnson, Phone Number: 5555555555
