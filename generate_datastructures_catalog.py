"""
Comprehensive Data Structures Catalog Generator
Generates a multi-sheet Excel workbook with detailed information about data structures
across Java, C++, Python, and JavaScript.

Run: python generate_datastructures_catalog.py
Requires: pip install pandas openpyxl
"""

import pandas as pd
from pathlib import Path

# ==============================================================================
# MAIN STRUCTURES CATALOG
# ==============================================================================
structures = [
    # ==================== ARRAY-BASED LINEAR STRUCTURES ====================
    {
        "Category": "Linear - Array Based",
        "Name": "Fixed-size Array",
        "Concept": "Contiguous block of memory with fixed size",
        "Java": "T[] (primitive/object arrays)",
        "C++": "std::array<T,N> or T[]",
        "Python": "array.array() or list",
        "JavaScript": "TypedArray or Array",
        "Access by index": "O(1)",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "O(n)",
        "Insert middle": "O(n)",
        "Insert back": "O(1) if space, O(n) if resize",
        "Delete front": "O(n)",
        "Delete middle": "O(n)",
        "Delete back": "O(1)",
        "Search unsorted": "O(n)",
        "Search sorted": "O(log n)",
        "Memory locality": "Excellent",
        "Memory overhead": "Minimal",
        "Ordered": "Yes (insertion order)",
        "Duplicates": "Yes",
        "Thread-safe": "No",
        "Use cases": "Matrices, buffers, lookup tables, image data, audio samples",
        "Industries": "Embedded systems, games, signal processing, graphics, scientific computing",
        "When to use": "Size known at compile-time; maximum performance needed; memory constrained",
        "When NOT to use": "Size needs to grow dynamically; frequent inserts/deletes except at end"
    },
    {
        "Category": "Linear - Array Based",
        "Name": "Dynamic Array (ArrayList/Vector)",
        "Concept": "Resizable array with amortized growth",
        "Java": "ArrayList<E>",
        "C++": "std::vector<T>",
        "Python": "list",
        "JavaScript": "Array",
        "Access by index": "O(1)",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "O(n)",
        "Insert middle": "O(n)",
        "Insert back": "Amortized O(1)",
        "Delete front": "O(n)",
        "Delete middle": "O(n)",
        "Delete back": "O(1)",
        "Search unsorted": "O(n)",
        "Search sorted": "O(log n)",
        "Memory locality": "Excellent",
        "Memory overhead": "Low (~1.5-2x capacity)",
        "Ordered": "Yes",
        "Duplicates": "Yes",
        "Thread-safe": "No",
        "Use cases": "General collections, stacks, buffers, dynamic sequences",
        "Industries": "All software development",
        "When to use": "Default choice for sequential data; random access needed; mostly appending",
        "When NOT to use": "Frequent insert/delete at start or middle"
    },
    {
        "Category": "Linear - Array Based",
        "Name": "Deque (Double-Ended Queue)",
        "Concept": "Efficient operations at both ends",
        "Java": "ArrayDeque<E>",
        "C++": "std::deque<T>",
        "Python": "collections.deque",
        "JavaScript": "Custom implementation",
        "Access by index": "O(1)",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "O(1)",
        "Insert middle": "O(n)",
        "Insert back": "O(1)",
        "Delete front": "O(1)",
        "Delete middle": "O(n)",
        "Delete back": "O(1)",
        "Search unsorted": "O(n)",
        "Search sorted": "O(n)",
        "Memory locality": "Good",
        "Memory overhead": "Moderate",
        "Ordered": "Yes",
        "Duplicates": "Yes",
        "Thread-safe": "No",
        "Use cases": "Task queues, sliding windows, BFS, work stealing",
        "Industries": "OS, schedulers, algorithms, game engines",
        "When to use": "Need efficient operations at both ends; implementing queues/stacks",
        "When NOT to use": "Only appending to one end; frequent middle insertions"
    },
    
    # ==================== LINKED STRUCTURES ====================
    {
        "Category": "Linear - Linked",
        "Name": "Singly Linked List",
        "Concept": "Nodes with next pointer only",
        "Java": "Custom (LinkedList is doubly)",
        "C++": "std::forward_list<T>",
        "Python": "Custom",
        "JavaScript": "Custom",
        "Access by index": "O(n)",
        "Access front": "O(1)",
        "Access back": "O(n) or O(1) with tail",
        "Insert front": "O(1)",
        "Insert middle": "O(1) at position, O(n) to find",
        "Insert back": "O(n) or O(1) with tail",
        "Delete front": "O(1)",
        "Delete middle": "O(1) at position, O(n) to find",
        "Delete back": "O(n)",
        "Search unsorted": "O(n)",
        "Search sorted": "O(n)",
        "Memory locality": "Poor",
        "Memory overhead": "One pointer per node",
        "Ordered": "Yes",
        "Duplicates": "Yes",
        "Thread-safe": "No",
        "Use cases": "Simple queues, adjacency lists, memory-constrained insertions",
        "Industries": "Networking, OS, embedded systems",
        "When to use": "Memory fragmented; only forward traversal; insertions at known positions",
        "When NOT to use": "Random access needed; backward traversal; cache performance matters"
    },
    {
        "Category": "Linear - Linked",
        "Name": "Doubly Linked List",
        "Concept": "Nodes with next and previous pointers",
        "Java": "LinkedList<E>",
        "C++": "std::list<T>",
        "Python": "Custom",
        "JavaScript": "Custom",
        "Access by index": "O(n)",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "O(1)",
        "Insert middle": "O(1) at position, O(n) to find",
        "Insert back": "O(1)",
        "Delete front": "O(1)",
        "Delete middle": "O(1) at position, O(n) to find",
        "Delete back": "O(1)",
        "Search unsorted": "O(n)",
        "Search sorted": "O(n)",
        "Memory locality": "Poor",
        "Memory overhead": "Two pointers per node",
        "Ordered": "Yes",
        "Duplicates": "Yes",
        "Thread-safe": "No",
        "Use cases": "LRU caches, browser history, playlists, undo/redo",
        "Industries": "OS, memory allocators, databases, GUI",
        "When to use": "O(1) insert/delete at known positions; bidirectional traversal; splice ops",
        "When NOT to use": "Random access frequent; memory locality important"
    },
    
    # ==================== HASH-BASED STRUCTURES ====================
    {
        "Category": "Hash-based - Set",
        "Name": "Hash Set",
        "Concept": "Unique elements using hash table",
        "Java": "HashSet<E>",
        "C++": "std::unordered_set<T>",
        "Python": "set",
        "JavaScript": "Set",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(1) avg",
        "Insert back": "O(1) avg",
        "Delete front": "N/A",
        "Delete middle": "O(1) avg by value",
        "Delete back": "O(1) avg by value",
        "Search unsorted": "O(1) avg, O(n) worst",
        "Search sorted": "N/A",
        "Memory locality": "Poor",
        "Memory overhead": "Hash table + load factor",
        "Ordered": "No",
        "Duplicates": "No",
        "Thread-safe": "No",
        "Use cases": "Deduplication, membership testing, unique elements, graph vertices",
        "Industries": "Web apps, data processing, ETL, analytics",
        "When to use": "Fast membership checks; order doesn't matter; removing duplicates",
        "When NOT to use": "Need ordering; retrieve by index; duplicates needed"
    },
    {
        "Category": "Hash-based - Map",
        "Name": "Hash Map",
        "Concept": "Key-value pairs with hash table",
        "Java": "HashMap<K,V>",
        "C++": "std::unordered_map<K,V>",
        "Python": "dict",
        "JavaScript": "Map or Object",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(1) avg",
        "Insert back": "O(1) avg",
        "Delete front": "N/A",
        "Delete middle": "O(1) avg by key",
        "Delete back": "O(1) avg by key",
        "Search unsorted": "O(1) avg by key",
        "Search sorted": "N/A",
        "Memory locality": "Poor",
        "Memory overhead": "Buckets + chains/probing",
        "Ordered": "No",
        "Duplicates": "No duplicate keys",
        "Thread-safe": "No",
        "Use cases": "Caching, dictionaries, frequencies, memoization, indexing",
        "Industries": "All industries - most common",
        "When to use": "Default for key-value; fast lookups; order doesn't matter",
        "When NOT to use": "Need sorted keys; iteration order important"
    },
    {
        "Category": "Hash-based - Map",
        "Name": "Linked Hash Map",
        "Concept": "Hash map maintaining insertion order",
        "Java": "LinkedHashMap<K,V>",
        "C++": "Custom",
        "Python": "dict (3.7+)",
        "JavaScript": "Map",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(1) avg",
        "Insert back": "O(1) avg",
        "Delete front": "N/A",
        "Delete middle": "O(1) avg by key",
        "Delete back": "O(1) avg by key",
        "Search unsorted": "O(1) avg by key",
        "Search sorted": "N/A",
        "Memory locality": "Poor",
        "Memory overhead": "HashMap + linked list",
        "Ordered": "Yes (insertion)",
        "Duplicates": "No duplicate keys",
        "Thread-safe": "No",
        "Use cases": "LRU cache, preserving order, access tracking",
        "Industries": "Caching, web servers, frameworks",
        "When to use": "HashMap + predictable iteration; LRU caches",
        "When NOT to use": "Order doesn't matter; memory overhead critical"
    },
    
    # ==================== TREE-BASED STRUCTURES ====================
    {
        "Category": "Tree - Balanced BST",
        "Name": "Red-Black Tree (Set)",
        "Concept": "Self-balancing BST with color rules",
        "Java": "TreeSet<E>",
        "C++": "std::set<T>",
        "Python": "sortedcontainers.SortedSet",
        "JavaScript": "Custom",
        "Access by index": "N/A",
        "Access front": "O(log n)",
        "Access back": "O(log n)",
        "Insert front": "O(log n)",
        "Insert middle": "O(log n)",
        "Insert back": "O(log n)",
        "Delete front": "O(log n)",
        "Delete middle": "O(log n)",
        "Delete back": "O(log n)",
        "Search unsorted": "N/A",
        "Search sorted": "O(log n)",
        "Memory locality": "Poor",
        "Memory overhead": "Pointers + color bit",
        "Ordered": "Yes (sorted)",
        "Duplicates": "No",
        "Thread-safe": "No",
        "Use cases": "Sorted collections, range queries, order statistics",
        "Industries": "Databases, OS, compilers, finance",
        "When to use": "Need sorted unique elements; range queries; worst-case O(log n)",
        "When NOT to use": "Hash table's O(1) avg sufficient; memory overhead matters"
    },
    {
        "Category": "Tree - Balanced BST",
        "Name": "Red-Black Tree (Map)",
        "Concept": "Self-balancing BST for key-value pairs",
        "Java": "TreeMap<K,V>",
        "C++": "std::map<K,V>",
        "Python": "sortedcontainers.SortedDict",
        "JavaScript": "Custom",
        "Access by index": "N/A",
        "Access front": "O(log n)",
        "Access back": "O(log n)",
        "Insert front": "O(log n)",
        "Insert middle": "O(log n)",
        "Insert back": "O(log n)",
        "Delete front": "O(log n)",
        "Delete middle": "O(log n)",
        "Delete back": "O(log n)",
        "Search unsorted": "N/A",
        "Search sorted": "O(log n)",
        "Memory locality": "Poor",
        "Memory overhead": "Tree nodes",
        "Ordered": "Yes (by key)",
        "Duplicates": "No duplicate keys",
        "Thread-safe": "No",
        "Use cases": "Ordered dictionaries, interval trees, range maps",
        "Industries": "Databases, finance, scheduling",
        "When to use": "Need sorted keys; ceiling/floor ops; range queries",
        "When NOT to use": "HashMap performance adequate; order doesn't matter"
    },
    {
        "Category": "Tree - Specialized",
        "Name": "B-Tree",
        "Concept": "Multi-key nodes optimized for disk",
        "Java": "Custom or DB libraries",
        "C++": "Custom or Boost",
        "Python": "Custom or DB libraries",
        "JavaScript": "Custom",
        "Access by index": "N/A",
        "Access front": "O(log n)",
        "Access back": "O(log n)",
        "Insert front": "O(log n)",
        "Insert middle": "O(log n)",
        "Insert back": "O(log n)",
        "Delete front": "O(log n)",
        "Delete middle": "O(log n)",
        "Delete back": "O(log n)",
        "Search unsorted": "N/A",
        "Search sorted": "O(log n) fewer seeks",
        "Memory locality": "Excellent within node",
        "Memory overhead": "Moderate",
        "Ordered": "Yes (sorted)",
        "Duplicates": "Typically no",
        "Thread-safe": "Depends",
        "Use cases": "Database indexes, file systems, disk structures",
        "Industries": "Databases (MySQL, PostgreSQL), file systems",
        "When to use": "Disk-based storage; minimize disk I/O; database indexes",
        "When NOT to use": "In-memory structures; nodes don't align with blocks"
    },
    {
        "Category": "Tree - Specialized",
        "Name": "Trie (Prefix Tree)",
        "Concept": "Character-based tree for strings",
        "Java": "Custom",
        "C++": "Custom",
        "Python": "pygtrie or custom",
        "JavaScript": "Custom",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(m) where m=key length",
        "Insert back": "O(m)",
        "Delete front": "N/A",
        "Delete middle": "O(m)",
        "Delete back": "O(m)",
        "Search unsorted": "N/A",
        "Search sorted": "O(m) prefix search",
        "Memory locality": "Poor",
        "Memory overhead": "High",
        "Ordered": "Lexicographic",
        "Duplicates": "No",
        "Thread-safe": "No",
        "Use cases": "Autocomplete, spell check, IP routing, dictionaries, DNA analysis",
        "Industries": "Search engines, networking, bioinformatics, text editors",
        "When to use": "Prefix searches; autocomplete; keys share prefixes; lexicographic ops",
        "When NOT to use": "Keys random; simple hash map works; small datasets"
    },
    {
        "Category": "Tree - Specialized",
        "Name": "Segment Tree",
        "Concept": "Binary tree for range queries",
        "Java": "Custom",
        "C++": "Custom",
        "Python": "Custom",
        "JavaScript": "Custom",
        "Access by index": "O(log n) range",
        "Access front": "O(1) if cached",
        "Access back": "O(1) if cached",
        "Insert front": "O(log n) update",
        "Insert middle": "O(log n) update",
        "Insert back": "O(log n) update",
        "Delete front": "O(log n) update",
        "Delete middle": "O(log n) update",
        "Delete back": "O(log n) update",
        "Search unsorted": "N/A",
        "Search sorted": "O(log n) range query",
        "Memory locality": "Moderate",
        "Memory overhead": "~4n space",
        "Ordered": "Implicit by index",
        "Duplicates": "N/A",
        "Thread-safe": "No",
        "Use cases": "Range min/max/sum, computational geometry, scheduling",
        "Industries": "Competitive programming, graphics, analytics",
        "When to use": "Range queries with updates; interval problems; efficient query+update",
        "When NOT to use": "Static arrays (prefix sum works); only point queries"
    },
    
    # ==================== HEAP STRUCTURES ====================
    {
        "Category": "Heap",
        "Name": "Binary Heap (Priority Queue)",
        "Concept": "Complete binary tree, array-based",
        "Java": "PriorityQueue<E>",
        "C++": "std::priority_queue<T>",
        "Python": "heapq",
        "JavaScript": "Custom",
        "Access by index": "N/A",
        "Access front": "O(1) peek min/max",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(log n)",
        "Insert back": "O(log n)",
        "Delete front": "O(log n) extract",
        "Delete middle": "O(n) find + O(log n) delete",
        "Delete back": "N/A",
        "Search unsorted": "O(n)",
        "Search sorted": "N/A",
        "Memory locality": "Excellent",
        "Memory overhead": "Minimal",
        "Ordered": "Partial (heap order)",
        "Duplicates": "Yes",
        "Thread-safe": "No",
        "Use cases": "Priority queues, scheduling, Dijkstra, heap sort, median",
        "Industries": "OS (scheduling), simulations, graph algorithms",
        "When to use": "Need min/max efficiently; priority processing; k-largest/smallest",
        "When NOT to use": "Need full sorting; search by value; FIFO queues"
    },
    
    # ==================== GRAPH STRUCTURES ====================
    {
        "Category": "Graph",
        "Name": "Adjacency List",
        "Concept": "Array/map of neighbor lists per vertex",
        "Java": "List<List<Integer>>",
        "C++": "vector<vector<int>>",
        "Python": "list of lists or dict",
        "JavaScript": "Array of Arrays or Map",
        "Access by index": "O(1) vertex list",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "O(1) add vertex",
        "Insert middle": "O(1) add edge",
        "Insert back": "O(1) add edge",
        "Delete front": "O(V+E) remove vertex",
        "Delete middle": "O(degree) remove edge",
        "Delete back": "O(degree) remove edge",
        "Search unsorted": "O(degree) edge check",
        "Search sorted": "O(log degree) if sorted",
        "Memory locality": "Good for iteration",
        "Memory overhead": "O(V+E) optimal",
        "Ordered": "No",
        "Duplicates": "Can represent multi-edges",
        "Thread-safe": "No",
        "Use cases": "Graph algorithms (DFS, BFS), social networks, dependencies",
        "Industries": "Social media, routing, compilers, recommendations",
        "When to use": "Default for graphs; sparse graphs; iterating neighbors",
        "When NOT to use": "Dense graphs; edge existence checks critical"
    },
    {
        "Category": "Graph",
        "Name": "Adjacency Matrix",
        "Concept": "2D array for edge representation",
        "Java": "boolean[][] or int[][]",
        "C++": "vector<vector<bool>>",
        "Python": "2D list or numpy array",
        "JavaScript": "2D Array",
        "Access by index": "O(1) edge check",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "O(V²) add vertex",
        "Insert middle": "O(1) add edge",
        "Insert back": "O(1) add edge",
        "Delete front": "O(V²) remove vertex",
        "Delete middle": "O(1) remove edge",
        "Delete back": "O(1) remove edge",
        "Search unsorted": "O(1) edge, O(V) neighbors",
        "Search sorted": "N/A",
        "Memory locality": "Excellent for dense",
        "Memory overhead": "O(V²) always",
        "Ordered": "Implicit by index",
        "Duplicates": "No",
        "Thread-safe": "No",
        "Use cases": "Dense graphs, Floyd-Warshall, game boards, grids",
        "Industries": "Game dev, network analysis, optimization",
        "When to use": "Dense graphs; O(1) edge check critical; matrix algorithms",
        "When NOT to use": "Sparse graphs; iterating neighbors frequently"
    },
    
    # ==================== SPECIALIZED STRUCTURES ====================
    {
        "Category": "Specialized",
        "Name": "Bloom Filter",
        "Concept": "Probabilistic set with false positives",
        "Java": "Guava BloomFilter",
        "C++": "Boost or custom",
        "Python": "pybloom or custom",
        "JavaScript": "bloomfilter.js",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(k) add, k=hash funcs",
        "Insert back": "O(k)",
        "Delete front": "N/A (no deletion)",
        "Delete middle": "N/A",
        "Delete back": "N/A",
        "Search unsorted": "O(k) probabilistic",
        "Search sorted": "N/A",
        "Memory locality": "Good",
        "Memory overhead": "Very low (bits)",
        "Ordered": "No",
        "Duplicates": "Implicit",
        "Thread-safe": "Can be",
        "Use cases": "Cache filtering, spell check, deduplication, DB optimization",
        "Industries": "Databases (Cassandra), web crawlers, CDNs, blockchain",
        "When to use": "Space premium; false positives OK; quick membership",
        "When NOT to use": "False positives unacceptable; deletions needed; exact counting"
    },
    {
        "Category": "Specialized",
        "Name": "Disjoint Set (Union-Find)",
        "Concept": "Track disjoint set partitions",
        "Java": "Custom",
        "C++": "Custom",
        "Python": "Custom",
        "JavaScript": "Custom",
        "Access by index": "O(α(n)) find",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "O(α(n)) union",
        "Insert middle": "O(α(n)) union",
        "Insert back": "O(α(n)) union",
        "Delete front": "N/A (no delete)",
        "Delete middle": "N/A",
        "Delete back": "N/A",
        "Search unsorted": "O(α(n)) connected",
        "Search sorted": "N/A",
        "Memory locality": "Good",
        "Memory overhead": "O(n) parent array",
        "Ordered": "No",
        "Duplicates": "N/A",
        "Thread-safe": "No",
        "Use cases": "Kruskal MST, cycle detection, connected components, segmentation",
        "Industries": "Graph algorithms, networks, image processing, social networks",
        "When to use": "Connectivity queries; Kruskal; dynamic grouping",
        "When NOT to use": "Deletions needed; full graph structure required"
    },
    {
        "Category": "Specialized",
        "Name": "LRU Cache",
        "Concept": "HashMap + doubly-linked list for LRU",
        "Java": "LinkedHashMap",
        "C++": "Custom (list + unordered_map)",
        "Python": "functools.lru_cache or custom",
        "JavaScript": "Custom (Map + list)",
        "Access by index": "N/A",
        "Access front": "O(1) most recent",
        "Access back": "O(1) least recent",
        "Insert front": "O(1) put",
        "Insert middle": "O(1) put",
        "Insert back": "O(1) put",
        "Delete front": "O(1) evict LRU",
        "Delete middle": "O(1) remove by key",
        "Delete back": "O(1)",
        "Search unsorted": "O(1) by key",
        "Search sorted": "N/A",
        "Memory locality": "Moderate",
        "Memory overhead": "HashMap + list pointers",
        "Ordered": "Access order",
        "Duplicates": "No",
        "Thread-safe": "No",
        "Use cases": "Caching, memoization, browser history, DB buffers",
        "Industries": "Web servers, databases, OS, CDNs",
        "When to use": "Caching with size limit; LRU eviction makes sense",
        "When NOT to use": "Other eviction policies needed; unlimited caches"
    },
    {
        "Category": "Specialized",
        "Name": "Skip List",
        "Concept": "Probabilistic multi-level linked lists",
        "Java": "ConcurrentSkipListMap/Set",
        "C++": "Custom or Boost",
        "Python": "Custom",
        "JavaScript": "Custom",
        "Access by index": "O(log n) avg",
        "Access front": "O(1)",
        "Access back": "O(1) if tail",
        "Insert front": "O(log n)",
        "Insert middle": "O(log n) avg",
        "Insert back": "O(log n)",
        "Delete front": "O(log n)",
        "Delete middle": "O(log n) avg",
        "Delete back": "O(log n)",
        "Search unsorted": "N/A",
        "Search sorted": "O(log n) avg",
        "Memory locality": "Poor",
        "Memory overhead": "Multiple pointers",
        "Ordered": "Yes (sorted)",
        "Duplicates": "Typically no",
        "Thread-safe": "Java impl is lock-free",
        "Use cases": "Concurrent sorted maps, DB indexes, in-memory DBs",
        "Industries": "Databases (Redis), concurrent systems",
        "When to use": "Concurrent sorted map; simpler than balanced trees; lock-free",
        "When NOT to use": "Memory overhead concern; deterministic performance required"
    },
    
    # ==================== QUEUE/STACK STRUCTURES ====================
    {
        "Category": "Linear - Stack/Queue",
        "Name": "Stack (LIFO)",
        "Concept": "Last-In-First-Out collection",
        "Java": "Stack<E> or ArrayDeque<E>",
        "C++": "std::stack<T>",
        "Python": "list (use append/pop)",
        "JavaScript": "Array (push/pop)",
        "Access by index": "N/A",
        "Access front": "O(1) peek top",
        "Access back": "N/A",
        "Insert front": "O(1) push",
        "Insert middle": "N/A",
        "Insert back": "N/A",
        "Delete front": "O(1) pop",
        "Delete middle": "N/A",
        "Delete back": "N/A",
        "Search unsorted": "O(n)",
        "Search sorted": "N/A",
        "Memory locality": "Excellent (array-based)",
        "Memory overhead": "Minimal",
        "Ordered": "LIFO order",
        "Duplicates": "Yes",
        "Thread-safe": "No (use ConcurrentLinkedDeque)",
        "Use cases": "Function call stack, expression evaluation, backtracking, undo/redo",
        "Industries": "Compilers, browsers, text editors, algorithms",
        "When to use": "LIFO semantics needed; parsing; depth-first traversal",
        "When NOT to use": "Need FIFO; need to access middle elements; random access required"
    },
    {
        "Category": "Linear - Stack/Queue",
        "Name": "Queue (FIFO)",
        "Concept": "First-In-First-Out collection",
        "Java": "Queue<E> interface (LinkedList, ArrayDeque)",
        "C++": "std::queue<T>",
        "Python": "collections.deque or queue.Queue",
        "JavaScript": "Array (push/shift) or custom",
        "Access by index": "N/A",
        "Access front": "O(1) peek",
        "Access back": "O(1) peek rear",
        "Insert front": "N/A",
        "Insert middle": "N/A",
        "Insert back": "O(1) enqueue",
        "Delete front": "O(1) dequeue",
        "Delete middle": "N/A",
        "Delete back": "N/A",
        "Search unsorted": "O(n)",
        "Search sorted": "N/A",
        "Memory locality": "Good (circular buffer impl)",
        "Memory overhead": "Low",
        "Ordered": "FIFO order",
        "Duplicates": "Yes",
        "Thread-safe": "No (use ArrayBlockingQueue)",
        "Use cases": "Task scheduling, BFS, request handling, print spooling, buffering",
        "Industries": "Operating systems, web servers, messaging systems, simulations",
        "When to use": "FIFO processing; breadth-first traversal; producer-consumer",
        "When NOT to use": "Need LIFO; need priority-based access; random access needed"
    },
    {
        "Category": "Linear - Stack/Queue",
        "Name": "Circular Buffer (Ring Buffer)",
        "Concept": "Fixed-size buffer with wrap-around",
        "Java": "Custom or ArrayBlockingQueue",
        "C++": "boost::circular_buffer",
        "Python": "collections.deque with maxlen",
        "JavaScript": "Custom implementation",
        "Access by index": "O(1)",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "O(1)",
        "Insert middle": "N/A",
        "Insert back": "O(1)",
        "Delete front": "O(1)",
        "Delete middle": "N/A",
        "Delete back": "O(1)",
        "Search unsorted": "O(n)",
        "Search sorted": "N/A",
        "Memory locality": "Excellent (contiguous)",
        "Memory overhead": "Fixed size overhead",
        "Ordered": "Yes (insertion order)",
        "Duplicates": "Yes",
        "Thread-safe": "Can be (with synchronization)",
        "Use cases": "Audio/video buffering, logging systems, streaming data, fixed-size caches",
        "Industries": "Media streaming, embedded systems, real-time systems, networking",
        "When to use": "Fixed memory constraint; streaming data; overwrite old data automatically",
        "When NOT to use": "Need dynamic size; need to preserve all historical data"
    },
    
    # ==================== TREE VARIANTS ====================
    {
        "Category": "Tree - Specialized",
        "Name": "AVL Tree",
        "Concept": "Strictly height-balanced BST",
        "Java": "Custom or Apache Commons",
        "C++": "Custom implementation",
        "Python": "Custom or bintrees library",
        "JavaScript": "Custom implementation",
        "Access by index": "N/A",
        "Access front": "O(log n)",
        "Access back": "O(log n)",
        "Insert front": "O(log n)",
        "Insert middle": "O(log n)",
        "Insert back": "O(log n)",
        "Delete front": "O(log n)",
        "Delete middle": "O(log n)",
        "Delete back": "O(log n)",
        "Search unsorted": "N/A",
        "Search sorted": "O(log n)",
        "Memory locality": "Poor",
        "Memory overhead": "Height/balance factor per node",
        "Ordered": "Yes (sorted)",
        "Duplicates": "Depends on implementation",
        "Thread-safe": "No",
        "Use cases": "Databases with read-heavy workloads, in-memory indexes, sorted data with frequent lookups",
        "Industries": "Databases, search systems, compilers",
        "When to use": "Lookups more frequent than insertions; strict balancing needed",
        "When NOT to use": "Write-heavy workload (RB tree better); memory constrained"
    },
    {
        "Category": "Tree - Specialized",
        "Name": "Suffix Tree",
        "Concept": "Compressed trie of all suffixes",
        "Java": "Custom implementation",
        "C++": "Custom implementation",
        "Python": "suffix-tree library",
        "JavaScript": "Custom implementation",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "O(n) construction",
        "Insert middle": "O(n) for dynamic",
        "Insert back": "O(n) construction",
        "Delete front": "Complex",
        "Delete middle": "Complex",
        "Delete back": "Complex",
        "Search unsorted": "O(m) pattern search",
        "Search sorted": "O(m) pattern search",
        "Memory locality": "Poor",
        "Memory overhead": "O(n) nodes",
        "Ordered": "N/A",
        "Duplicates": "N/A",
        "Thread-safe": "No",
        "Use cases": "Pattern matching, bioinformatics, longest common substring, plagiarism detection",
        "Industries": "Bioinformatics, search engines, text analysis, data compression",
        "When to use": "Multiple pattern searches; substring problems; DNA sequence analysis",
        "When NOT to use": "Small texts; simple pattern matching; construction cost too high"
    },
    {
        "Category": "Tree - Specialized",
        "Name": "Fenwick Tree (BIT)",
        "Concept": "Binary Indexed Tree for prefix queries",
        "Java": "Custom implementation",
        "C++": "Custom implementation",
        "Python": "Custom implementation",
        "JavaScript": "Custom implementation",
        "Access by index": "O(log n) prefix query",
        "Access front": "O(log n)",
        "Access back": "O(log n)",
        "Insert front": "O(log n) point update",
        "Insert middle": "O(log n) point update",
        "Insert back": "O(log n) point update",
        "Delete front": "O(log n) point update",
        "Delete middle": "O(log n) point update",
        "Delete back": "O(log n) point update",
        "Search unsorted": "N/A",
        "Search sorted": "O(log n) prefix sum",
        "Memory locality": "Excellent (array-based)",
        "Memory overhead": "O(n) - same as input",
        "Ordered": "Implicit by index",
        "Duplicates": "N/A",
        "Thread-safe": "No",
        "Use cases": "Cumulative frequency, range sum queries, inversion counting, order statistics",
        "Industries": "Competitive programming, analytics, time-series analysis",
        "When to use": "Prefix sum queries with updates; simpler than segment tree",
        "When NOT to use": "Need complex range updates (use segment tree); static queries only"
    },
    
    # ==================== ADDITIONAL SPECIALIZED ====================
    {
        "Category": "Specialized",
        "Name": "BitSet / Bit Vector",
        "Concept": "Compact array of bits",
        "Java": "BitSet",
        "C++": "std::bitset<N> or std::vector<bool>",
        "Python": "bitarray library or int operations",
        "JavaScript": "Typed arrays or custom",
        "Access by index": "O(1)",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "N/A (fixed size typically)",
        "Insert middle": "O(1) set bit",
        "Insert back": "O(1) set bit",
        "Delete front": "N/A",
        "Delete middle": "O(1) clear bit",
        "Delete back": "O(1) clear bit",
        "Search unsorted": "O(n) scan bits",
        "Search sorted": "O(n) find next set",
        "Memory locality": "Excellent",
        "Memory overhead": "Minimal (1 bit per flag)",
        "Ordered": "Implicit by position",
        "Duplicates": "N/A",
        "Thread-safe": "No",
        "Use cases": "Flags, permissions, Sieve of Eratosthenes, compression, state tracking",
        "Industries": "Systems programming, compression, networking, algorithms",
        "When to use": "Boolean flags; memory critical; set operations on integers; bitmasks",
        "When NOT to use": "Sparse sets (hash set better); need complex per-element data"
    },
    {
        "Category": "Specialized",
        "Name": "Sparse Table",
        "Concept": "Precomputed table for immutable range queries",
        "Java": "Custom implementation",
        "C++": "Custom implementation",
        "Python": "Custom implementation",
        "JavaScript": "Custom implementation",
        "Access by index": "O(1) range query",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "N/A (static)",
        "Insert middle": "N/A (static)",
        "Insert back": "N/A (static)",
        "Delete front": "N/A",
        "Delete middle": "N/A",
        "Delete back": "N/A",
        "Search unsorted": "N/A",
        "Search sorted": "O(1) range min/max query",
        "Memory locality": "Good",
        "Memory overhead": "O(n log n) space",
        "Ordered": "N/A",
        "Duplicates": "N/A",
        "Thread-safe": "Yes (immutable)",
        "Use cases": "Static range min/max/GCD queries, lowest common ancestor, immutable data analysis",
        "Industries": "Competitive programming, scientific computing, data analysis",
        "When to use": "Static data; many range queries; O(1) query time needed",
        "When NOT to use": "Data changes (use segment tree); space is constrained"
    },
    {
        "Category": "Specialized",
        "Name": "Count-Min Sketch",
        "Concept": "Probabilistic frequency counting",
        "Java": "stream-lib or Guava",
        "C++": "Custom implementation",
        "Python": "countminsketch library",
        "JavaScript": "Custom implementation",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(k) increment (k hash functions)",
        "Insert back": "O(k) increment",
        "Delete front": "N/A (count-only variant)",
        "Delete middle": "O(k) decrement (conservative update)",
        "Delete back": "N/A",
        "Search unsorted": "O(k) frequency estimate",
        "Search sorted": "N/A",
        "Memory locality": "Good",
        "Memory overhead": "Very low (sublinear)",
        "Ordered": "No",
        "Duplicates": "Counts frequencies",
        "Thread-safe": "Can be",
        "Use cases": "Heavy hitters, frequency estimation in streams, network traffic analysis",
        "Industries": "Big data analytics, network monitoring, streaming systems",
        "When to use": "Massive streams; approximate counts acceptable; memory constrained",
        "When NOT to use": "Exact counts required; small datasets (use HashMap)"
    },
    {
        "Category": "Specialized",
        "Name": "HyperLogLog",
        "Concept": "Probabilistic cardinality estimation",
        "Java": "stream-lib or Guava",
        "C++": "Custom or Redis implementation",
        "Python": "hyperloglog library",
        "JavaScript": "Custom implementation",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(1) add element",
        "Insert back": "O(1) add element",
        "Delete front": "N/A (no deletion)",
        "Delete middle": "N/A",
        "Delete back": "N/A",
        "Search unsorted": "O(1) cardinality estimate",
        "Search sorted": "N/A",
        "Memory locality": "Excellent",
        "Memory overhead": "Very low (fixed small size)",
        "Ordered": "No",
        "Duplicates": "Automatically handled",
        "Thread-safe": "Can be",
        "Use cases": "Unique visitor counting, distinct value estimation, database query optimization",
        "Industries": "Web analytics, databases (Redis), big data systems",
        "When to use": "Count distinct elements in huge datasets; memory extremely limited; approximate OK",
        "When NOT to use": "Exact count required; small datasets (use HashSet)"
    },
    {
        "Category": "Specialized",
        "Name": "Cuckoo Filter",
        "Concept": "Space-efficient probabilistic set with deletion support",
        "Java": "Custom implementation",
        "C++": "libcuckoo",
        "Python": "Custom implementation",
        "JavaScript": "Custom implementation",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(1) avg insert",
        "Insert back": "O(1) avg insert",
        "Delete front": "N/A",
        "Delete middle": "O(1) delete",
        "Delete back": "N/A",
        "Search unsorted": "O(1) membership test",
        "Search sorted": "N/A",
        "Memory locality": "Good",
        "Memory overhead": "Very low",
        "Ordered": "No",
        "Duplicates": "Limited support",
        "Thread-safe": "Can be",
        "Use cases": "Like Bloom filter but with deletion, deduplication, cache filtering",
        "Industries": "Databases, networking, distributed systems",
        "When to use": "Need deletion support that Bloom filter lacks; space-efficient membership",
        "When NOT to use": "Exact membership required; unlimited insertions expected"
    },
    
    # ==================== SPATIAL STRUCTURES ====================
    {
        "Category": "Spatial",
        "Name": "KD-Tree",
        "Concept": "k-dimensional space partitioning tree",
        "Java": "Custom or JTS library",
        "C++": "Custom or CGAL",
        "Python": "scipy.spatial.KDTree",
        "JavaScript": "Custom implementation",
        "Access by index": "N/A",
        "Access front": "O(log n) avg nearest neighbor",
        "Access back": "N/A",
        "Insert front": "O(log n) avg",
        "Insert middle": "O(log n) avg",
        "Insert back": "O(log n) avg",
        "Delete front": "O(log n) avg",
        "Delete middle": "O(log n) avg",
        "Delete back": "O(log n) avg",
        "Search unsorted": "O(log n) avg nearest neighbor",
        "Search sorted": "N/A",
        "Memory locality": "Poor",
        "Memory overhead": "Tree nodes",
        "Ordered": "Spatial ordering",
        "Duplicates": "Depends",
        "Thread-safe": "No",
        "Use cases": "Nearest neighbor search, range search, point location, clustering",
        "Industries": "GIS, machine learning, computer graphics, robotics",
        "When to use": "Low dimensions (<20); nearest neighbor queries; spatial indexing",
        "When NOT to use": "High dimensions (curse of dimensionality); dynamic data with many updates"
    },
    {
        "Category": "Spatial",
        "Name": "Quadtree",
        "Concept": "2D space partitioning tree",
        "Java": "Custom implementation",
        "C++": "Custom implementation",
        "Python": "pyqtree library",
        "JavaScript": "Custom implementation",
        "Access by index": "O(log n) avg",
        "Access front": "O(log n)",
        "Access back": "O(log n)",
        "Insert front": "O(log n) avg",
        "Insert middle": "O(log n) avg",
        "Insert back": "O(log n) avg",
        "Delete front": "O(log n) avg",
        "Delete middle": "O(log n) avg",
        "Delete back": "O(log n) avg",
        "Search unsorted": "O(log n) avg region query",
        "Search sorted": "N/A",
        "Memory locality": "Poor",
        "Memory overhead": "4 children per internal node",
        "Ordered": "Spatial quadrants",
        "Duplicates": "Depends",
        "Thread-safe": "No",
        "Use cases": "Image processing, collision detection, spatial indexing, map rendering",
        "Industries": "Game development, GIS, computer graphics, simulations",
        "When to use": "2D spatial data; hierarchical subdivision; range queries in 2D",
        "When NOT to use": "1D or 3D data; uniform grid sufficient; very dynamic data"
    },
    {
        "Category": "Spatial",
        "Name": "R-Tree",
        "Concept": "Tree for indexing spatial rectangles",
        "Java": "JTS or custom",
        "C++": "Boost.Geometry or libspatialindex",
        "Python": "rtree library",
        "JavaScript": "rbush library",
        "Access by index": "O(log n) avg",
        "Access front": "O(log n)",
        "Access back": "O(log n)",
        "Insert front": "O(log n) avg",
        "Insert middle": "O(log n) avg",
        "Insert back": "O(log n) avg",
        "Delete front": "O(log n) avg",
        "Delete middle": "O(log n) avg",
        "Delete back": "O(log n) avg",
        "Search unsorted": "O(log n) avg range query",
        "Search sorted": "N/A",
        "Memory locality": "Moderate",
        "Memory overhead": "Bounding boxes per node",
        "Ordered": "Spatial ordering",
        "Duplicates": "Yes",
        "Thread-safe": "No",
        "Use cases": "GIS, spatial databases, map applications, CAD systems",
        "Industries": "Geographic information systems, databases (PostGIS), mapping",
        "When to use": "Spatial rectangles/polygons; range/intersection queries; GIS applications",
        "When NOT to use": "Point data only (KD-tree better); 1D data"
    },
    
    # ==================== CONCURRENT STRUCTURES ====================
    {
        "Category": "Concurrent",
        "Name": "Concurrent Hash Map",
        "Concept": "Thread-safe hash map with fine-grained locking",
        "Java": "ConcurrentHashMap<K,V>",
        "C++": "TBB concurrent_hash_map",
        "Python": "Custom with locks (GIL helps)",
        "JavaScript": "N/A (single-threaded)",
        "Access by index": "N/A",
        "Access front": "N/A",
        "Access back": "N/A",
        "Insert front": "N/A",
        "Insert middle": "O(1) avg",
        "Insert back": "O(1) avg",
        "Delete front": "N/A",
        "Delete middle": "O(1) avg",
        "Delete back": "O(1) avg",
        "Search unsorted": "O(1) avg",
        "Search sorted": "N/A",
        "Memory locality": "Moderate",
        "Memory overhead": "Higher than HashMap (locks/segments)",
        "Ordered": "No",
        "Duplicates": "No duplicate keys",
        "Thread-safe": "Yes",
        "Use cases": "Shared caches, concurrent servers, parallel algorithms, thread-safe mappings",
        "Industries": "High-performance servers, concurrent applications, real-time systems",
        "When to use": "Multiple threads access map; high concurrency; lock-free performance needed",
        "When NOT to use": "Single-threaded; can synchronize externally; memory overhead critical"
    },
    {
        "Category": "Concurrent",
        "Name": "Blocking Queue",
        "Concept": "Thread-safe queue with blocking operations",
        "Java": "ArrayBlockingQueue, LinkedBlockingQueue",
        "C++": "TBB concurrent_queue",
        "Python": "queue.Queue",
        "JavaScript": "N/A (single-threaded)",
        "Access by index": "N/A",
        "Access front": "O(1) blocking take",
        "Access back": "O(1)",
        "Insert front": "N/A",
        "Insert middle": "N/A",
        "Insert back": "O(1) blocking put",
        "Delete front": "O(1) take",
        "Delete middle": "N/A",
        "Delete back": "N/A",
        "Search unsorted": "O(n)",
        "Search sorted": "N/A",
        "Memory locality": "Good",
        "Memory overhead": "Lock/condition overhead",
        "Ordered": "FIFO",
        "Duplicates": "Yes",
        "Thread-safe": "Yes",
        "Use cases": "Producer-consumer, thread pools, task queues, message passing",
        "Industries": "Multi-threaded applications, web servers, background processing",
        "When to use": "Producer-consumer pattern; thread coordination; bounded buffer needed",
        "When NOT to use": "Single-threaded; lock-free alternatives available; no blocking needed"
    },
    
    # ==================== STRING STRUCTURES ====================
    {
        "Category": "String",
        "Name": "Rope (String)",
        "Concept": "Tree-based string for efficient editing",
        "Java": "Custom or Apache Commons",
        "C++": "SGI std::rope (deprecated) or custom",
        "Python": "Custom implementation",
        "JavaScript": "Custom implementation",
        "Access by index": "O(log n)",
        "Access front": "O(log n)",
        "Access back": "O(log n)",
        "Insert front": "O(log n)",
        "Insert middle": "O(log n)",
        "Insert back": "O(log n)",
        "Delete front": "O(log n)",
        "Delete middle": "O(log n)",
        "Delete back": "O(log n)",
        "Search unsorted": "O(n)",
        "Search sorted": "N/A",
        "Memory locality": "Poor (tree-based)",
        "Memory overhead": "Tree nodes",
        "Ordered": "Character sequence",
        "Duplicates": "N/A",
        "Thread-safe": "No",
        "Use cases": "Large text editing, text editors, string manipulation with many inserts/deletes",
        "Industries": "Text editors, IDEs, document processing",
        "When to use": "Large strings (MB+); frequent insertions/deletions; many concatenations",
        "When NOT to use": "Small strings; mostly sequential access; simplicity preferred"
    },
    {
        "Category": "String",
        "Name": "Suffix Array",
        "Concept": "Sorted array of all suffixes",
        "Java": "Custom implementation",
        "C++": "Custom implementation",
        "Python": "Custom or pysuffixarray",
        "JavaScript": "Custom implementation",
        "Access by index": "O(log n) with binary search",
        "Access front": "O(1)",
        "Access back": "O(1)",
        "Insert front": "O(n) rebuild",
        "Insert middle": "O(n) rebuild",
        "Insert back": "O(n) rebuild",
        "Delete front": "O(n) rebuild",
        "Delete middle": "O(n) rebuild",
        "Delete back": "O(n) rebuild",
        "Search unsorted": "N/A",
        "Search sorted": "O(m log n) pattern search",
        "Memory locality": "Excellent (array)",
        "Memory overhead": "O(n) integers",
        "Ordered": "Suffix order",
        "Duplicates": "N/A",
        "Thread-safe": "No",
        "Use cases": "Pattern matching, longest common substring, bioinformatics, data compression",
        "Industries": "Bioinformatics, text processing, search engines",
        "When to use": "Space-efficient suffix structure; pattern matching; static text",
        "When NOT to use": "Dynamic text (suffix tree better for some queries); simple pattern matching"
    }
]

