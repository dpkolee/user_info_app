list_of_users = []

def main():
	first_name = input('enter first name: ')
	last_name = input('enter last name: ')
	email = input('enter email: ')
	address = input('enter address: ')

	user_info = {
		'first_name': first_name,
		'last_name': last_name,
		'email': email,
		'address': address 
	}

	list_of_users.append(user_info)
	print('user list: ', list_of_users)

main()