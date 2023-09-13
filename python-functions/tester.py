'''
The function can_buy_ticket will determine if a person can buy a lottery ticket.

It will accept a dictionary as input containing the following properties:

Parameter	Type	Description
age	Integer	The age of the person
state	String (optional)	The two-letter US state abbreviation
The function will return True if someone lives in NV or NJ, and is 18 years or older. It will also return True if someone is 21 years or older from any state. Otherwise, it will return False.

Please fix the function below so that it will pass its unit tests and not fail when the "state" key is missing or non-existent.

Examples:

input	output
{ "age" : 14 }	False
{ "age" : 25 }	True
{ "age" : 18, "state": "NV" }	True

'''