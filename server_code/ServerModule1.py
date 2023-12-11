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

@anvil.server.callable
def get_articles():
  # Get a list of articles from the Data Table, sorted by 'created' column, in descending order
  return app_tables.articles.search(
    tables.order_by("created", ascending=False)
  )

@anvil.server.callable
def update_article(article, article_dict):
  # check that the article given is really a row in the ‘articles’ table
  if app_tables.articles.has_row(article):
    article_dict['updated'] = datetime.now()
    article.update(**article_dict)
  else:
    raise Exception("Article does not exist")