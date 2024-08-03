contact = {}

def view_contact():
    print('Name\t\tContact Number')
    for key in contact:
        print('{}\t\t{}'.format(key, contact.get(key)))

while True:
    choice = int(input('Enter your choice:\n'
                       '1. Add new contact\n'
                       '2. Search contact\n'
                       '3. View contact\n'
                       '4. Edit contact\n'
                       '5. Delete contact\n'
                       '6. Exit\n'))
    
    if choice == 1:
        name = input('Enter a contact name: ')
        phone_number = input('Enter a mobile number: ')
        contact[name] = phone_number

    elif choice == 2:
        search_name = input('Enter a contact name: ')
        if search_name in contact:
            print(search_name, '\'s contact number is', contact[search_name])
        else:
            print('Contact is not found.')

    elif choice == 3:
        view_contact()

    elif choice == 4:
        edit_contact = input('Enter the contact to edit: ')
        if edit_contact in contact:
            phone = input('Enter a mobile number: ')
            contact[edit_contact] = phone
            print('Contact updated.')
            view_contact()
        else:
            print('Contact is not found.')

    elif choice == 5:
        del_contact = input('Enter the contact to delete: ')
        if del_contact in contact:
            confirm = input('Do you want to delete the contact (y/n)? ')
            if confirm.lower() == 'y':
                contact.pop(del_contact)
                view_contact()
        else:
            print('The contact is not found in the book.')

    elif choice == 6:
        break

    else:
        print('Invalid choice, please try again.')