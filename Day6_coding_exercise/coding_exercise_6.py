member = input("Add a new member: ")

file = open(r"C:\\Users\\hadi.khadim\Desktop\STE AI - Abdul Hadi\Day6_coding_exercise\\members.txt", 'r')
existing_members = file.readlines()
file.close()

existing_members.append(member + "\n")

file = open(r"C:\\Users\\hadi.khadim\Desktop\STE AI - Abdul Hadi\Day6_coding_exercise\\members.txt", 'w')
existing_members = file.writelines(existing_members)
file.close()