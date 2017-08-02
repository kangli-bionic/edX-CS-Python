#Problem 6-1

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # write code here
        if e in self.vals.keys():
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        if e not in self.vals.keys():
            return 0
        else:
            return self.vals[e]
    def __add__(self, other):
        new_dict = other.vals.copy()  # copy required to prevent updating `other.vals`
        for e in self.vals.keys():
            if e in other.vals.keys():
                new_dict[e] += self.vals[e]
            else:
                new_dict[e] = self.vals[e]

        # Create a new instance and populate it with new_dict
        new_instance = Bag()
        new_instance.vals.update(new_dict)
        return new_instance

    def __str__(self):
        # Use self.vals here not sef.new_dict
        s1 = ""
        for i in sorted(self.vals.keys()):
            s1 += str(i)+":"+str(self.vals[i])+"\n"
        return s1
