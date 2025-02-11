import os


with open("ip_list.txt") as file:
    park = file.read().splitlines()

file = open("ip_output.csv","w")

for ip in park:
    response = os.popen(f"ping -c 5 {ip} ").read()
    postresponse = response.split('\n')[6:]
    file.write(postresponse[1] + "\n")
    file.write(postresponse[3] + "\n" + "\n")
    print(postresponse)
file.close()
