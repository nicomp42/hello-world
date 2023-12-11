from ._anvil_designer import ArticleEditTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ArticleEdit(ArticleEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.categories = [(cat['name'], cat) for cat in app_tables.categories.search()]
    self.category_box.items = self.categories
