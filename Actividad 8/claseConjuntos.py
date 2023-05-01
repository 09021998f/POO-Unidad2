class Conjunto:
    __conj = []

    def __init__(self, conjunto=[]):
        self.__conj = set(conjunto)

    def __repr__(self):
        return str(self.__conj)
    
    def __add__(self, otro):
        return Conjunto(self.__conj.union(otro.__conj))
    
    def __sub__(self, otro):
        resta = Conjunto()
        for i in self.__conj:
            if i not in otro.__conj:
                resta.__conj.add(i)
        return resta
    
    def __eq__(self, otro):
        if len(self.__conj) == len(otro.__conj):
            if sorted(self.__conj) == sorted(otro.__conj):
                return True
            else:
                print('Los elementos son distintos')
                return False
        else:
            print( f'Los conjunto son de distinto tamaño')
            return False
    

