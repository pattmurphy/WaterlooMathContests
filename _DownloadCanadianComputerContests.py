import urllib.request

def download_file(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()

def download_zip(download_url, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(filename + ".zip", 'wb')
    file.write(response.read())
    file.close()

pdf_path = ""

ccc_url = [2020]
stage_url = [2019, 2018, 2017, 2016, 2015, 2014, 2013]

# CCC URL

# Canadian Computing Competition Problems
for x in ccc_url:
    download_file(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/ccc/juniorEF.pdf", f"Computing Competition Junior {x}")
    download_file(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/ccc/seniorEF.pdf", f"Computing Competition Senior {x}")

# Canadian Computing Competition Test Zips
for x in ccc_url:
    download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/ccc/all_data.zip", f"Computing Competition {x}")

# Canadian Computing Olympiad Problems
for x in ccc_url:
    download_file(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/cco/day1.pdf", f"Computing Olympiad {x} 1")
    download_file(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/cco/day2.pdf", f"Computing Olympiad {x} 2")

# Canadian Computing Olympiad Test Zips
for x in ccc_url:
    download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/cco/day1data.zip", f"Computing Olympiad {x}")
    download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/cco/day2data.zip", f"Computing Olympiad {x}")



# Stage URL

# Canadian Computing Competition Problems
for x in stage_url:
    download_file(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/stage 1/juniorEF.pdf", f"Computing Competition Junior {x}")
    download_file(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/stage 1/seniorEF.pdf", f"Computing Competition Senior {x}")

# Canadian Computing Competition Test Zips
all_data_url = [2019]
windows_url = [2018, 2017, 2016, 2015]
stage_folder_url = [2014, 2013]
for x in stage_url:
    if x in all_data_url:
        download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/stage 1/all_data.zip", f"Computing Competition {x}")
    elif x in windows_url:
        download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/WINDOWS.zip", f"Computing Competition {x}")
    elif x in stage_folder_url:
        download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/Stage1Data/WINDOWS.zip", f"Computing Competition {x}")

# Canadian Computing Olympiad Problems
for x in stage_url:
    download_file(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/stage 2/day1.pdf", f"Computing Olympiad {x} 1")
    download_file(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/stage 2/day2.pdf", f"Computing Olympiad {x} 2")

# Canadian Computing Olympiad Test Zips
data_suffix_url = [2019, 2015, 2014, 2013]
no_suffix_url = [2018, 2017, 2016]
for x in stage_url:
    if x in data_suffix_url:
        download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/stage 2/day1data.zip", f"Computing Olympiad {x}")
        download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/stage 2/day2data.zip", f"Computing Olympiad {x}")
    elif x in no_suffix_url:
        download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/stage 2/day1.zip", f"Computing Olympiad {x}")
        download_zip(f"https://www.cemc.uwaterloo.ca/contests/computing/{x}/stage 2/day2.zip", f"Computing Olympiad {x}")
