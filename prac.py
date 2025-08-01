import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.status_code)     # Should print 200
        # Will print the actual list of posts in JSON
