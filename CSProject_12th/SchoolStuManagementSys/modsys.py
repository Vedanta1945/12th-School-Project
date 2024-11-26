import csv, os, datetime , time
from termcolor import colored
from prettytable import from_csv, PrettyTable


# generating coloured font using "termcolour"

class fontcolor():
	'''
	This class contains functions for coloured fonts

	Available func:
	1.green()
	2.white()
	3.yellow()
	4.cyan()
	5.red()
	6.blue()

	Takes string as parameter, ex
	text = cyan("hello")

	Returns a coloured, bold string
	'''
	def green(string):
		return colored(string, "green", attrs=['bold'])
	def white(string):
		return colored(string, "white", attrs=['bold'])
	def yellow(string):
		return colored(string, "yellow", attrs=['bold'])
	def cyan(string):
		return colored(string, "cyan", attrs=['bold'])
	def red(string):
		return colored(string, "red", attrs=['bold'])
	def blue(string):
		return colored(string, "blue", attrs=['bold'])

# symbols
class smb:
	'''
	This class contains symbols
	'''
	WARN = fontcolor.red(" [-] ")
	DONE = fontcolor.green(" [+] ")
	INPUT = fontcolor.cyan(" [»] ")
	INFO = fontcolor.yellow(" [!] ")
	ARROW = fontcolor.cyan(" > ")

# Head banner
def headder():
	'''
	Prints the heading
	'''
	text = '''
             ╔═╗   ╦   ╔═╗     STUDENT
             ╚═╗   ║   ╚═╗     INFORMATION
             ╚═╝   ╩   ╚═╝     SYSTEM
          '''

	print(fontcolor.cyan(text))

# Numbers
class Num:
	'''
	contains number symbols
	'''
	one = fontcolor.yellow("[1] ")
	two = fontcolor.yellow("[2] ")
	three = fontcolor.yellow("[3] ")
	four = fontcolor.yellow("[4] ")
	five = fontcolor.yellow("[5] ")
	six = fontcolor.yellow("[6] ")
	seven = fontcolor.yellow("[7] ")
	eight = fontcolor.yellow("[8] ")
	nine = fontcolor.yellow("[9] ")
	zero = fontcolor.yellow("[0] ")

# generating bordered messages
def border_msg(msg):
	'''
	takes string as parameter, ex
	border_msg("hello")

	prints a bordered string, ex
	    +-------+
        | hello |
        +-------+
	'''
	row = len(msg)
	m = ''.join(['        +'] + ['-' *row] + ['+'])
	h = fontcolor.cyan(m)
	result= h + '\n' + fontcolor.cyan("        |") + fontcolor.white(msg) + fontcolor.cyan("|") + '\n' + h
	print((result))


#choice menu 
def display_menu():
	'''
	displays the menu
	'''
	choice_one = fontcolor.white("Add New Student")
	choice_two = fontcolor.white("View Students")
	choice_three = fontcolor.white("Search Student")
	choice_four = fontcolor.white("Update Student")
	choice_five = fontcolor.white("Delete Student")
	choice_six = fontcolor.white("Project Development Team")
	choice_seven = fontcolor.white("Quit")

	headder()
	border_msg(" Welcome To Student Information System ! ")
	print("\n" + smb.ARROW + fontcolor.cyan("CHOOSE AN OPTION :") + "\n")
	print(smb.ARROW + Num.one + choice_one)
	print(smb.ARROW + Num.two + choice_two)
	print(smb.ARROW + Num.three + choice_three)
	print(smb.ARROW + Num.four + choice_four)
	print(smb.ARROW + Num.five + choice_five)
	print(smb.ARROW + Num.six + choice_six)
	print(smb.ARROW + Num.seven + choice_seven)


#function for clearing screen
def clr_scr():
    if os.name == 'posix':
		# for linux and other operating system
        _ = os.system('clear')
    else:
        _ = os.system('cls')

