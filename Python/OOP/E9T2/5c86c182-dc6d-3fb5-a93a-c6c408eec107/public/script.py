class Fridge:
    def __init__(self):
        self.contenido = []
        self.inc = 0

    def store(self, item):
        self.contenido.append(item)
        self.sorted_contenido = sorted(self.contenido)
        return self.sorted_contenido

    def take(self, i):
        if i in self.sorted_contenido:
            i_return = self.sorted_contenido.pop(self.sorted_contenido.index(i))
            return i_return
        else:
            raise Warning(f"{i} is not in your fridge, can't be taken out")

    def find(self, name):
        for index, item in enumerate(self.sorted_contenido):
            if item[1] == name:
                return self.sorted_contenido[index]
            else:
                raise Warning

    def take_before_date(self, date):
        return_list = []
        for things in self.sorted_contenido:
            if things[0] < date:
                return_list.append(things)
                self.sorted_contenido.remove(things)
            else:
                pass
        print(self.sorted_contenido)
        return return_list

    def __str__(self):
        return f"I have these items: {self.sorted_contenido}."

    def __iter__(self):
        return self

    def __next__(self):
        if self.inc == len(self):
            self.inc = 0
            raise StopIteration
        self.inc += 1
        return self.sorted_contenido[self.inc - 1]

    def __len__(self):
        return len(self.sorted_contenido)


if __name__ == '__main__':
    l = ["a", "b", "c"]
    for i in l:
        l.remove(i)

    f = Fridge()
    f.store((191127, "Butter"))
    f.store((191117, "Milk"))
    f.store((181117, "Milk"))

    print("Items in the fridge:")
    for i in f:
        print("- {} ({})".format(i[1], i[0]))

    print(f" Items you have to take before : {f.take_before_date(191118)}")
