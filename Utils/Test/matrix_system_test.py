import sys
import os

# Aggiungi la cartella root al Python path per pytest
project_root = os.path.dirname(os.path.abspath(__name__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

print(f"✅ Added to Python path: {project_root}")
import pytest
from Utils.matrix_system import Matrix
from Configuration.data_structure import ComponentRecord, component_record_keys, entity_type

class TestMatrix:
    """Test suite per la classe Matrix"""

    def setup_method(self):
        """Setup eseguito prima di ogni test"""
        self.matrix = Matrix(5, 5)
        
        # ✅ CORREZIONE: ComponentRecord con struttura corretta
        self.player_record = ComponentRecord(
            id=1,
            type=entity_type.player,
            instance=entity_type.player,  # Usa enum invece di classe
            position=(0, 0),

        )
        
        self.client_record = ComponentRecord(
            id=2,
            type=entity_type.client,
            instance=entity_type.client,  # Usa enum invece di classe
            position=(1, 1),

        )
        
        self.wall_record = ComponentRecord(
            id=3,
            type=entity_type.wall,
            instance=entity_type.wall,  # Usa enum invece di classe
            position=(2, 2),

        )

    def test_init(self):
        """Test inizializzazione Matrix"""
        matrix = Matrix(3, 4)
        assert matrix.rows == 3
        assert matrix.cols == 4
        assert len(matrix.matrix) == 3
        assert len(matrix.matrix[0]) == 4
        assert matrix.matrix[0][0] == []

    def test_get_matrix(self):
        """Test get_matrix restituisce la matrice"""
        result = self.matrix.get_matrix()
        assert result == self.matrix.matrix
        assert isinstance(result, list)

class TestMatrixAddRecord:
    """Test per add_record method"""
    
    def setup_method(self):
        """Setup per ogni test"""
        self.matrix = Matrix(5, 5)
    
    def test_add_single_record(self):
        """Test aggiunta singolo record"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),

        )
        
        self.matrix.add_record((2, 3), player)
        
        assert len(self.matrix.matrix[3][2]) == 1
        assert self.matrix.matrix[3][2][0] == player

    def test_add_multiple_records_same_position(self):
        """Test aggiunta multipli record stessa posizione"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(1, 1),

        )
        client = ComponentRecord(
            id=2, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(1, 1),

        )

        self.matrix.add_record((1, 1), player)
        self.matrix.add_record((1, 1), client)
        
        assert len(self.matrix.matrix[1][1]) == 2
        assert player in self.matrix.matrix[1][1]
        assert client in self.matrix.matrix[1][1]

    def test_add_record_boundary_positions(self):
        """Test aggiunta ai confini della matrice"""
        record = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(0, 0),

        )
        
        # Angolo top-left
        self.matrix.add_record((0, 0), record)
        assert self.matrix.matrix[0][0][0] == record
        
        # Angolo bottom-right
        record2 = ComponentRecord(
            id=2, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(4, 4),

        )
        self.matrix.add_record((4, 4), record2)
        assert self.matrix.matrix[4][4][0] == record2

