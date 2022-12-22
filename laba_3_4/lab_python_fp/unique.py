# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        ignore_case = kwargs.get('ignore_case', False)
        self.items = []
        self.index = 0
        mod_elems = []
        for item in items:
            mod_elem = None
            if ignore_case:
                mod_elem = item.lower() if isinstance(item, str) else item
                if mod_elem in mod_elems:
                    continue
                mod_elems.append(mod_elem)
                self.items.append(item)
            else:
                if item in self.items:
                    continue
                self.items.append(item)

    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            return item
        else:
            self.index = 0
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == "__main__":
    for i in Unique([1, 2, 3, 1, 2, 3]):
        print(i, end=" ")
    print()
    for i in Unique(["a", "A", "B", "b"], ignore_case=True):
        print(i, end=" ")
    print()