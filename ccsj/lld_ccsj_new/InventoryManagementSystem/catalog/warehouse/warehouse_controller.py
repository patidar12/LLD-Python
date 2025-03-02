from typing import List

from catalog.warehouse import WareHouse
from catalog.warehouse.strategy import (
    WarehouseSelectionStrategy,
    NearestWarehouseSelectionStrategy
)

class WareHouseController:
    def __init__(self, warehouse_list: List[WareHouse], warehouse_selection_strategy: WarehouseSelectionStrategy):
        self.warehouses: List[WareHouse] = warehouse_list
        self.warehouse_selection_strategy: WarehouseSelectionStrategy = warehouse_selection_strategy
    
    def add_warehouse(self, warehouse: WareHouse):
        self.warehouses.append(warehouse)
    
    def remove_warehouse(self, warehouse: WareHouse):
        self.warehouses.remove(warehouse)

    def select_warehouse(self, selection_strategy: WarehouseSelectionStrategy):
        self.warehouse_selection_strategy = selection_strategy
        return  selection_strategy.select_warehouse(self.warehouses)