#press enter to continue message
def continue_msg():
	input("\n" + smb.ARROW + fontcolor.cyan("Press Enter To Continue : "))
	clr_scr()

##### validation functions #####
class Validate:
	def Name(name):
		if name.replace(" ", "").isalpha():
			pass
		else:
			print("\n" + smb.WARN + fontcolor.red("Name Is Invalid ! It Should Not Have Digits !"))
			return False
		return True

	def Class(value):
		valid_classes = ('1','2','3','4','5','6','7','8,','9','10','11','12')
		if value in valid_classes:
			pass
		else:
			print("\n" + smb.WARN + fontcolor.red("Invalid Class !"))
			return False
		return True

	def RollNum(rollNum):
		try:
			roll = int(rollNum)
		except ValueError:
			print("\n" + smb.WARN + fontcolor.red("Roll Number Must Be A Number !"))
			return False
		return True

	def Dob(dob):
		try:
			date_of_birth = datetime.datetime.strptime(dob, "%d/%m/%Y")
		except:
			print("\n" + smb.WARN + fontcolor.red("Incorrect date ! Valid Format Is (DD/MM/YYYY)"))
			return False
		return True

	def Sex(sex):
		valid_sexes = set('mftMFT')
		if sex in valid_sexes:
			pass
		else:
			print("\n" + smb.WARN + fontcolor.red("Invalid Gender !"))
			return False
		return True

	def PhoneNum(phoneNum):
		if len(phoneNum) == 10:
			try:
				phone = int(phoneNum)
			except ValueError:
				print("\n" + smb.WARN + fontcolor.red("Phone Number Must Not Contains Letters !"))
				return False
		else:
			print("\n" + smb.WARN + fontcolor.red("It Must Contain 10 Digits !"))
			return False
		return True

'''
#########################################################################################
									MAIN FUNCTIONS
#########################################################################################
'''
# variables
raw_database = 'raw_data.csv'
student_database = 'students.csv'

#function to add students in database
def add_student():
	check = False
	'''
	adds new student in the database
	'''
	print("\n")
	border_msg(" Add A New Student's Information To Database ")
	print("\n")
	while not check:
		stu_name = input(smb.DONE + fontcolor.green("Student's Name : "))
		check = Validate.Name(stu_name)
	check = False
	while not check:
		stu_father = input(smb.DONE + fontcolor.green("Father's Name : "))
		check = Validate.Name(stu_father)
	check = False
	while not check:
		stu_class = input(smb.DONE + fontcolor.green("Class (1-12) : "))
		check = Validate.Class(stu_class)
	check = False
	while not check:
		roll_Num = input(smb.DONE + fontcolor.green("Roll No : "))
		check = Validate.RollNum(roll_Num)
	check = False
	while not check:
		stu_dob = input(smb.DONE + fontcolor.green("DOB (DD/MM/YYYY) : "))
		check = Validate.Dob(stu_dob)
	check = False
	while not check:
		stu_sex = input(smb.DONE + fontcolor.green("Sex (M/F/T) : "))
		check = Validate.Sex(stu_sex)
	check = False
	while not check:
		phone_Num = input(smb.DONE + fontcolor.green("Phone No (+91) : "))
		check = Validate.PhoneNum(phone_Num)
	check = False
	
	student_data = [stu_name, stu_father, stu_class, roll_Num, stu_dob,stu_sex,phone_Num]

	header = ['Student','Father','Class','Roll No','DOB','Sex(M/F/T)','Phone']
	with open(raw_database, mode = 'a+',newline="\n") as f:
		reader = csv.reader(f)
		writer = csv.writer(f)
		writer.writerow(student_data)

	f1 = open(student_database, mode = 'a+',newline="\n")
	f2 = open(raw_database, mode = 'r',newline="\n")
	end = f1.tell()
	f1.seek(0)
	reader1 = csv.reader(f1)
	reader2 = csv.reader(f2)
	writer1 = csv.writer(f1)
	try:
		fline = list(reader1)[0]
		if fline != header:
			writer1.writerow(header)
		else:
			f1.seek(end)
	except IndexError as e:
		if len(list(reader1)) == 0:
			writer1.writerow(header)
		else:
			print(e)
	f1.seek(0)
	f2.seek(0)
	try:
		AlrExist = []
		for x in list(reader2):
			f1.seek(0)
			if x in list(reader1):
				AlrExist.append(x)
			else:
				f1.seek(end)
				writer1.writerow(x)
				end = f1.tell()
		if len(AlrExist) != 0:
			print(border_msg("These Record Already Exists"))
			z = PrettyTable()
			z.field_names = ['Student','Father','Class','Roll No','DOB','Sex(M/F/T)','Phone']
			z.add_rows(AlrExist)
			print(z)

	except Exception as e:
		print("exception occured\n"+e)

	f2.close()
	f1.close()

	#printing recorded data
	try:
		x = PrettyTable()
		x.field_names = header
		x.add_row([student_data[0],student_data[1],student_data[2],student_data[3],student_data[4],student_data[5],student_data[6]])
		print("\n" + smb.DONE + fontcolor.green("Quick Overview :"))
		print(fontcolor.white(x))
		print("\n" + smb.DONE + fontcolor.green("Data Saved Successfully !"))
	except Exception:
		print("\n" + smb.WARN + fontcolor.red("Something Went Wrong ! Check Your Code !"))
	finally:
		continue_msg()

