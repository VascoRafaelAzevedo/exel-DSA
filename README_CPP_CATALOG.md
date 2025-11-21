# C++ DSA Functions & Algorithms Catalog

## 📚 Overview

This project provides a comprehensive, professionally formatted Excel catalog of C++ Standard Template Library (STL) algorithms and container methods, specifically tailored for Data Structures and Algorithms (DSA) learning and competitive programming.

## 🎯 Purpose

- **Learning Resource**: Complete reference for C++ STL algorithms and containers
- **Interview Preparation**: Quick lookup for coding interviews
- **Competitive Programming**: Essential guide for LeetCode, Codeforces, HackerRank, etc.
- **Quick Reference**: Time/space complexity at a glance
- **Best Practices**: When to use vs. when NOT to use each function

## 📊 What's Included

### Generated Files

1. **`cpp_dsa_functions_catalog.xlsx`** (27KB)
   - Professional Excel spreadsheet with 99 comprehensive entries
   - 5 color-coded, filterable sheets
   - Frozen panes for easy navigation

2. **`generate_cpp_functions_catalog.py`** (1,250 lines)
   - Python script to generate the catalog
   - Fully self-contained (all data in code)
   - Easy to maintain and extend

### Catalog Contents

#### Sheet 1: STL Algorithms (56 functions)
From `<algorithm>` and `<numeric>` headers:

**Search & Find**: `find`, `find_if`, `find_if_not`, `find_first_of`, `find_end`, `adjacent_find`, `binary_search`, `lower_bound`, `upper_bound`, `equal_range`

**Sorting**: `sort`, `stable_sort`, `partial_sort`, `nth_element`, `is_sorted`, `is_sorted_until`

**Modifying Operations**: `copy`, `copy_if`, `copy_n`, `fill`, `fill_n`, `transform`, `generate`, `remove`, `remove_if`, `unique`, `reverse`, `rotate`, `shuffle`

**Heap Operations**: `make_heap`, `push_heap`, `pop_heap`, `sort_heap`

**Set Operations**: `set_union`, `set_intersection`, `set_difference`, `merge`, `includes`

**Min/Max**: `min`, `max`, `minmax`, `min_element`, `max_element`, `clamp`

**Permutations**: `next_permutation`, `prev_permutation`

**Partitioning**: `partition`, `stable_partition`, `partition_point`

**Numeric**: `accumulate`, `iota`, `gcd`, `lcm`

**Predicates**: `all_of`, `any_of`, `none_of`, `count`, `count_if`, `mismatch`

#### Sheet 2: Vector Methods (17 methods)
Complete `std::vector<T>` reference:
- Element Access: `[]`, `at()`, `front()`, `back()`, `data()`
- Capacity: `size()`, `empty()`, `reserve()`, `capacity()`, `resize()`
- Modifiers: `push_back()`, `emplace_back()`, `pop_back()`, `insert()`, `erase()`, `clear()`, `swap()`

#### Sheet 3: Map Methods (10 methods)
For `std::map` and `std::unordered_map`:
- Access: `[]`, `at()`
- Modifiers: `insert()`, `emplace()`, `erase()`, `clear()`
- Lookup: `find()`, `count()`, `contains()` (C++20)
- Capacity: `size()`, `empty()`

#### Sheet 4: Set Methods (7 methods)
For `std::set` and `std::unordered_set`:
- Modifiers: `insert()`, `erase()`
- Lookup: `find()`, `count()`, `contains()` (C++20), `lower_bound()`, `upper_bound()`

#### Sheet 5: Other Containers (9 summaries)
Quick reference for:
- `deque` - Double-ended queue
- `list` - Doubly-linked list
- `forward_list` - Singly-linked list
- `stack` - LIFO adapter
- `queue` - FIFO adapter
- `priority_queue` - Heap adapter
- `array` - Fixed-size array
- `multiset` - Set with duplicates
- `multimap` - Map with duplicate keys

## 📋 Information Fields

Each entry includes:

| Field | Description |
|-------|-------------|
| **Function/Method** | Name with namespace (e.g., `std::sort`) |
| **Header** | Required header file (e.g., `<algorithm>`) |
| **Category** | Classification (Search, Sorting, Modifying, etc.) |
| **Time Complexity** | Big-O notation (e.g., `O(n log n)`) |
| **Space Complexity** | Memory requirements (e.g., `O(1)`) |
| **Arguments** | Function signature parameters |
| **Arg Explanation** | Detailed parameter descriptions |
| **Return Type** | What the function returns |
| **Description** | Clear explanation of functionality |
| **When to Use** | Appropriate use cases |
| **When NOT to Use** | Anti-patterns and alternatives |
| **Real-World Freq** | Usage frequency in production code (1-10) |
| **DSA/LeetCode Freq** | Usage frequency in competitive programming (1-10) |
| **Example** | Working code snippet |
| **Notes** | Important warnings, gotchas, tips |
| **Since Version** | C++ standard (C++98, C++11, C++17, C++20, C++23) |
| **Related** | Similar/alternative functions |

## ✨ Features

