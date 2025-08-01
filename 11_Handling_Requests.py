#ekta website kivabe kaj kore?

#Request , Response cycle er maddhomne
#Request <------> ( API ) <-------> Response

#Example: (ei 4 dhoroner request ei amra whole life kaj korbo)
#Ostad er website account create kori - POST request
#course details dekhar request kori - GET request
#nijer profile Update kori - PUT/PATCH/Update request
#Ostad kono course delete korte pare - DELETE request

#python er request module diye amra egula korbo
# search on google : json placeholder 

# ------------------------
# 200	OK	Request succeeded.
# 201	Created	Resource created successfully.
# 202	Accepted	Request accepted but not yet processed.
# 204	No Content	Request succeeded, no content returned.
# ---------------------------

import requests
# -------------------------------GET requests--------------------------------

response = requests.get("https://jsonplaceholder.typicode.com/posts") # eta evabe kaj kore na er directly --error--dekhabe so er jonno ekta command dite hobe---> pip install requests ----eta dile sob install hobe ekhane

print(response.status_code)
print(response.json())  

# ------------------------------POST requests--------------------------------

data = {'userID' : 1, 'id' : 1, 'title': 'for test'}
response = requests.post("https://jsonplaceholder.typicode.com/posts", json = data)
print(response.status_code)
print(response.json())

# ------------------------------Update requests--------------------------------