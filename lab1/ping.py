import os

with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print(" {park}  \n")

open('ip_output.csv', 'w').close()
f = open("ip_output.csv","a")

for ip in park:
    response = os.popen(f"ping -c 5 {ip} ").read()
    postres = response.split('\n')[6:]
    f.write(postres[1] + "\n")
    f.write(postres[3] + "\n" + "\n")
    print(postres)
f.close()