class TestMatrixListRecords:
    """Test per list_records method - il metodo principale del tuo Matrix"""
    
    def setup_method(self):
        """Setup per ogni test"""
        self.matrix = Matrix(3, 3)
    
    def test_list_all_records_no_index(self):
        """Test lista tutti i record senza indice specifico"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(1, 1),

        )
        client = ComponentRecord(
            id=2, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(2, 2),

        )

        self.matrix.add_record((1, 1), player)
        self.matrix.add_record((2, 2), client)
        
        result = self.matrix.list_records()
        
        assert result is not None
        assert len(result) == 2
        
        # Verifica struttura: lista di [(position, ComponentRecord), ...]
        assert isinstance(result, list)
        for item in result:
            assert isinstance(item, list)
            assert len(item) == 2
            position, record = item
            assert isinstance(position, tuple)
            assert len(position) == 2
            assert isinstance(record, dict)

    def test_list_records_with_specific_index(self):
        """Test lista record con indice specifico"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(1, 1),
   
        )
        self.matrix.add_record((1, 1), player)
        
        # Test con index specifico per id e type
        index = [component_record_keys.id, component_record_keys.type]
        result = self.matrix.list_records(index)
        
        assert result is not None
        assert len(result) == 1
        
        position, data = result[0]
        assert position == (1, 1)
        assert isinstance(data, dict)
        assert component_record_keys.id.value in data
        assert component_record_keys.type.value in data
        assert data[component_record_keys.id.value] == 1
        assert data[component_record_keys.type.value] == entity_type.player

    def test_list_records_single_field(self):
        """Test lista record con un solo campo"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(1, 1),
  
        )
        self.matrix.add_record((1, 1), player)
        
        # Solo il tipo
        index = [component_record_keys.type]
        result = self.matrix.list_records(index)
        
        assert result is not None
        assert len(result) == 1
        
        position, data = result[0]
        assert position == (1, 1)
        assert len(data) == 1
        assert component_record_keys.type.value in data
        assert component_record_keys.id.value not in data

    def test_list_records_empty_matrix(self):
        """Test lista su matrice vuota"""
        result = self.matrix.list_records()
        assert result == []

    def test_list_records_multiple_components_same_position(self):
        """Test lista con più componenti nella stessa posizione"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(1, 1),
     
        )
        client = ComponentRecord(
            id=2, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(1, 1),  # Stessa posizione del player

        )

        self.matrix.add_record((1, 1), player)
        self.matrix.add_record((1, 1), client)
        
        result = self.matrix.list_records()
        
        assert result is not None
        assert len(result) == 2  # Due record dalla stessa posizione
        
        # Verifica che entrambi abbiano la stessa posizione
        positions = [item[0] for item in result]
        assert positions.count((1, 1)) == 2

    def test_list_records_all_fields(self):
        """Test lista con tutti i campi disponibili"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(1, 1),

        )
        self.matrix.add_record((1, 1), player)
        
        # Tutti i campi
        index = [
            component_record_keys.id, 
            component_record_keys.type, 
            component_record_keys.instance,
        ]
        result = self.matrix.list_records(index)
        
        assert result is not None
        assert len(result) == 1
        
        position, data = result[0]
        assert position == (1, 1)
        assert len(data) == 3
        assert data[component_record_keys.id.value] == 1
        assert data[component_record_keys.type.value] == entity_type.player

class TestMatrixRemoveRecord:
    """Test per remove_record method"""
    
    def setup_method(self):
        """Setup per ogni test"""
        self.matrix = Matrix(5, 5)
    
    def test_remove_existing_record(self):
        """Test rimozione record esistente"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),

        )
        
        self.matrix.add_record((2, 3), player)
        assert len(self.matrix.matrix[3][2]) == 1
        
        self.matrix.remove_record((2, 3), player)
        assert len(self.matrix.matrix[3][2]) == 0

    def test_remove_non_existing_record(self):
        """Test rimozione record non esistente"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),

        )
        
        # Non dovrebbe crashare
        self.matrix.remove_record((2, 3), player)
        assert len(self.matrix.matrix[3][2]) == 0

    def test_remove_one_of_multiple_records(self):
        """Test rimozione uno di più record"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(1, 1),

        )
        client = ComponentRecord(
            id=2, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(1, 1),

        )

        self.matrix.add_record((1, 1), player)
        self.matrix.add_record((1, 1), client)
        
        self.matrix.remove_record((1, 1), player)
        
        assert len(self.matrix.matrix[1][1]) == 1
        assert self.matrix.matrix[1][1][0] == client