### Professional Formatting
- ✅ **Color-Coded Headers**: Different color per sheet for easy identification
- ✅ **Auto-Filtering**: Sort and filter by any column
- ✅ **Frozen Panes**: Header row and first column stay visible while scrolling
- ✅ **Optimized Widths**: Columns automatically sized for readability
- ✅ **Alternating Rows**: Light gray/white for easier reading
- ✅ **Professional Borders**: Clean, organized appearance

### Comprehensive Coverage
- ✅ **50+ Algorithms**: Most important functions from `<algorithm>` and `<numeric>`
- ✅ **All Major Containers**: vector, map, set, deque, list, stack, queue, priority_queue, etc.
- ✅ **Complexity Analysis**: Time and space complexity for every operation
- ✅ **Usage Guidance**: Real-world and competitive programming frequency ratings
- ✅ **Practical Examples**: Working code for each entry
- ✅ **Modern C++**: Includes C++11, C++17, C++20, and C++23 features

## 🚀 Usage

### Generating the Catalog

```bash
# Install dependencies
pip install pandas openpyxl

# Run the generator
python generate_cpp_functions_catalog.py
```

### Using the Excel File

1. **Open** `cpp_dsa_functions_catalog.xlsx` in Excel, LibreOffice, or Google Sheets
2. **Navigate** between sheets using the tabs at the bottom
3. **Filter** by clicking the dropdown arrows in the header row
4. **Sort** by clicking column headers or using the filter dropdown
5. **Search** using Ctrl+F (Cmd+F on Mac)

### Common Use Cases

**Learning**: 
- Study algorithms by category
- Compare time complexities
- Understand when to use each function

**Interview Prep**:
- Quick lookup during practice problems
- Review frequency ratings to prioritize learning
- Check complexity before implementing

**Competitive Programming**:
- Reference during contests
- Find the right algorithm quickly
- Check if a function exists before implementing manually

## 📖 Examples from the Catalog

### High-Frequency Algorithm: `std::sort`
```cpp
// Function: std::sort
// Time: O(n log n)
// Space: O(log n)
// Real-World Freq: 10/10
// DSA Freq: 10/10

std::vector<int> v = {5, 2, 8, 1, 9};
std::sort(v.begin(), v.end());  // Ascending: {1, 2, 5, 8, 9}

// Custom comparator for descending
std::sort(v.begin(), v.end(), [](int a, int b){ return a > b; });
```

### High-Frequency Search: `std::lower_bound`
```cpp
// Function: std::lower_bound
// Time: O(log n)
// Space: O(1)
// Real-World Freq: 8/10
// DSA Freq: 10/10

std::vector<int> v = {1, 2, 4, 4, 5, 8};  // Must be sorted!
auto it = std::lower_bound(v.begin(), v.end(), 4);  // First >= 4
// Returns iterator to first 4
```

### Essential Container Method: `vector::push_back`
```cpp
// Method: push_back
// Time: Amortized O(1)
// Space: O(1)
// Real-World Freq: 10/10
// DSA Freq: 10/10

std::vector<int> v;
v.push_back(42);  // Add element to end
```

## 🎓 Learning Tips

1. **Start with High-Frequency Items**: Focus on algorithms with DSA frequency >= 8
2. **Understand Complexity**: Always know the time/space trade-offs
3. **Practice Categories**: Master one category at a time (sorting, then searching, etc.)
4. **Use Examples**: Type out the examples to build muscle memory
5. **Read "When NOT to Use"**: Avoid common pitfalls
6. **Compare Alternatives**: Use "Related" column to find similar functions

## 🔍 Frequency Guide

### Real-World Frequency (1-10)
- **10**: Used daily in production code
- **8-9**: Very common, weekly usage
- **6-7**: Common, monthly usage
- **4-5**: Occasional, specific use cases
- **1-3**: Rare, specialized scenarios

### DSA/LeetCode Frequency (1-10)
- **10**: Essential, appears in most problems
- **8-9**: Very common, weekly in contests
- **6-7**: Common, appears regularly
- **4-5**: Moderate, certain problem types
- **1-3**: Rare, specialized problems

## 🛠️ Technical Details

**Dependencies**:
- Python 3.6+
- pandas
- openpyxl

**Format**: Excel 2007+ (.xlsx)

**Size**: 27KB (compact and efficient)

**Compatibility**: 
- Microsoft Excel
- LibreOffice Calc
- Google Sheets
- Numbers (Mac)

## 📝 Maintenance

To add new algorithms or containers:

1. Edit `generate_cpp_functions_catalog.py`
2. Add entries to the appropriate list (`stl_algorithms`, `vector_methods`, etc.)
3. Follow the existing dictionary structure
4. Run the script to regenerate the Excel file

## 🤝 Contributing

Suggestions for improvement:
- Additional algorithms or methods
- Better examples
- Corrected complexities
- Usage tips and notes

## 📄 License

This catalog is created for educational purposes. C++ and STL are maintained by the ISO C++ Standards Committee.

## 🌟 Acknowledgments

- Inspired by the need for a comprehensive C++ STL reference
- Based on C++ Standard Library documentation
- Designed for the DSA learning community
- Created to support competitive programmers worldwide

---

**Happy Coding! 🚀**

For questions or suggestions, refer to the repository documentation.
