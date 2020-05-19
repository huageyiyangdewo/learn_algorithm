from symbol.symbol_table import SymbolTable


s = SymbolTable()
s.put(1, 1)
s.put(2, 2)
s.put(1, 2)
print(s.num)
print(s.get(1))