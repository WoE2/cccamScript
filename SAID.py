import os
host=input("Enter your host: ")
port=input("Enter your port: ")
user=input("Enter your user: ")
pass1=input("Enter your pass: ")
#password =input("Enter Password : ")
#فتح الملف للكتابة وإنشاؤه إن لم يكن موجود
file = open("D:\Cccam.cfg", "a")
#كتابة البيانات إلى الملف
file.write("\nC: "+host.upper()+" "+port.upper()+" "+user.upper()+" "+pass1.upper())
file.close()
# قراءة محتوى الملف وطباعتها على الشاشة
data = open("D:\Cccam.cfg", "r")
for line in data:
    print(line)
#عرض حجم الملف
size = os.path.getsize("D:\Cccam.cfg") 
print(f"\nThe size of file is {size} bytes")
exit