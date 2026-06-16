class PincodeTrie:
    def __init__(self):
        self.root = {}

    def insert(self, pincode: str, data: dict = None) -> None:
        node = self.root
        for char in pincode:
            node = node.setdefault(char, {})
        node['$'] = data if data is not None else {}

    def search(self, prefix: str) -> list[tuple[str, dict]]:
        node = self.root
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        
        results = []
        def _dfs(curr: dict, path: str):
            if '$' in curr:
                results.append((path, curr['$']))
            for char, next_node in curr.items():
                if char != '$':
                    _dfs(next_node, path + char)
        
        _dfs(node, prefix)
        return results

if __name__ == "__main__":
    trie = PincodeTrie()
    trie.insert("560001", {"city": "Bengaluru"})
    trie.insert("560002", {"city": "Bengaluru"})
    trie.insert("110001", {"city": "Delhi"})
    
    assert len(trie.search("560")) == 2
    assert trie.search("560001")[0][1]["city"] == "Bengaluru"
    assert len(trie.search("110")) == 1
    assert len(trie.search("999")) == 0
    print("Self-check passed.")
