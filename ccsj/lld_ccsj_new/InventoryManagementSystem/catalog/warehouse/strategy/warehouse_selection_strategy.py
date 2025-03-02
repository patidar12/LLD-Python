from typing import List
from abc import ABC, abstractmethod

from catalog.warehouse import WareHouse

class WarehouseSelectionStrategy(ABC):

    @abstractmethod
    def select_warehouse(self, warehouse_list: List[WareHouse]): pass