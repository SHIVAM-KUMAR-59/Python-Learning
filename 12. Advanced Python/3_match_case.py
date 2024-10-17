# Definition of match-case:
# match-case is a control structure introduced in Python 3.10 that is similar to switch-case statements 
# in other programming languages. It allows matching a value against a series of patterns and executing
# code based on which pattern matches.

def http_status(status): 
    # Using match-case to handle different HTTP status codes
    match status:  
        case 200: 
            return "OK"  # Status code 200 indicates success
        case 404: 
            return "Not Found"  # Status code 404 indicates the resource was not found
        case 500: 
            return "Internal Server Error"  # Status code 500 indicates a server error
        case _:  # The underscore (_) is a wildcard that matches any value not covered by the other cases
            return "Unknown status"  # This handles any unknown status code

# Testing the function with a status code not listed (5007)
status_code = 5007
result = http_status(status_code)

# Descriptive print statement showing the input status code and the corresponding result
print(f"HTTP Status for {status_code}: {result}")  