# ==============================================================================
# CONCEPTS EXPLANATIONS
# ==============================================================================
concepts = [
    {
        "Concept": "Hash Table",
        "Explanation": "Data structure using hash function to map keys to buckets. Provides average O(1) lookup, insert, delete. Collision handling via chaining (linked lists) or open addressing (probing).",
        "Industries": "Web development, databases, caching systems, compilers, interpreters",
        "When used": "Dictionaries, caches, symbol tables, frequency counting, memoization, deduplication",
        "When not used": "When ordered iteration required; when worst-case guarantees needed; when keys need sorting"
    },
    {
        "Concept": "Balanced Binary Search Tree",
        "Explanation": "Self-balancing tree maintaining O(log n) height through rotations. Variants include AVL (strict height balance), Red-Black (relaxed balance, fewer rotations), and B-Tree (multi-key nodes for disk).",
        "Industries": "Database management, operating systems, compilers, financial systems",
        "When used": "Sorted collections, range queries, order statistics, ceiling/floor operations, sorted maps/sets",
        "When not used": "When hash table's average O(1) is sufficient; when order doesn't matter; high memory overhead unacceptable"
    },
    {
        "Concept": "Trie / Radix Tree",
        "Explanation": "Tree where each node represents a character/prefix. Enables efficient prefix operations. Radix tree is compressed version merging single-child paths. High memory usage but excellent for prefix queries.",
        "Industries": "Search engines, networking (IP routing), text processing, autocomplete systems, bioinformatics",
        "When used": "Autocomplete, spell checking, prefix matching, IP routing tables, dictionary implementations",
        "When not used": "Keys are random without shared prefixes; memory is limited; simple lookups without prefix queries"
    },
    {
        "Concept": "Heap",
        "Explanation": "Complete binary tree maintaining heap property (parent ≥/≤ children). Typically array-based for cache efficiency. Enables O(1) min/max access and O(log n) insert/extract.",
        "Industries": "Operating systems (process scheduling), event simulation, graph algorithms, real-time systems",
        "When used": "Priority queues, event scheduling, Dijkstra/Prim algorithms, heap sort, k-largest/smallest elements",
        "When not used": "When full sorting needed; when searching by arbitrary value; for FIFO queues; ordered iteration required"
    },
    {
        "Concept": "B-Tree / B+Tree",
        "Explanation": "Multi-way balanced tree with multiple keys per node, optimized for block-based storage (disk/SSD). Keeps tree shallow to minimize disk seeks. B+Tree stores data only in leaves for better range scans.",
        "Industries": "Database management systems, file systems, storage engines",
        "When used": "Database indexes, disk-based data structures, file systems (NTFS, ext4), when minimizing I/O operations",
        "When not used": "Small in-memory datasets; when node size doesn't align with block size; simpler BST sufficient"
    },
    {
        "Concept": "Graph Representations",
        "Explanation": "Adjacency List: array/map of neighbor lists, O(V+E) space, best for sparse graphs. Adjacency Matrix: 2D array, O(V²) space, O(1) edge checks, best for dense graphs.",
        "Industries": "Social networks, routing systems, compilers, recommendation engines, network analysis",
        "When used": "Social graphs, dependency analysis, routing algorithms, network topology, web crawling",
        "When not used": "Adjacency list for dense graphs (use matrix); adjacency matrix for sparse (wastes memory)"
    },
    {
        "Concept": "Disjoint Set (Union-Find)",
        "Explanation": "Tracks partition of elements into disjoint sets. With path compression and union by rank, achieves nearly O(1) operations (inverse Ackermann function). No deletion support.",
        "Industries": "Graph algorithms, network connectivity analysis, image segmentation, clustering",
        "When used": "Kruskal's MST, cycle detection, connected components, dynamic connectivity, percolation",
        "When not used": "When deletions required; when full graph structure needed; when simple DFS/BFS works"
    },
    {
        "Concept": "Bloom Filter",
        "Explanation": "Probabilistic data structure for set membership testing. Uses multiple hash functions and bit array. Space-efficient but allows false positives (never false negatives). No deletion in standard implementation.",
        "Industries": "Databases (query optimization), web crawlers, CDNs, blockchain, spam filtering",
        "When used": "Cache filtering, spell checkers, duplicate prevention, when space is premium and false positives acceptable",
        "When not used": "False positives unacceptable; deletions needed; exact counting required; small datasets"
    },
    {
        "Concept": "Segment Tree / Fenwick Tree",
        "Explanation": "Segment Tree: binary tree for range queries/updates (sum, min, max), O(log n) per op, ~4n space. Fenwick/BIT: array-based for prefix sums, simpler, O(n) space, only supports cumulative operations.",
        "Industries": "Competitive programming, analytics, time-series analysis, computational geometry",
        "When used": "Range queries with updates, interval problems, prefix sums, dynamic cumulative frequencies",
        "When not used": "Static arrays (simple prefix sum array works); only point queries; when simple scan acceptable"
    },
    {
        "Concept": "Skip List",
        "Explanation": "Probabilistic alternative to balanced BST using multi-level linked lists. Each level is express lane for level below. Simpler implementation than red-black trees, naturally supports concurrency.",
        "Industries": "Concurrent systems, databases (Redis uses skip lists), distributed systems",
        "When used": "Concurrent sorted maps, when simpler than balanced trees, lock-free data structures, in-memory databases",
        "When not used": "Memory overhead is concern; deterministic worst-case bounds required; non-concurrent scenarios"
    },
    {
        "Concept": "LRU Cache",
        "Explanation": "Combines hash map for O(1) access with doubly-linked list for O(1) eviction. Most recently used items at front, least at back. On access, move item to front. When full, evict from back.",
        "Industries": "Web servers, databases, operating systems (page replacement), CDN systems",
        "When used": "Caching with size limits, memoization, browser history, database buffer pools, page replacement",
        "When not used": "Other eviction policies needed (LFU, FIFO); unlimited cache; access pattern not temporal"
    },
    {
        "Concept": "Trie Variants (Suffix Tree/Array)",
        "Explanation": "Suffix Tree: tree of all suffixes for fast substring queries, O(n) space, O(m) pattern search. Suffix Array: sorted array of suffixes, more space-efficient, requires LCP array for some queries.",
        "Industries": "Bioinformatics (DNA analysis), search engines, plagiarism detection, data compression",
        "When used": "Pattern matching, longest common substring, string indexing, DNA sequence analysis, full-text search",
        "When not used": "Small texts; simple pattern matching (KMP/Boyer-Moore suffices); construction cost prohibitive"
    },
    {
        "Concept": "Probabilistic Data Structures",
        "Explanation": "Space-efficient structures trading exactness for memory: Bloom Filter (membership, false positives), Count-Min Sketch (frequency), HyperLogLog (cardinality), Cuckoo Filter (membership with deletion). Use hash functions for probabilistic guarantees.",
        "Industries": "Big data, streaming analytics, databases, web scale systems, network monitoring",
        "When used": "Massive datasets; memory constrained; approximate answers acceptable; real-time streaming",
        "When not used": "Exact results required; small datasets fit in memory; strict accuracy needed"
    },
    {
        "Concept": "Spatial Data Structures",
        "Explanation": "Structures optimized for spatial queries: KD-Tree (k-dimensional points), Quadtree/Octree (2D/3D regions), R-Tree (rectangles). Enable efficient range and nearest-neighbor queries in geometric space.",
        "Industries": "Geographic information systems (GIS), computer graphics, game development, robotics, CAD",
        "When used": "Spatial/geometric data; nearest neighbor; collision detection; map rendering; location-based queries",
        "When not used": "1D data; no spatial relationships; simple coordinate lookups"
    },
    {
        "Concept": "Concurrent Data Structures",
        "Explanation": "Thread-safe structures for multi-threaded environments: ConcurrentHashMap (fine-grained locking), BlockingQueue (producer-consumer), Skip List (lock-free sorted). Avoid race conditions while maintaining performance.",
        "Industries": "Multi-threaded servers, parallel computing, real-time systems, high-performance computing",
        "When used": "Multiple threads; shared data; parallel algorithms; producer-consumer patterns",
        "When not used": "Single-threaded; external synchronization sufficient; performance overhead unacceptable"
    },
    {
        "Concept": "Stack vs Queue vs Deque",
        "Explanation": "Stack: LIFO (Last-In-First-Out) for depth-first, function calls, undo. Queue: FIFO (First-In-First-Out) for breadth-first, task scheduling. Deque: efficient at both ends, combines both use cases.",
        "Industries": "All software - fundamental structures in compilers, OS, algorithms, simulations",
        "When used": "Stack: recursion elimination, parsing, DFS. Queue: BFS, task scheduling, buffering. Deque: sliding window, both-end access",
        "When not used": "Stack: for FIFO. Queue: for LIFO or priority. Deque: when simple stack/queue suffices"
    },
    {
        "Concept": "Range Query Structures",
        "Explanation": "Segment Tree: mutable range queries (sum, min, max) with O(log n) update. Fenwick/BIT: simpler, prefix sums only. Sparse Table: static data, O(1) query. Each optimized for different update/query patterns.",
        "Industries": "Competitive programming, time-series analysis, computational geometry, game development",
        "When used": "Range sum/min/max queries; interval updates; cumulative statistics; dynamic data analysis",
        "When not used": "Point queries only; static data with no queries; simple array scan acceptable"
    }
]