class TestMatrixIsEmpty:
    """Test per is_empty method"""
    
    def setup_method(self):
        """Setup per ogni test"""
        self.matrix = Matrix(5, 5)
    
    def test_empty_position(self):
        """Test posizione vuota"""
        assert self.matrix.is_empty((2, 3)) == True

    def test_non_empty_position(self):
        """Test posizione non vuota"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),
 
        )
        self.matrix.add_record((2, 3), player)
        
        assert self.matrix.is_empty((2, 3)) == False

class TestMatrixUpdateRecord:
    """Test per update_record method"""
    
    def setup_method(self):
        """Setup per ogni test"""
        self.matrix = Matrix(5, 5)
    
    def test_update_existing_record(self):
        """Test aggiornamento record esistente"""
        old_player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),

        )
        new_player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),

        )

        self.matrix.add_record((2, 3), old_player)
        self.matrix.update_record((2, 3), old_player, new_player)
        
        assert len(self.matrix.matrix[3][2]) == 1
        assert self.matrix.matrix[3][2][0] == new_player
        assert old_player not in self.matrix.matrix[3][2]

    def test_update_non_existing_record(self):
        """Test aggiornamento record non esistente"""
        old_player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),

        )
        new_player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),

        )

        # Non dovrebbe crashare
        self.matrix.update_record((2, 3), old_player, new_player)
        assert len(self.matrix.matrix[3][2]) == 0

class TestMatrixReturnPositionRecords:
    """Test per return_position_records method"""
    
    def setup_method(self):
        """Setup per ogni test"""
        self.matrix = Matrix(5, 5)
    
    def test_valid_position_with_records(self):
        """Test posizione valida con record"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),

        )
        client = ComponentRecord(
            id=2, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(2, 3),

        )

        self.matrix.add_record((2, 3), player)
        self.matrix.add_record((2, 3), client)
        
        result = self.matrix.return_position_records((2, 3))
        
        assert result is not None
        assert len(result) == 2

    def test_valid_position_empty(self):
        """Test posizione valida ma vuota"""
        result = self.matrix.return_position_records((2, 3))
        assert result is None

    def test_invalid_position(self):
        """Test posizione fuori dai confini"""
        # Fuori confini
        assert self.matrix.return_position_records((10, 10)) is None
        assert self.matrix.return_position_records((-1, 0)) is None
        assert self.matrix.return_position_records((0, -1)) is None

class TestMatrixFilter:
    """Test per filter method"""
    
    def setup_method(self):
        """Setup per ogni test"""
        self.matrix = Matrix(5, 5)
    
    def test_filter_by_type(self):
        """Test filtro per tipo"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(1, 1),

        )
        client1 = ComponentRecord(
            id=2, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(2, 2),

        )
        client2 = ComponentRecord(
            id=3, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(3, 3),
  
        )

        self.matrix.add_record((1, 1), player)
        self.matrix.add_record((2, 2), client1)
        self.matrix.add_record((3, 3), client2)
        
        # Filtra per CLIENT
        result = self.matrix.filter(
            component_record_keys.type, 
            entity_type.client
        )
        
        assert result is not None
        assert len(result) == 2

    def test_filter_no_matches(self):
        """Test filtro senza risultati"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(1, 1),

        )
        self.matrix.add_record((1, 1), player)
        
        result = self.matrix.filter(
            component_record_keys.type, 
            entity_type.wall.value
        )
        
        assert result is None

    def test_filter_with_predefined_list(self):
        """Test filtro su lista predefinita"""
        # Crea lista predefinita
        predefined_list = [
            [(1, 1), {"type": entity_type.player.value, "id": 1}],
            [(2, 2), {"type": entity_type.client.value, "id": 2}]
        ]
        
        result = self.matrix.filter(
            component_record_keys.type,
            entity_type.player.value,
            list_of_component=predefined_list
        )
        
        assert result is not None
        assert len(result) == 1
        assert result[0][1]["type"] == entity_type.player.value

