f = open("C:\\Users\\gohil\\OneDrive\\Desktop\\File Handling\\my_file_example.txt","r")

count = 0
for i in f.readlines():
    count += 1

print(count)