def make_dfs(number, trie):
    if number not in visited:
        trie[number] = {}
        if len(number) > 1:
            make_dfs(number[1:], trie[number])
            make_dfs(number[:-1], trie[number])

def find_dfs(trie):
    if not trie:
        return 1
    
    result = 0

    for nxt in trie.values():
        result += find_dfs(nxt)

    return result

N = input()
visited = {}

make_dfs(N, visited)
answer = find_dfs(visited)

print(answer)