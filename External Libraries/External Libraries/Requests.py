# Requests Module - Working with APIs
# The requests library simplifies making HTTP requests. This is essential for interacting with web APIs (Application Programming Interfaces).
"""import requests

url = "https://api.github.com/users/octocat"  # Example API endpoint
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data["name"])  # Access data from the JSON
else:
    print(f"Error: {response.status_code}")

# Making a POST request (for sending data to an API):
# data = {"key": "value"}
# response = requests.post(url, json=data)  # Sends data as JSON

# Other HTTP methods: put(), delete(), etc."""