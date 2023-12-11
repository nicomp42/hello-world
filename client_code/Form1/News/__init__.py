from ._anvil_designer import NewsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ArticleEdit import ArticleEdit

class News(NewsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.refresh_articles()

  def add_article_button_click(self, **event_args):
    # Initialise an empty dictionary to store the user inputs
    new_article = {}
    # Open an alert displaying the 'ArticleEdit' Form
    save_clicked = alert(
      content=ArticleEdit(item=new_article),
      title="Add Article",
      large=True,
      buttons=[("Save", True), ("Cancel", False)],
    )
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      #alert(("Save Clicked"))
      #print(new_article)
      anvil.server.call('add_article', new_article)
      self.refresh_articles()
  def refresh_articles(self):
    # Load existing articles from the Data Table, 
    # and display them in the RepeatingPanel
    self.articles_panel.items = anvil.server.call('get_articles')