# ==============================================================================
# OPERATIONS LEGEND
# ==============================================================================
operations_legend = [
    {
        "Operation": "Access by index",
        "Meaning": "Time to retrieve element at specific numeric index position",
        "Example": "array[5], list.get(5)"
    },
    {
        "Operation": "Access front",
        "Meaning": "Time to access first element",
        "Example": "array[0], list.getFirst(), deque.peekFirst()"
    },
    {
        "Operation": "Access back",
        "Meaning": "Time to access last element",
        "Example": "array[n-1], list.getLast(), deque.peekLast()"
    },
    {
        "Operation": "Insert front",
        "Meaning": "Time to insert element at beginning",
        "Example": "list.addFirst(), deque.addFirst()"
    },
    {
        "Operation": "Insert middle",
        "Meaning": "Time to insert at arbitrary position (average case for position lookup + insertion)",
        "Example": "list.add(index, element), array insert requires shifting"
    },
    {
        "Operation": "Insert back",
        "Meaning": "Time to append element at end",
        "Example": "list.add(element), array.push(), vector.push_back()"
    },
    {
        "Operation": "Delete front",
        "Meaning": "Time to remove first element",
        "Example": "list.removeFirst(), deque.pollFirst()"
    },
    {
        "Operation": "Delete middle",
        "Meaning": "Time to delete element at arbitrary position or by value",
        "Example": "list.remove(index), array deletion requires shifting"
    },
    {
        "Operation": "Delete back",
        "Meaning": "Time to remove last element",
        "Example": "list.removeLast(), array.pop(), vector.pop_back()"
    },
    {
        "Operation": "Search unsorted",
        "Meaning": "Time to find element by value in unordered collection",
        "Example": "Linear scan through array/list"
    },
    {
        "Operation": "Search sorted",
        "Meaning": "Time to find element in sorted collection",
        "Example": "Binary search on sorted array, TreeSet.contains()"
    },
    {
        "Operation": "Memory locality",
        "Meaning": "Cache-friendliness. 'Excellent' = contiguous (arrays), 'Poor' = scattered (linked structures)",
        "Example": "Arrays have excellent locality; linked lists have poor locality"
    },
    {
        "Operation": "Memory overhead",
        "Meaning": "Extra memory beyond element storage (pointers, metadata, empty buckets, etc.)",
        "Example": "Array: minimal; LinkedList: 2 pointers per node; HashMap: buckets + load factor"
    }
]

