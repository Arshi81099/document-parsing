import pdfplumber
import re

# Define the path to your PDF file
pdf_file_path = "../../Downloads/Sow-sample/MPS SOW_ Senior SAP SD (Sunil Kumar) - Execute (part 1) - signed.pdf"  # Replace with your PDF file path

# Define the keywords to search for
import pdfplumber
keywords = ["SOW Term", "TOTAL"]

# Initialize a dictionary to store the extracted data
extracted_data = {keyword: "Keyword not found" for keyword in keywords}

# Open the PDF file and extract text
with pdfplumber.open(pdf_file_path) as pdf:
    pdf_text = ""
    for page in pdf.pages:
        pdf_text += page.extract_text()
        # print(pdf_text)
        # print("--------")
# Search for the keywords and extract associated values
for keyword in keywords:
    pattern = re.compile(rf'{keyword}(.*?)(?=\n|$)', re.IGNORECASE | re.DOTALL)
    match = pattern.search(pdf_text)

    if match:
        extracted_data[keyword] = match.group(1).strip()

# Print the extracted data
for keyword, value in extracted_data.items():
    print(f"{keyword}: {value}")









import pdfplumber
import re

# Define the path to your PDF file
pdf_file_path = "../../Downloads/Sow-sample/4700088360.pdf"  # Replace with your PDF file path

# Define the keywords to search for
import pdfplumber
keywords = ["PurchaseOrder#", "Order Date", "Print Date", "Total"]

# Initialize a dictionary to store the extracted data
extracted_data = {keyword: "Keyword not found" for keyword in keywords}

# Open the PDF file and extract text
with pdfplumber.open(pdf_file_path) as pdf:
    pdf_text = ""
    for page in pdf.pages:
        pdf_text += page.extract_text()
        # print(pdf_text)
        # print("--------")
# Search for the keywords and extract associated values
for keyword in keywords:
    pattern = re.compile(rf'{keyword}(.*?)(?=\n|$)', re.IGNORECASE | re.DOTALL)
    match = pattern.search(pdf_text)

    if match:
        extracted_data[keyword] = match.group(1).strip()

# Print the extracted data
for keyword, value in extracted_data.items():
    print(f"{keyword}: {value}")







import re

# Define the path to your PDF file
pdf_file_path = "../../Downloads/Sow-sample/2023-01-04 SOW  48 Request for Extension 2- Emma (Matchpoint Solutions - RHM).pdf"  # Replace with your PDF file path

# Define the keywords to search for
import pdfplumber
keywords = ["A+B ="]

# Initialize a dictionary to store the extracted data
extracted_data = {keyword: "Keyword not found" for keyword in keywords}

# Open the PDF file and extract text
with pdfplumber.open(pdf_file_path) as pdf:
    pdf_text = ""
    for page in pdf.pages:
        pdf_text += page.extract_text()

# Search for the keywords and extract associated values
for keyword in keywords:
    pattern = re.compile(rf'{re.escape(keyword)}\s*([$\d,.]+)', re.IGNORECASE)
    
    match = pattern.search(pdf_text)

    if match:
        extracted_data[keyword] = match.group(1).strip()

# Print the extracted data
for keyword, value in extracted_data.items():
    print(f"{keyword}: {value}")