# main-function-2
#function to view the list of students in database
def view_students():
	print("\n")
	border_msg(" Student's Record In Our Information System ")
	try:
		fp = open(student_database, "r")
		file = from_csv(fp)
		fp.close()
		print(file)
	except (csv.Error, FileNotFoundError):
		print("\n" + smb.WARN + fontcolor.red("Something Went Wrong ! Check 'students.csv' File !"))
	finally:
		continue_msg()

# main-function-3
#function to search student with roll Num
def search_student():
	print("\n")
	border_msg(" Search For A Student Inside Database ")
	roll = input("\n" + smb.DONE + fontcolor.green("Enter Roll No. To Search : "))
	try:
		fd = open(student_database, "r", encoding="utf-8")
		reader = csv.reader(fd)
		for row in reader:
			if len(row) > 0:
				if roll == row[3]:
					print("\n")
					print(fontcolor.green("\t----- STUDENT FOUND -----") + "\n")
					print(smb.DONE + fontcolor.green("Student's Name : ") + row[0])
					print(smb.DONE + fontcolor.green("Father's Name : ") + row[1])
					print(smb.DONE + fontcolor.green("Class : ") + row[2])
					print(smb.DONE + fontcolor.green("Roll No : ") + row[3])
					print(smb.DONE + fontcolor.green("DOB (DD/MM/YYYY) : ") + row[4])
					print(smb.DONE + fontcolor.green("Sex (M/F/T) : ") + row[5])
					print(smb.DONE + fontcolor.green("Phone No : ") + row[6])
					break
		else:
			print("\n" + smb.WARN + fontcolor.red("Student Not Found In Our Database !!!"))
		
	except FileNotFoundError:
		print("\n" + smb.WARN + fontcolor.red("No Records To Search !"))
	finally:
		continue_msg()

