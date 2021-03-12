import urllib.request

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()

pdf_path = ""

# Grade 7 Gauss Contests
for x in range(1998, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}Gauss7Contest.pdf", f"Grade 7 Gauss {x}")

# Grade 8 Gauss Contests
for x in range(1998, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}Gauss8Contest.pdf", f"Grade 8 Gauss {x}")

# Grade 7/8 Gauss Solutions
for x in range(1998, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}GaussSolution.pdf", f"Grade 7&8 Gauss {x} Solutions")

# Grade 9 Pascal Contests
for x in range(1997, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}PascalContest.pdf", f"Grade 9 Pascal {x}")

# Grade 9 Pascal Solutions
for x in range(1997, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}PascalSolution.pdf", f"Grade 9 Pascal {x} Solutions")

# Grade 10 Cayley Contests
for x in range(1997, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CayleyContest.pdf", f"Grade 10 Cayley {x}")

# Grade 10 Cayley Solutions
for x in range(1997, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CayleySolution.pdf", f"Grade 10 Cayley {x} Solutions")

# Grade 11 Fermat Contests
for x in range(1997, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}FermatContest.pdf", f"Grade 11 Fermat {x}")

# Grade 11 Fermat Solutions
for x in range(1997, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}FermatSolution.pdf", f"Grade 11 Fermat {x} Solutions")

# Grade 10 Galois Contests
for x in range(2003, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}GaloisContest.pdf", f"Grade 10 Galois {x}")

# Grade 10 Galois Solutions
for x in range(2003, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}GaloisSolution.pdf", f"Grade 10 Galois {x} Solutions")

# Grade 11 Hypatia Contests
for x in range(2003, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}HypatiaContest.pdf", f"Grade 11 Hypatia {x}")

# Grade 11 Hypatia Solutions
for x in range(2003, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}HypatiaSolution.pdf", f"Grade 11 Hypatia {x} Solutions")

# Grade 12 Euclid Contests
for x in range(1998, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}EuclidContest.pdf", f"Grade 12 Euclid {x}")

# Grade 12 Euclid Solutions
for x in range(1998, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}EuclidSolution.pdf", f"Grade 12 Euclid {x} Solutions")

# Canadian Intermediate Math Contests
for x in range(2011, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CIMC.pdf", f"Canadian Intermediate {x}")

# Canadian Intermediate Math Solutions
for x in range(2011, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CIMCSolution.pdf", f"Canadian Intermediate {x} Solutions")

# Canadian Senior Math Contests
for x in range(2011, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CSMC.pdf", f"Canadian Senior {x}")

# Canadian Senior Math Solutions
for x in range(2011, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CSMCSolution.pdf", f"Canadian Senior {x} Solutions")

# Canadian Team Math Contests - Individual
for x in range(2012, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CTMCIndividualProblems.pdf", f"Canadian Team Individual {x}")

# Canadian Team Math Contests - Relay
for x in range(2012, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CTMCRelayProblems.pdf", f"Canadian Team Relay {x}")

# Canadian Team Math Contests - Team
for x in range(2012, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CTMCTeamProblems.pdf", f"Canadian Team Team {x}")

# Canadian Team Math Contests - Answer Key
for x in range(2012, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CTMCAnswerKeys.pdf", f"Canadian Team {x} Answers")

# Canadian Team Math Solutions
for x in range(2014, 2021):
    download_file(f"https://www.cemc.uwaterloo.ca/contests/past_contests/{x}/{x}CTMCSoln.pdf", f"Canadian Team {x} Solutions")

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