import requests

target = input("Enter the target url: ")

if target.startswith("http"):
   url = target
else:
   url = "http://" + target

r = requests.get(url)

if r.status_code == 200:
   pass

else:
   print("[!] Connection Error, Please enter a valid Website")

wordlist = input("Enter the wordlist for hunting for directories: ")
a = open(wordlist,"r")

print("Let's hunt for some directories")

for i in a:
    word = i.strip()
    dir_url = url + "/" + word
    dir = requests.get(dir_url)
    if dir.status_code == 200 and 201 and 202 and 204:
       print(dir_url ," : " ,dir.status_code)
    elif dir.status_code == 300 and 301 and 302:
       print(dir_url ," : " ,dir.status_code)
    elif dir.status_code == 500 and 501 and 502 and 503:
       print(dir_url ," : " ,dir.status_code)
    else:
       pass
