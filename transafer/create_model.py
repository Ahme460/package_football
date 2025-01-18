from .utlis import Analysis_data
from .model import Player_transfer
from typing import List

class Transfer_manger:
    def __init__(self,Analysis_data:Analysis_data,fatch_data) -> list[Player_transfer]:
        self.analysis=Analysis_data()
        self.raw_data=self.analysis.dict_data(fatch_data)
        self.transfer=self.create_transfer()

    def create_transfer(self):
        return list(map(lambda player_tr:Player_transfer(**player_tr),self.raw_data))
    
    def display_transfers(self):
        for transfer in self.transfers:
            print(transfer)

        
#تشكيلات الفرق هنطبق في مبداء 
            