# ==============================================================================
# COMMON LIBRARIES
# ==============================================================================
libraries = [
    {
        "Language": "Java",
        "Category": "Collections Framework",
        "Libraries": "java.util: ArrayList, LinkedList, HashMap, TreeMap, HashSet, TreeSet, PriorityQueue, ArrayDeque, LinkedHashMap, BitSet, ConcurrentHashMap, ConcurrentSkipListMap"
    },
    {
        "Language": "Java",
        "Category": "Third-party",
        "Libraries": "Google Guava: Multimap, BiMap, Table, BloomFilter, Cache. Apache Commons: CircularFifoQueue. FastUtil: optimized primitive collections"
    },
    {
        "Language": "C++",
        "Category": "STL",
        "Libraries": "Sequence: vector, deque, list, forward_list, array. Associative: map, multimap, set, multiset, unordered_map, unordered_multimap, unordered_set, unordered_multiset. Adapters: stack, queue, priority_queue"
    },
    {
        "Language": "C++",
        "Category": "Third-party",
        "Libraries": "Boost: circular_buffer, multi_index, graph library, property_tree. abseil: flat_hash_map, node_hash_map. folly: F14 hash maps"
    },
    {
        "Language": "Python",
        "Category": "Built-in",
        "Libraries": "list, dict, set, tuple, collections.deque, collections.defaultdict, collections.Counter, collections.OrderedDict, heapq module, array.array"
    },
    {
        "Language": "Python",
        "Category": "Third-party",
        "Libraries": "sortedcontainers: SortedList, SortedDict, SortedSet. pygtrie: trie implementations. bintrees: AVL, RB trees. bitarray: efficient bit arrays"
    },
    {
        "Language": "JavaScript",
        "Category": "Built-in",
        "Libraries": "Array, Map, Set, WeakMap, WeakSet, TypedArray (Int8Array, Uint8Array, Float32Array, etc.)"
    },
    {
        "Language": "JavaScript",
        "Category": "Third-party (npm)",
        "Libraries": "immutable.js: persistent data structures. lodash: utility functions. collections: MultiMap, SortedSet. datastructures-js: various implementations. mnemonist: trie, bloom filter, etc."
    }
]

