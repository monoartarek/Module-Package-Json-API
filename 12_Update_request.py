# ------------------------------Update requests--------------------------------
import requests

data = {'userID' : 1, 'id' : 1, 'title': 'for test(updated)'} #(updated likhlam seshe bujhar jonno)
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json = data) #GET er jaygay put use korbo and link er seshe /1 dilam diye bujhailam je 1 no id jar ache take update korbo. karon oi link to amader create kora na ejonno.
print(response.status_code)
print(response.json())