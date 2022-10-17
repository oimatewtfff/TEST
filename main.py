from pprint import pprint


class TreeStore:
    def __init__(self, array):
        self.array = array

    def getAll(self):
        return self.array

    def getItem(self, id):
        for item in self.array:
            if item['id'] == id:
                return item

    def getChildren(self, id):
        result = []
        for item in self.array:
            if item['parent'] == id:
                result.append(item)
        return result

    def getAllParents(self, id, result=[]):
        test = self.getItem(id)['parent']
        if test == 'root':
            return [self.getItem(i) for i in result]
        else:
            result.append(test)
            return self.getAllParents(id=test)


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

pprint(ts.getAll())
pprint(ts.getItem(7))
pprint(ts.getChildren(4))
pprint(ts.getChildren(5))
pprint(ts.getAllParents(7))

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
