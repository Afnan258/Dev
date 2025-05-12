import requests  # Import the requests library for making HTTP requests
import os        # Import the os module for interacting with the operating system (not used in this code)
import sys       # Import the sys module for accessing command-line arguments
from requests.auth import HTTPBasicAuth  # Import HTTPBasicAuth for handling basic authentication

def get_jira_ticket_status(ticket_id):
    # Construct the JIRA API URL using the provided ticket ID
    jira_url = f"https://deloitte-team-k2zkg8k5.atlassian.net/rest/api/3/issue/{ticket_id}"
    
    # Define the username and API token for JIRA authentication
    username = "aajazshaikh@deloitte.com"
    api_token = "ATATT3xFfGF0lCD15kxQ5Vs8lQdCOhyU7a2UX6HQ26zWs_WSp8jJnHBS2gXIbSxrZvtUMMNwgHDuROCDkj0L67WDqdsmQdVHFw77UNnbslOxy8dondGF2pTfySFQkv6of7OpXR1e8uxkQVd7l5SzULlQCfAx5irG7TIPRMc-0apbdlvBYiIrSfw=0D7DAFF5"
    
    # Create an HTTPBasicAuth object for authentication using the username and API token
    auth = HTTPBasicAuth(username, api_token)
    
    # Set the request headers to accept JSON responses
    headers = {'Accept': 'application/json'}
    
    # Make an HTTP GET request to the JIRA API endpoint
    response = requests.get(jira_url, headers=headers, auth=auth)

    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        # Parse the JSON response to get the issue details
        issue = response.json()
        
        # Return the status name of the JIRA issue
        return issue['fields']['status']['name']
    else:
        # Print an error message if the ticket number is incorrect
        print(f"Enter correct JIRA ticket number")
        
        # Return None to indicate failure to retrieve the status
        return None

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        # Exit the program with a status code of 1 if arguments are incorrect
        sys.exit(1)
    
    # Get the JIRA ticket ID from the command-line arguments
    ticket_id = sys.argv[1]
    
    # Call the function to get the JIRA ticket status
    status = get_jira_ticket_status(ticket_id)
    
    # If the status is successfully retrieved, print it
    if status:
        print(status)