# ==============================================================================
# COMPLEXITY NOTATION GUIDE
# ==============================================================================
complexity_guide = [
    {
        "Notation": "O(1)",
        "Name": "Constant",
        "Description": "Operation takes same time regardless of input size",
        "Examples": "Array access by index, hash table lookup (average), stack push/pop"
    },
    {
        "Notation": "O(log n)",
        "Name": "Logarithmic",
        "Description": "Time grows logarithmically with input size. Typically from dividing problem in half repeatedly",
        "Examples": "Binary search, balanced tree operations, heap insert/delete"
    },
    {
        "Notation": "O(n)",
        "Name": "Linear",
        "Description": "Time grows linearly with input size. Must examine each element once",
        "Examples": "Array scan, linked list traversal, linear search"
    },
    {
        "Notation": "O(n log n)",
        "Name": "Linearithmic",
        "Description": "Common for efficient sorting algorithms",
        "Examples": "Merge sort, heap sort, quick sort (average)"
    },
    {
        "Notation": "O(n²)",
        "Name": "Quadratic",
        "Description": "Time grows quadratically, typically from nested loops over input",
        "Examples": "Bubble sort, selection sort, naive string matching, adjacency matrix for all edges"
    },
    {
        "Notation": "O(2ⁿ)",
        "Name": "Exponential",
        "Description": "Time doubles with each additional input element",
        "Examples": "Recursive fibonacci (naive), generating all subsets, traveling salesman (brute force)"
    },
    {
        "Notation": "Amortized O(1)",
        "Name": "Amortized Constant",
        "Description": "Average time per operation over sequence of operations is constant, though individual ops may be expensive",
        "Examples": "Dynamic array append, stack push, disjoint set operations"
    },
    {
        "Notation": "O(α(n))",
        "Name": "Inverse Ackermann",
        "Description": "Extremely slow-growing function, effectively constant for all practical purposes",
        "Examples": "Disjoint set union/find with path compression and union by rank"
    },
    {
        "Notation": "O(k)",
        "Name": "Dependent on parameter",
        "Description": "Time depends on parameter k (e.g., number of hash functions, string length)",
        "Examples": "Bloom filter operations (k hash functions), trie operations (k = key length)"
    }
]

