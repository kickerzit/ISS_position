# http://api.open-notify.org/iss-now.json
# restfulapi.net
# json pretty


#prvně musíme udělat request (žádost)
# response = odpověď
# pip install requests

import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status() # .raise_for_status = nic nebude dělat, pokud vše ok. Pokud chyba, vypíše chybu podrobně
print(response.status_code) # .status_code = vrátí pouze status code 1xx, 2xx...



# odpověď response = vše OK (vše co začíná dvojkou = vše ok, tady máš data)

# 1xx = ještě není konec
# 2xx = vše ok, tady máš data
# 3xx = přesměrování
# 4xx = chyba na straně uživatele
# 5xx = chyba na serveru, na straně poskytovatele