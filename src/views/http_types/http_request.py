from typing import Dict


class HttpRequest:
  def __init__(self, 
               header: Dict = None, 
               body: Dict = None, 
               quert_params: Dict = None
               ) -> None:
    self.header = header
    self.body = body
    self.quert_params = quert_params