# ==============================================================================
# USE CASE SCENARIOS
# ==============================================================================
use_cases = [
    {
        "Scenario": "Caching with size limit",
        "Requirements": "Fast access, automatic eviction, size bounded",
        "Best choice": "LRU Cache (LinkedHashMap + eviction)",
        "Why": "O(1) access and update, automatic eviction of least recently used",
        "Avoid": "Regular HashMap (no eviction), TreeMap (slower access)"
    },
    {
        "Scenario": "Autocomplete / prefix search",
        "Requirements": "Fast prefix matching, many queries",
        "Best choice": "Trie (Prefix Tree)",
        "Why": "O(m) prefix search where m=query length, natural prefix operations",
        "Avoid": "Hash map (can't do prefix), sorted array (slower), BST (not optimized for prefixes)"
    },
    {
        "Scenario": "Finding k largest elements",
        "Requirements": "Efficiently maintain top k items from stream",
        "Best choice": "Min-Heap of size k",
        "Why": "O(log k) insert, O(1) access to k-th largest, space O(k)",
        "Avoid": "Sorting entire stream O(n log n), array scan O(nk)"
    },
    {
        "Scenario": "Duplicate detection in stream",
        "Requirements": "Fast membership test, memory constrained",
        "Best choice": "Bloom Filter (if false positives OK) or Hash Set",
        "Why": "Bloom: minimal memory, O(k) check. HashSet: exact, O(1) average",
        "Avoid": "Sorted array (slow insert), trie (memory overhead)"
    },
    {
        "Scenario": "Range queries with updates",
        "Requirements": "Find min/max/sum in range, update values",
        "Best choice": "Segment Tree or Fenwick Tree",
        "Why": "O(log n) query and update, segment tree more flexible",
        "Avoid": "Array (O(n) query), BST (not designed for ranges)"
    },
    {
        "Scenario": "Scheduling with priorities",
        "Requirements": "Always process highest priority, add new tasks",
        "Best choice": "Priority Queue (Binary Heap)",
        "Why": "O(1) peek max priority, O(log n) insert/extract",
        "Avoid": "Sorted array (O(n) insert), unsorted (O(n) find max)"
    },
    {
        "Scenario": "Undo/Redo in text editor",
        "Requirements": "Track history, navigate back/forth",
        "Best choice": "Deque or two Stacks",
        "Why": "O(1) add/remove at both ends, natural for undo/redo",
        "Avoid": "ArrayList (shifting overhead), LinkedList (poor locality for iteration)"
    },
    {
        "Scenario": "Graph connectivity queries",
        "Requirements": "Check if nodes connected, merge components",
        "Best choice": "Disjoint Set (Union-Find)",
        "Why": "Nearly O(1) find and union, optimal for dynamic connectivity",
        "Avoid": "DFS/BFS each query O(V+E), adjacency matrix O(V²) space"
    },
    {
        "Scenario": "Database index",
        "Requirements": "Sorted access, range queries, disk-based",
        "Best choice": "B-Tree or B+Tree",
        "Why": "Minimizes disk I/O, shallow tree, sorted order, efficient range scans",
        "Avoid": "Binary tree (too deep), hash table (no ordering/ranges)"
    },
    {
        "Scenario": "Frequency counting",
        "Requirements": "Count occurrences of items",
        "Best choice": "Hash Map (item → count)",
        "Why": "O(1) average increment/lookup, flexible for any type",
        "Avoid": "Array (if items aren't small integers), TreeMap (slower)"
    },
    {
        "Scenario": "Sorted unique elements with fast access",
        "Requirements": "Maintain sorted order, no duplicates, fast operations",
        "Best choice": "TreeSet (Red-Black Tree)",
        "Why": "O(log n) insert/delete/search, maintains order, no duplicates",
        "Avoid": "HashSet (no order), sorted array (O(n) insert)"
    },
    {
        "Scenario": "Graph with frequent edge checks",
        "Requirements": "Often check if edge exists between vertices",
        "Best choice": "Adjacency Matrix (if dense) or Hash-based Adjacency List",
        "Why": "Matrix: O(1) edge check. Hash: O(1) average if using HashMap<Vertex, Set<Vertex>>",
        "Avoid": "Simple adjacency list with array/linked list (O(degree) check)"
    },
    {
        "Scenario": "Real-time leaderboard",
        "Requirements": "Frequent score updates, rank queries, top-k retrieval",
        "Best choice": "Skip List or TreeMap with count tracking",
        "Why": "O(log n) insert/delete/rank, naturally sorted, efficient range queries",
        "Avoid": "Array (O(n) insert/sort), HashMap (no ordering), heap (no rank queries)"
    },
    {
        "Scenario": "IP address routing table",
        "Requirements": "Longest prefix match, efficient lookup, memory efficient",
        "Best choice": "Trie (Radix Tree/Patricia Trie)",
        "Why": "O(m) lookup where m=address length, prefix matching natural, compressed trie saves space",
        "Avoid": "Hash table (no prefix matching), binary search (slower for prefixes)"
    },
    {
        "Scenario": "Spell checker / autocomplete",
        "Requirements": "Prefix matching, dictionary storage, suggestions",
        "Best choice": "Trie (Prefix Tree)",
        "Why": "O(m) prefix search, all words with prefix efficiently retrieved, natural for dictionaries",
        "Avoid": "Hash table (can't do prefixes), sorted array (slower prefix enumeration)"
    },
    {
        "Scenario": "In-memory time-series database",
        "Requirements": "Range queries by time, aggregations, recent data access",
        "Best choice": "Segment Tree or Fenwick Tree + Circular Buffer",
        "Why": "O(log n) range queries, efficient updates, circular buffer for windowing",
        "Avoid": "Simple array (O(n) range scan), linked list (poor locality)"
    },
    {
        "Scenario": "Web crawler URL deduplication",
        "Requirements": "Billions of URLs, memory constrained, duplicates not critical",
        "Best choice": "Bloom Filter",
        "Why": "Constant memory regardless of URLs, O(k) lookup, false positives acceptable (just re-crawl)",
        "Avoid": "HashSet (too much memory for billions), database (too slow)"
    },
    {
        "Scenario": "Game spatial collision detection",
        "Requirements": "2D/3D objects, range queries, moving objects",
        "Best choice": "Quadtree (2D) or Octree (3D)",
        "Why": "Spatial partitioning, O(log n) region queries, dynamic updates",
        "Avoid": "Brute force O(n²), static grid (poor for non-uniform distribution)"
    },
    {
        "Scenario": "Expression evaluation (calculator)",
        "Requirements": "Parse infix notation, handle parentheses, operator precedence",
        "Best choice": "Stack (for operators and operands)",
        "Why": "Natural LIFO for operator precedence and parentheses matching",
        "Avoid": "Queue (wrong order), recursion (stack overflow risk for deep expressions)"
    },
    {
        "Scenario": "Browser back/forward navigation",
        "Requirements": "Navigate history, add new pages, go back/forward",
        "Best choice": "Two Stacks (back and forward)",
        "Why": "O(1) push/pop, natural for undo/redo pattern",
        "Avoid": "Array (O(n) for position tracking), single stack (can't do forward)"
    },
    {
        "Scenario": "Social network friend suggestions",
        "Requirements": "Find common friends, graph connectivity, recommend connections",
        "Best choice": "Adjacency List + BFS/DFS",
        "Why": "Sparse graph structure, O(V+E) traversal, efficient neighbor iteration",
        "Avoid": "Adjacency matrix (too much memory for millions of users)"
    },
    {
        "Scenario": "Unique visitors per day (analytics)",
        "Requirements": "Count distinct IPs/users, massive scale, approximate OK",
        "Best choice": "HyperLogLog",
        "Why": "Fixed small memory (~1KB for billions of users), <2% error, O(1) add/count",
        "Avoid": "HashSet (too much memory), exact counting (unnecessary for analytics)"
    },
    {
        "Scenario": "Database query result caching",
        "Requirements": "Cache frequently accessed queries, evict old/unused, size limit",
        "Best choice": "LRU Cache (LinkedHashMap)",
        "Why": "O(1) access and eviction, automatic removal of least recently used",
        "Avoid": "Simple HashMap (no eviction), FIFO (doesn't consider frequency)"
    },
    {
        "Scenario": "Network packet buffering",
        "Requirements": "Fixed buffer size, FIFO, overwrite old packets if full",
        "Best choice": "Circular Buffer (Ring Buffer)",
        "Why": "O(1) operations, fixed memory, automatic overwrite, excellent for streaming",
        "Avoid": "Queue with resizing (memory spikes), linked list (poor cache locality)"
    },
    {
        "Scenario": "File system directory structure",
        "Requirements": "Hierarchical organization, path traversal, nested folders",
        "Best choice": "Tree (general tree, not binary)",
        "Why": "Natural hierarchy, O(depth) path traversal, variable children per node",
        "Avoid": "Flat structure (no hierarchy), binary tree (limited children)"
    },
    {
        "Scenario": "Collaborative text editor (real-time)",
        "Requirements": "Concurrent edits, conflict resolution, insertion tracking",
        "Best choice": "Rope or CRDT (Conflict-free Replicated Data Type)",
        "Why": "Efficient inserts/deletes, handles concurrent modifications, maintains consistency",
        "Avoid": "Simple string (O(n) inserts), array (poor for distributed edits)"
    },
    {
        "Scenario": "Huffman encoding (compression)",
        "Requirements": "Build frequency tree, extract min twice repeatedly",
        "Best choice": "Min-Heap (Priority Queue)",
        "Why": "O(log n) extract-min, O(log n) insert, perfect for building Huffman tree",
        "Avoid": "Sorted array (O(n) insert), unsorted array (O(n) find min)"
    },
    {
        "Scenario": "Job scheduling with deadlines",
        "Requirements": "Process highest priority, dynamic priorities, deadline tracking",
        "Best choice": "Priority Queue (Binary Heap) + TreeMap for deadlines",
        "Why": "O(log n) priority updates, O(1) get next job, O(log n) deadline checks",
        "Avoid": "Sorted array (O(n) insert), simple queue (no priority)"
    },
    {
        "Scenario": "Symbol table in compiler",
        "Requirements": "Variable lookup, nested scopes, fast insertion/deletion",
        "Best choice": "Hash Map (per scope) with stack of scopes",
        "Why": "O(1) lookup, easy scope entry/exit with stack, efficient for typical code",
        "Avoid": "Single global map (scope conflicts), tree (unnecessary ordering)"
    },
    {
        "Scenario": "Finding connected components in network",
        "Requirements": "Determine if nodes connected, merge components, dynamic updates",
        "Best choice": "Disjoint Set (Union-Find)",
        "Why": "Nearly O(1) find and union, optimal for connectivity, simple implementation",
        "Avoid": "DFS each query O(V+E), storing all edges explicitly"
    },
    {
        "Scenario": "Median maintenance in stream",
        "Requirements": "Insert numbers continuously, query median anytime",
        "Best choice": "Two Heaps (max-heap for lower half, min-heap for upper half)",
        "Why": "O(log n) insert, O(1) median retrieval, balanced partition",
        "Avoid": "Sorting each time O(n log n), single heap (can't get median efficiently)"
    }
]

