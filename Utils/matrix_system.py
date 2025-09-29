from enum import Enum


record1 = {
    "id": 1,
    "type": "client",
    "instance": "object",
    "position": (2,5),
    "grid_id": 1}

record2 = {
    "id": 2,
    "type": "player",
    "instance": "object",
    "position": (3,6),
    "grid_id": 8 }

record3 = {
    "id": 3,
    "type": "destination",
    "instance": "object",
    "position": (8,10),
    "grid_id": 5 }

record4 = {
    "id": 4,
    "type": "destination",
    "instance": "object",
    "position": (12,15),
    "grid_id": 7 }

record5 = {
    "id": 5,
    "type": "client",
    "instance": "object",
    "position": (4,5),
    "grid_id": 78 }


matrix = [
    [[record1, record2],[record3],],
    [[record4],[record5]]
]

def unzip_components(matrix, index: list):
    
    components_unziped = []
            
    y_range = len(matrix)
        
    y=0
    while y < y_range:
        x_range = len(matrix[y])
        
        x=0
        data = {}
        while x < x_range:
            
            
            for component in matrix[y][x]:
                
                if index.count("id") >= 1:
                    data["id"] = component["id"]
                elif index.count("type") >= 1:
                    data["type"]  = component["type"],
                elif index.count("instance") >= 1:
                    data["instance"] = component["instance"]
                elif index.count("position") >= 1:
                    data["position"]  = component["position"]
                elif index.count("grid_id") >= 1:
                    data["grid_id"]  = component ["grid_id"]
                
                components_unziped.append([(y,x), data])
            
            x += 1
        y +=1
        
    return components_unziped


def find_element():
    print("find element")
    

def add_component():
    print("add component")
    
    
def remove_component():
    print("remove component")

def update_component():
    print("update component")
    

data_entity = unzip_components(matrix,["type"])
print(data_entity)
#data_entity.filter("type='destination' and position=(1,2)")


sample = [[(0, 0), {'type': ('destination',)}], [(0, 0), {'type': ('destination',)}], [(0, 1), {'type': ('destination',)}], [(1, 0), {'type': ('client',)}], [(1, 1), {'type': ('client',)}]]

criterion = "type='destination' and position=(1,2)"
criterion_parts = criterion.split(" and ")
criterion1 = "type='destination'"

def filter(criterio: str, sample: list):
    
    output = []
    
    criterion_elements = criterion.split("=")
    
    for element in sample:
        if criterion_elements[0] == "position" and tuple(criterion_elements[1]) == element[0]:
            output.append(element)
        elif criterion_elements[0] == "id" and criterion_elements[1] == element[1]["id"]:
            output.append(element)
        elif criterion_elements[0] == "instance" and criterion_elements[1] == element[1]["instance"]:
            output.append(element)
        elif criterion_elements[0] == "grid_id" and criterion_elements[1] == element[1]["grid_id"]:
            output.append(element)
    
    return output

print(filter("type=client",sample))