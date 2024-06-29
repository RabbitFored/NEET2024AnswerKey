'''
from bs4 import BeautifulSoup

def scrape_page(page):
  with open(page, "r") as f:
    keys = {}
    soup = BeautifulSoup(f.read(), 'html.parser')
    s = soup.find_all('tr', class_='form-options-item')
    for i in s:
      k = i.select("td:nth-of-type("+str(2)+")")    
      keys[i.td.text] = k[0].text
    return keys

key = scrape_page("answer-key.html")    # json/dict of official answer key
res = scrape_page("omr-response.html")  # json/dict of omr scanned response
'''

def split_dict(d,n):
  items = list(d.items())
  dicts = [dict(items[x:x+n]) for x in range(0, len(d), n)]
  return dicts

def remove_blank(d):
  new_list = {}
  for k in list(d.keys()):
      ans = key[k]
      re = d[k]
      if re == "-":
        pass
      else:
        new_list[k] = re
  return new_list
  
def evaluate(d,key):
   c = 0
   w = 0
   keys = d.keys()
   for k in keys:
     ans = key[k]
     re = res[k]
     if ans == re:
       c = c + 1 
     elif re == "-":
       pass
     else:
      w = w + 1
   return c, w 
    


def calculate_total(res, key):
  correct = 0 
  wrong = 0
  
  response = []

  subs = split_dict(res, 50)
  for sub in subs:
    sec = split_dict(sub, 35)
    response.append(sec)
    
  for subject in response:
      sectionA = subject[0]
      sectionB = subject[1]


      sectionB = split_dict(remove_blank(sectionB),10)[0]

      c,w = evaluate(sectionA,key)
      correct = correct + c
      wrong = wrong + w

      c,w = evaluate(sectionB,key)

      correct = correct + c
      wrong = wrong + w

  print(f'''
\033[34mCORRECT = \033[0m{correct}
\033[34mWRONG   = \033[0m{wrong}
-----------------
\033[34mTOTAL    => \033[0m{4*correct - wrong}
-----------------
''')

calculate_total(res,key)
