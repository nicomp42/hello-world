import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
from datetime import datetime
@anvil.server.callable
def add_feedback(name, email, feedback, rate):
  app_tables.feedback.add_row(
    name=name, 
    email=email, 
    feedback=feedback, 
    created=datetime.now(),
    rate = rate
  )
  anvil.email.send(to="DirkGentlyhhgg@gmail.com",
                   subject=f"Feedback from {name}",
                   text=f""" A new person has filled out the feedback form! Name: {name} Email address: {email} Feedback: {feedback} """)

@anvil.server.callable
def add_article(article_dict):
  app_tables.articles.add_row(
    created=datetime.now(),
    **article_dict
  )