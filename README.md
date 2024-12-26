# Constraint-Satisfaction-Problem 
## Province Coloring Program

This Python program assigns colors to Canadian provinces such that no two neighboring provinces share the same color. The program demonstrates the concept of graph coloring, where provinces represent graph nodes, and edges represent adjacency between provinces.

## Features
- Assigns one of three colors (Red, Green, or Blue) to each province.
- Ensures neighboring provinces have different colors.
- Uses random selection for assigning colors.

## Data Structures

### Provinces
A list of up to 10 Canadian provinces:
```python
provinces = [
    "Alberta", "British Columbia", "Manitoba", "New Brunswick",
    "Newfoundland and Labrador", "Nova Scotia", "Ontario",
    "Prince Edward Island", "Quebec", "Saskatchewan"
]
```

### Colors
A predefined list of three colors:
```python
colors = ["Red", "Green", "Blue"]
```

### Neighboring Provinces
A list of tuples representing adjacency relationships:
```python
neighbor_provinces = [
    ("British Columbia", "Alberta"),
    ("Alberta", "British Columbia"),
    ("Alberta", "Saskatchewan"),
    # ... and so on
]
```

### Province Color Map
A dictionary that maps each province to its assigned color:
```python
province_colormap = {}
```

## Algorithm
1. **Initialize Available Colors**: Each province starts with all three colors available.
2. **Assign Colors**: Randomly select a color for a province from its available colors.
3. **Update Neighbors**: Remove the chosen color from the available colors of neighboring provinces.
4. **Repeat**: Continue until all provinces are assigned a color.

## Example Output
The program prints a dictionary showing each province and its assigned color:
```
 --  Province -- 
Alberta  :  Red
British Columbia  :  Green
Manitoba  :  Blue
New Brunswick  :  Red
Newfoundland and Labrador  :  Green
Nova Scotia  :  Blue
Ontario  :  Red
Prince Edward Island  :  Green
Quebec  :  Blue
Saskatchewan  :  Green
```

## How to Run
1. Ensure Python is installed on your system.
2. Save the code in a file, e.g., `province_coloring.py`.
3. Run the program:
   ```
   python province_coloring.py
   ```
4. View the output in the console.

## Applications
This program is an example of the map coloring problem, a common application of graph theory. Practical uses include:
- Designing conflict-free schedules.
- Assigning frequencies in cellular networks.
- Partitioning tasks in parallel computing.

## Customization
- **Change the provinces**: Modify the `provinces` list and `neighbor_provinces` relationships.
- **Add more colors**: Update the `colors` list.

## Limitations
- Random color assignment may lead to non-optimal results.
- Fixed to three colors; increasing the number of colors requires adding to the `colors` list.


