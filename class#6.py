file=open("hello.txt",'w')
file.write("Hello!\nmy name is DemonKingSwarn")
file.close()

file=open("hello.txt", 'r')
read_karo_bsdk = file.readlines()
for line in read_karo_bsdk:
    print(line + "\n", end="#")
