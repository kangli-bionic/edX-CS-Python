#Problem 6-3

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
          removes e from self"""
        if e in self.vals.keys():
            self.vals[e] = 0
           
    def is_in(self, e):
        """assumes e is hashable
          returns True if e has been inserted in self and
          not subsequently removed, and False otherwise."""
        if e in self.vals.keys() and self.vals[e] != 0:
            return True
        else:
            return False
