# metodos comunes para reutilizar en los tests, pero no los que usa el driver

class Utils:

    def assert_list_item_text(self, lista, valor_buscado):
        for i in lista:
            assert i == valor_buscado



