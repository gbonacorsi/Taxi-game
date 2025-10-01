from enum import Enum
from Configuration.data_structure import ComponentRecord, component_record_keys, entity_type

class Matrix:
    def __init__(self, rows: int, cols: int) -> None:
        self.rows = rows
        self.cols = cols
        self.matrix = [[[] for _ in range(cols)] for _ in range(rows)]
        
    def get_matrix(self) -> list:
        return self.matrix

    def list_records(self, index: list[component_record_keys] | None = None) -> list[list[tuple, dict]] | None:
    
        matrix = self.get_matrix()
        list_components = []       
            
        y=0
        while y < self.cols:
            
            x=0
            while x < self.rows:
                
                
                for component in matrix[y][x]:
                    
                    data = {}
                    if index is not None:
                        if index.count(component_record_keys.id) >= 1:
                            data["id"] = component.id
                        if index.count(component_record_keys.type) >= 1:
                            data["type"]  = component.type
                        if index.count(component_record_keys.instance) >= 1:
                            data["instance"] = component.instance
                        #if index.count(component_record_keys.position) >= 1:
                        #    data["position"]  = component.position
                        
                    else:
                            
                            data["id"] = component.id
                            data["type"]  = component.type
                            data["instance"] = component.instance
                        #    data["position"]  = component.position
                    list_components.append([(y,x), data])
                
                x += 1
            y +=1

        return list_components

    def filter(self, key: component_record_keys, criteria, index: list[component_record_keys] | None = None, list_of_component: list[list[tuple, ComponentRecord]] | None = None) -> list[list[tuple, dict]] | None:

        if list_of_component is not None:
            list_component = list_of_component
        else:
            list_component = self.list_records(index)

        filtered = []
        
        key = key.value
        for (coords, data) in list_component:
            
            value=data[key]
                
            if value == criteria:
                filtered.append([coords, data])

        return filtered if filtered else None

    def add_record(self, position: tuple[int, int], component: ComponentRecord) -> None:
        self.matrix[position[1]][position[0]].append(component)

    def remove_record(self, position: tuple[int, int], component: ComponentRecord) -> None:
        if component in self.matrix[position[1]][position[0]]:
            self.matrix[position[1]][position[0]].remove(component)

    def is_empty(self, position: tuple[int, int]) -> bool:
        coordinates_value = self.matrix[position[1]][position[0]]
        return True if coordinates_value == [] else False

    def update_record(self, position: tuple[int, int], old_component: ComponentRecord, new_component: ComponentRecord) -> None:
        if old_component in self.matrix[position[1]][position[0]]:
            self.matrix[position[1]][position[0]].remove(old_component)
            self.matrix[position[1]][position[0]].append(new_component)

    def return_position_records(self, position: tuple[int, int]) -> list[list[tuple, ComponentRecord]] | None:
        if 0 <= position[1] < self.rows and 0 <= position[0] < self.cols:
            components_record = self.matrix[position[1]][position[0]]
            if components_record == []:
                return None
            
            list_record = []
            for record in components_record:
                data = {}
                data["id"] = record.id
                data["type"]  = record.type
                data["instance"] = record.instance
                list_record.append([position, data])
                
            return list_record

    def contain_type(self, position: tuple[int, int], type: entity_type) -> bool:
        
        components = self.return_position_records(position)
        filtered_components = self.filter(component_record_keys.type, type, None, components)
        if components is not None and filtered_components is not None:
            if len(filtered_components) > 0:
                return True
            else:
                return False
        else:
            return False

    def move_record(self, old_position: tuple[int, int], new_position: tuple[int, int], component: ComponentRecord) -> None:
        if component in self.matrix[old_position[1]][old_position[0]]:
            self.matrix[old_position[1]][old_position[0]].remove(component)
            self.matrix[new_position[1]][new_position[0]].append(component)
        
        component.instance.set_position(new_position)
