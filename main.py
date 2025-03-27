from ftplib import FTP

ftp = FTP('103.240.90.98')
ftp.login()
with open('text', 'wb') as f:
    ftp.retrbinary('RETR text', f.write)
ftp.quit()

with open('text', 'r', encoding='utf-8', errors='ignore') as f:
    data = f.read().lower()

counts = {}
for char in data:
    if char.isalpha():  
        counts[char] = counts.get(char, 0) + 1

for letter in sorted(counts):
    print(f"{letter}: {counts[letter]}")

