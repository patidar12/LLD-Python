from typing import List

from catalog.warehouse import WareHouse
from catalog.warehouse.strategy import WarehouseSelectionStrategy

class NearestWarehouseSelectionStrategy(WarehouseSelectionStrategy):

    def select_warehouse(self, warehouse_list: List[WareHouse]):
        # algo to pick the nearest algo, for now I am just picking the first warehouse for demo purpose
        return warehouse_list.get(0)
