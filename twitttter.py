#url= input("URL: ").strip()
#
#
#username= url.replace("http://twitter.com/","")
#print(f"username: {username}")
import re
url= input("URL: ").strip()
#username= re.sub(r"^(https?://)?(www\.)?twitter\.com/", "",url)
if username := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)",url,re.IGNORECASE):
    print(f"Username:",username.group(1))