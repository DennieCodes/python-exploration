import random

__all__ = ("__version__", "ball")
__version__ = "3.0"
class ballException(Exception):
 pass
"""
Here we start the ball
"""
class ball:
 def __init__(self):
  self.responses_list=["As I see it, yes.", 
                       "Ask again later.", 
                       "Better not tell you now.", 
                       "Cannot predict now.", 
                       "Concentrate and ask again.", 
                       "Don’t count on it.", 
                       "It is certain.", 
                       "It is decidedly so.", 
                       "Most likely.", 
                       "My reply is no.", 
                       "My sources say no.", 
                       "Outlook not so good.", 
                       "Outlook good.", 
                       "Reply hazy, try again.", 
                       "Signs point to yes.", 
                       "Very doubtful.", 
                       "Without a doubt.", 
                       "Yes.", 
                       "Yes – definitely.", 
                       "You may rely on it.",
                       "What do you think?",
                       "Maybe yes maybe not"]
 def add_response_from_file(self, filename):
  with open(filename, "r") as f:
   choices = f.read().split("\n")
   for i in choices:
    self.responses_list.append(i)
    
 def override_response_from_file(self, filename):
  with open(filename, "r") as f:
   choices = f.read().split("\n")
   self.responses_list=choices
   
 def add_response(self, response):
  self.responses_list.append(response)
  
 def add_response_from_list(self, response_list):
  for i in response_list:
   self.response_list.append(i)
   
 def response(self, question):
   random.seed(len(question)*random.randint(0,10))
   return random.choice(self.responses_list)
