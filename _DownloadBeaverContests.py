import urllib.request

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()

pdf_path = ""

# Beaver Grade 5/6 Computing Contests
for x in range(2017, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}BCCContest5_6.pdf", f"Grade 6 Beaver Computing {x}")

# Beaver Grade 5/6 Computing Solutions
for x in range(2017, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}BCCContestSolutions5_6.pdf", f"Grade 6 Beaver Computing {x} Solutions")

# Beaver Grade 7/8 Computing Contests
for x in range(2015, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}BCCContest7_8.pdf", f"Grade 8 Beaver Computing {x}")

# Beaver Grade 7/8 Computing Solutions
for x in range(2015, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}BCCContestSolutions7_8.pdf", f"Grade 8 Beaver Computing {x} Solutions")

# Beaver Grade 9/10 Computing Contests
for x in range(2012, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}BCCContest9_10.pdf", f"Grade 10 Beaver Computing {x}")

# Beaver Grade 9/10 Computing Contests
for x in range(2012, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}BCCContestSolutions9_10.pdf", f"Grade 10 Beaver Computing {x} Solutions")