def detect_deadlock(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


def edge_chasing(graph):
    for initiator in graph:
        visited = set()

        def probe(current):
            if current == initiator and current in visited:
                return True

            visited.add(current)

            for neighbor in graph[current]:
                if neighbor not in visited or neighbor == initiator:
                    if probe(neighbor):
                        return True
            return False

        if probe(initiator):
            return True

    return False