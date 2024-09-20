from ._anvil_designer import frmStartupTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from ..frmClientEdit import frmClientEdit


class frmStartup(frmStartupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_1.items = app_tables.clients.search()

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def add_client_click(self, **event_args):
    item={}
    editing_form = frmClientEdit(item=item)
    
    if alert(content=editing_form,large=True):
      #add the client information to the Data table
      anvil.server.call('add_client',item)
      #refresh the data grid
      self.repeating_panel_1.items= app_tables.clients.search()
    
