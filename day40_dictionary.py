print("🌟Contact Card🌟")

dit = {}
dit["Name"] = input("Enter Name: ")
dit["birthday"] = input("Enter you date of birth:")
dit["Phone"] = input("Enter Phone Number: ")
dit["Email"] = input("Enter Email: ")
dit["address"] = input("Enter Address: ") 

print(f"Hi {dit['Name']}. Our dictionary says that you were born on {dit['birthday']}. Your phone number is {dit['Phone']}. Your email is {dit['Email']}. Your address is {dit['address']}." )  
