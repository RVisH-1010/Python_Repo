print("this is day 5 of pythin in github")
# # question merge pdf using pypdf module in ptyhon
# from pypdf import PdfWriter
# import os

# merger = PdfWriter()
# files =[file for file in os.listdir() if file.endswith(".pddf")]

# for pdf in files:
#     merger.append(pdf)
 
# merger.write("Merged-pdf.pdf")
# merger.close



# 1. time module in py
import time
print("hey\n5 sec earlier")
# time.sleep(10)
# print("5s later")
t = time.localtime()
form_t = time.strftime("%y-%m-%d time is>> %H:%M:%S",t)

print(form_t)