class TestMatrixIsContainType:
    """Test per is_contain_type method"""
    
    def setup_method(self):
        """Setup per ogni test"""
        self.matrix = Matrix(5, 5)
    
    def test_position_contains_type(self):
        """Test posizione contiene tipo specifico"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),
  
        )
        self.matrix.add_record((2, 3), player)
        
        assert self.matrix.is_contain_type((2, 3), entity_type.player.value) == True

    def test_position_not_contains_type(self):
        """Test posizione non contiene tipo"""
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(2, 3),

        )
        self.matrix.add_record((2, 3), player)
        
        assert self.matrix.is_contain_type((2, 3), entity_type.client.value) == False

    def test_empty_position_not_contains_type(self):
        """Test posizione vuota non contiene tipo"""
        assert self.matrix.is_contain_type((2, 3), entity_type.player.value) == False

# ===== INTEGRATION TESTS =====

class TestMatrixIntegration:
    """Test di integrazione per scenari complessi"""

    def setup_method(self):
        """Setup per integration tests"""
        self.matrix = Matrix(10, 10)

    def test_full_game_scenario(self):
        """Test scenario completo di gioco"""
        # Setup game world
        player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(5, 5),

        )
        client1 = ComponentRecord(
            id=2, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(3, 3),
  
        )
        client2 = ComponentRecord(
            id=3, 
            type=entity_type.client, 
            instance=entity_type.client,
            position=(7, 7),
     
        )
        destination = ComponentRecord(
            id=4, 
            type=entity_type.destination, 
            instance=entity_type.destination,
            position=(9, 9),

        )
        wall = ComponentRecord(
            id=5, 
            type=entity_type.wall, 
            instance=entity_type.wall,
            position=(4, 4),

        )
        
        # Add all entities
        self.matrix.add_record((5, 5), player)
        self.matrix.add_record((3, 3), client1)
        self.matrix.add_record((7, 7), client2)
        self.matrix.add_record((9, 9), destination)
        self.matrix.add_record((4, 4), wall)
        
        # Test: List all entities
        all_records = self.matrix.list_records()
        assert len(all_records) == 5
        
        # Test: Filter clients
        clients = self.matrix.filter(component_record_keys.type, entity_type.client)
        assert len(clients) == 2
        
        # Test: Move player (simulate)
        self.matrix.remove_record((5, 5), player)
        new_player = ComponentRecord(
            id=1, 
            type=entity_type.player, 
            instance=entity_type.player,
            position=(5, 6),

        )
        self.matrix.add_record((5, 6), new_player)
        
        assert self.matrix.is_empty((5, 5)) == True
        assert self.matrix.is_empty((5, 6)) == False
        
        # Test: Check if client position has client
        assert self.matrix.is_contain_type((3, 3), entity_type.client.value) == True
        assert self.matrix.is_contain_type((5, 6), entity_type.player.value) == True

    def test_list_records_performance(self):
        """Test performance con molti record"""
        import time
        
        # Aggiungi 100 record
        start_time = time.time()
        for i in range(100):
            x, y = i % 10, i // 10
            record = ComponentRecord(
                id=i, 
                type=entity_type.player, 
                instance=entity_type.player,
                position=(x, y),

            )
            self.matrix.add_record((x, y), record)
        add_time = time.time() - start_time
        
        # Test list_records performance
        start_time = time.time()
        all_records = self.matrix.list_records()
        list_time = time.time() - start_time
        
        # Test filter performance
        start_time = time.time()
        filtered = self.matrix.filter(component_record_keys.type, entity_type.player)
        filter_time = time.time() - start_time
        
        # Assertions
        assert len(all_records) == 100
        assert len(filtered) == 100
        assert add_time < 1.0  # Dovrebbe essere veloce
        assert list_time < 1.0  # Dovrebbe essere veloce
        assert filter_time < 1.0  # Dovrebbe essere veloce

# ===== ENTRY POINT per esecuzione diretta =====
if __name__ == "__main__":
    # ✅ MODO CORRETTO: Usa pytest.main() per eseguire tutti i test
    pytest.main([__file__, "-v"])