#main-function-4
#function to update student data
def update_student():
	print("\n")
	border_msg(" Update Student's Record In Database ")
	roll_Num = input("\n" + smb.DONE + fontcolor.green("Enter Roll No. To Update : "))
	try:
		index_student = None
		updated_data = []
		fe = open(student_database, "r", encoding="utf-8")
		reader = csv.reader(fe)
		counter = 0
    	
		for row in reader:				
			if len(row) > 0:
				if roll_Num == row[3]:
					index_student = counter
					print("\n" + fontcolor.green('\t----- RECORD FOUND -----') + "\n")
					print(smb.DONE + fontcolor.cyan("Student Found At Index =>"), index_student)
					print(smb.DONE + fontcolor.cyan("Student's Name =>"), row[0])
					student_data = []
					print("\n")
					check = False
					while not check:
						new_stu_name = input(smb.DONE + fontcolor.green("Enter Student's New Name : "))
						check = Validate.Name(new_stu_name)
					while not check:
						new_stu_father = input(smb.DONE + fontcolor.green("Enter Father's New Name : "))
						check = Validate.Name(new_stu_father)
					while not check:
						new_stu_class = input(smb.DONE + fontcolor.green("Enter New Class (1-12) : "))
						check = Validate.Class(new_stu_class)
					while not check:
						new_roll_Num = input(smb.DONE + fontcolor.green("Enter New Roll No : "))
						check = Validate.RollNum(new_roll_Num)
					while not check:
						new_stu_dob = input(smb.DONE + fontcolor.green("Enter New DOB (DD/MM/YYYY) : "))
						check = Validate.Dob(new_stu_dob)
					while not check:
						new_stu_sex = input(smb.DONE + fontcolor.green("Enter New Sex (M/F/T) : "))
						check = Validate.Sex(new_stu_sex)
					while not check:
						new_phone_Num = input(smb.DONE + fontcolor.green("Enter New Phone No (+91) : "))
						check = Validate.PhoneNum(new_phone_Num)
    				
					student_data.append(new_stu_name)
					student_data.append(new_stu_father)
					student_data.append(new_stu_class)
					student_data.append(new_roll_Num)
					student_data.append(new_stu_dob)
					student_data.append(new_stu_sex)
					student_data.append(new_phone_Num)

					updated_data.append(student_data)
    			
				else:
					updated_data.append(row)
				counter += 1
    
	except FileNotFoundError:
		print("\n" + smb.WARN + fontcolor.red("No Records To Update !"))

#writing update to csv file
	if index_student is not None:
		with open(student_database, "w", encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerows(updated_data)
			print("\n" + smb.DONE + fontcolor.green("Data Updated Successfully ! "))
			continue_msg()
	else:
		print("\n" + smb.WARN + fontcolor.red("Student Not Found In Our Database !!!"))
		continue_msg()
        
# main-function-5
#function to delete student record
def delete_student():
	border_msg(" Delete Student's Record From Database ")
	roll = input("\n" + smb.WARN + fontcolor.red("Enter Roll No. To Delete : "))

	try:
		student_found = False
		updated_data = []
		ff = open(student_database, "r", encoding="utf-8")
		reader = csv.reader(ff)
		counter = 0
		for row in reader:
			if len(row) > 0:
				if roll != row[3]:
					updated_data.append(row)
					counter += 1
				else:
					student_found = True

	except FileNotFoundError:
		print("\n" + smb.WARN + fontcolor.red("No Records To Delete !"))

	if student_found is True:
		with open(student_database, "w", encoding="utf-8") as f:
			writer = csv.writer(f)
			writer.writerows(updated_data)
		print("\n" + smb.DONE + fontcolor.green("Roll No. Deleted Successfully"))
		continue_msg()
	else:
		print("\n" + smb.WARN + fontcolor.red("Roll No. Not Found In Our Database !!!"))
		continue_msg()

#main-function-6
#about us
def about_us():
	print("\n")
	border_msg(" Project Development Team ")
	#print("\n")
	z = PrettyTable()
	field_1 = fontcolor.green("Team Member")
	field_2 = fontcolor.green("Role")
	field_3 = fontcolor.green("Standard")
	z.field_names = [field_1,field_2,field_3]
	
	z.add_row(['Vedanta Mahour', 'Backend Programmer','XII A'])
	z.add_row(['Yashvardhan Choudhary', 'Testing','XII A'])
	z.add_row(['Vishwaraj Dixit', 'Interface Designer','XII A'])

	print(z)
	continue_msg()
