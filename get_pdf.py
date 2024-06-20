import os
import requests

# get the pdf documents

pdf_path = "Nutrition_text_book.pdf"

# download pdf if it does not exists
if not os.path.exists(pdf_path):
    print("[INFO] Downloading PDF document...")

    # get the url for the docuement
    url = "https://pressbooks.oer.hawaii.edu/humannutrition2/open/download?type=pdf"

    # the local filename for the file
    file_name = pdf_path

    # send a get request to url
    response = requests.get(url)

    #check if request is successfu

    if response.status_code == 200:
      with open(file_name, "wb") as f:
        f.write(response.content)

      print(f"The File has been downloaded and saved as{file_name}")

    else:
      print(f"Error downloading the file:status_code:{response.status_code}")

else:
  print(f"The File has been downloaded and saved as {pdf_path}")

