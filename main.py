keys = {}

with open("NEET_UG_2024_KEY_03.06.2024.txt", "r") as f:
  content = f.read()
  pages = content.split("NATIONAL TESTING AGENCY")
  pages.pop(0)

  for page in pages:
    key = {}
    lines = page.split("\n")
    code = lines[1][-3:]

    lines = lines[6:-1] 

    for line in lines:

      li = line.strip().split(" ")
      key[li[0]] = li[1]
    keys[code] = key

with open("2024.key", "a") as f:
  f.write(f"{keys}")
  f.close()