# ==============================================================================
# CREATE EXCEL WORKBOOK
# ==============================================================================
output_path = Path("/home/vasco-debian/Desktop/DEV/Versioned/Personal/exel_DS/datastructures_comprehensive_catalog.xlsx")

# Create DataFrames
df_structures = pd.DataFrame(structures)
df_concepts = pd.DataFrame(concepts)
df_operations = pd.DataFrame(operations_legend)
df_libraries = pd.DataFrame(libraries)
df_complexity = pd.DataFrame(complexity_guide)
df_use_cases = pd.DataFrame(use_cases)

# Write to Excel with multiple sheets
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df_structures.to_excel(writer, sheet_name='Data Structures', index=False)
    df_concepts.to_excel(writer, sheet_name='Concepts', index=False)
    df_operations.to_excel(writer, sheet_name='Operations Legend', index=False)
    df_libraries.to_excel(writer, sheet_name='Libraries', index=False)
    df_complexity.to_excel(writer, sheet_name='Complexity Guide', index=False)
    df_use_cases.to_excel(writer, sheet_name='Use Case Scenarios', index=False)
    
    # Auto-adjust column widths for readability
    for sheet_name in writer.sheets:
        worksheet = writer.sheets[sheet_name]
        for column in worksheet.columns:
            max_length = 0
            column_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)  # Cap at 50 for readability
            worksheet.column_dimensions[column_letter].width = adjusted_width

print(f"✅ Successfully created comprehensive data structures catalog!")
print(f"📁 Location: {output_path}")
print(f"\n📊 Workbook contains {len(writer.sheets)} sheets:")
print("   1. Data Structures - Main catalog with all structures")
print("   2. Concepts - Detailed explanations of core concepts")
print("   3. Operations Legend - What each complexity column means")
print("   4. Libraries - Common libraries per language")
print("   5. Complexity Guide - Big-O notation explained")
print("   6. Use Case Scenarios - When to use which structure")
print(f"\n📈 Total structures documented: {len(structures)}")
print(f"🔍 Total concepts explained: {len(concepts)}")
print(f"💡 Total use cases: {len(use_cases)}")
