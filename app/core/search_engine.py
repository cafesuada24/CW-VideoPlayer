from typing import Sequence

# class Trie:
#     def __init__(self):
#         self._children = dict()
#         self._end_of_word = False
#         self._indexes = set()
#         
#     def insert(self, text: str, index: int):
#         cur = self
#         for c in text:
#             if c not in cur._children:
#                 cur._children[c] = Trie()
#             cur = cur._children[c]
#         cur._end_of_word = True
#         cur._indexes.add(index)
#     
#     def _search_prefix(self, prefix):
#         cur = self
#         for c in prefix:
#             if c not in cur._children:
#                 return None
#             cur = cur._children[c]
#         return cur
#     
#     def _list_all(self, node):
#         found = node._indexes if node._end_of_word else set()
#         for next in node._children.values():
#             found |= self._list_all(next)
#         return found
#     
#     def search_prefix(self, prefix: str) -> tuple[int]:
#         trail_node = self._search_prefix(prefix)
#         if not trail_node: return tuple()
#
#         return tuple(self._list_all(trail_node))

class HashMap:
    def __init__(self):
        self.__data = dict()
    
    def insert(self, text, id):
        if text not in self.__data:
            self.__data[text] = set()
        self.__data[text].add(id)

    def search_prefix(self, prefix: str):
        found = set()
        for key, val in self.__data.items():
            if key.startswith(prefix):
                found |= val
        return found
    
    # def remove(self, text):
    #     if text not in self.__data:
    #         return
        

class SearchEngine:
    def __init__(self, data=None, /, *, data_structure=HashMap):
        self.__ds = data_structure()

        if not data:
            return
        for text, index in data: self.__ds.insert(text, index)
    
    def search_prefix(self, prefix):
        return self.__ds.search_prefix(prefix)
   
if __name__ == '__main__':
    data = ['abc', 'abcde', 'author1', 'author2']
    trie = SearchEngine(zip(data, range(len(data))))
    
    prefixes = ['ab', 'a', 'author', 'author3']

    for prefix in prefixes:
        print(trie.search_prefix(prefix))

