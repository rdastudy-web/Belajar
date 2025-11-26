from collections import deque

def topological_sort(graph):
    # 1. Hitung In-Degree untuk setiap Node
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # 2. Inisialisasi Antrean: Masukkan Node dengan In-Degree = 0
    queue = deque([node for node in graph if in_degree[node] == 0])

    # 3. Proses Antrean
    top_order = []
    while queue:
        u = queue.popleft() 
        top_order.append(u) 

        # Kurangi In-Degree dari semua Node tetangga
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # 4. Verifikasi dan Output
    if len(top_order) != len(graph):
        return "Error: Graf ini memiliki siklus, bukan DAG!"
    
    return " -> ".join(top_order)

# --- Contoh Graf (Alur Belajar) ---
course_graph = {
    'A': ['B', 'C'], # A harus selesai sebelum B dan C
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': [],
}

print("Urutan Topologis yang Valid:")
print(topological_sort(course_graph))