from ._anvil_designer import ArticleViewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ArticleView(ArticleViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    #alert("**properties:", **properties)
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
