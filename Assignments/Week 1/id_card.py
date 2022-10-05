print("Please fill out the following information for your ID Card.")
first_name = input('First Name: ')
last_name = input('Last Name: ')
email = input('Email address: ')
phone_number = input('Phone Number: ')
job_title = input('Job Title: ')
id_number = input('Id Number: ')
hair = input('Hair Color: ') 
eye = input('Eye Color: ') 
start = input('Month Started: ')
pre_ex = input('Pevious Experience Y/N: ')


print(f'''The ID Card is
---------------------------------------------
{last_name.upper()}, {first_name.capitalize()}
{job_title.title()}
ID: {id_number}

{email}
{phone_number}

Hair: {hair.title():15} Eye Color: {eye.capitalize()}
Month: {start.capitalize():14} Training: {pre_ex.capitalize()}
---------------------------------------------''')