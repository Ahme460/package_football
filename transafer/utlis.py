from leagues.utils import Rquest
from typing import Callable


class Get_transfer_team(Rquest):
    def get_transfer_team(self,url,headers,params):
       return self.rquest_data(url,headers,params)
