class TreeStore:
    def __init__(self, array):
        self.array = array

    def getAll(self):
        return self.array

    def getItem(self, id):
        return self.array[id - 1]
items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)

# print(ts.getAll())
print(ts.getItem(7))

# Примеры использования:
#  - ts.getAll() //
#  [{"id":1,"parent":"root"},
#  {"id":2,"parent":1,"type":"test"},
#  {"id":3,"parent":1,"type":"test"},
#  {"id":4,"parent":2,"type":"test"},
#  {"id":5,"parent":2,"type":"test"},
#  {"id":6,"parent":2,"type":"test"},
#  {"id":7,"parent":4,"type":None},
#  {"id":8,"parent":4,"type":None}]
#
#  - ts.getItem(7) // {"id":7,"parent":4,"type":None}
#
#  - ts.getChildren(4) // [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
#  - ts.getChildren(5) // []
#
#  - ts.getAllParents(7) //
#  [{"id":4,"parent":2,"type":"test"},
#  {"id":2,"parent":1,"type":"test"},
#  {"id":1,"parent":"root"}]
