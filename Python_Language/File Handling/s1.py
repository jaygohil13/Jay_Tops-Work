f = open("C:\\Users\\gohil\\OneDrive\\Desktop\\File Handling\\my_file_example.txt","a")

for i in range(1,4):
    name = input("Enter subject : ")
    f.write("\n"+name)