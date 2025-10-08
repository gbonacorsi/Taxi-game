from enum import Enum
from Configuration.data_structure import ComponentRecord, component_record_keys, entity_type

class Matrix:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.matrix = [[[] for _ in range(cols)] for _ in range(rows)]
        
    def get_matrix(self) -> list:
        return self.matrix

    def list_records(self) -> list[list[tuple, dict]] | None:
    
        matrix = self.get_matrix()
        list_components = []       
            
        y=0
        while y < self.cols:
            
            x=0
            while x < self.rows:
                for component in matrix[y][x]:
                    list_components.append([(y,x), component])
                
                x += 1
            y +=1

        if list_components == []:
            return None
        else:
            return list_components

    def filter(self,  list_of_component: list[list[tuple, ComponentRecord]] | None, key: component_record_keys, criteria) -> list[list[tuple, ComponentRecord]] | None:

        list_component = list_of_component
        
        if list_component is not None:
            filtered = []
            
            key = key.value
            for (coords, component) in list_component:
                
                data = component.get_values()
                value=data[key]
                    
                if value == criteria:
                    filtered.append([coords, component])

            if filtered == []:
                return None
            else:
                return filtered
        else:
            return None

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
                list_record.append([position, record])
                
            return list_record

    def contain_type(self, position: tuple[int, int], type: entity_type) -> bool:
        
        components = self.return_position_records(position)
        filtered_components = self.filter(components, component_record_keys.type, type)
        if filtered_components is not None:
            return True
        else:
            return False

    def move_record(self, old_position: tuple[int, int], new_position: tuple[int, int], component: ComponentRecord) -> None:
        if component in self.matrix[old_position[1]][old_position[0]]:
            self.matrix[old_position[1]][old_position[0]].remove(component)
            self.matrix[new_position[1]][new_position[0]].append(component)
        
        component.instance.set_position(new_position)
        