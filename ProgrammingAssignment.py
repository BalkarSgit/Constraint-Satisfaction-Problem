
import random

# random module to choose a color 

# Province list in Canada Up to 10
provinces = ["Alberta", "British Columbia", "Manitoba", "New Brunswick",
    "Newfoundland and Labrador", "Nova Scotia", "Ontario", "Prince Edward Island",
    "Quebec", "Saskatchewan"]


# colors list created
colors = ["Red", "Green", "Blue"]

# Creating tuples list for neighbor provinces 
# neighbor_proninces tuple list will use to assign color to provinces, to avoid same for neighbor provinces
neighbor_provinces = [
    ("British Columbia", "Alberta"),
    ("Alberta", "British Columbia"),
    ("Alberta", "Saskatchewan"),
    ("Saskatchewan", "Alberta"),
    ("Saskatchewan", "Manitoba"),
    ("Manitoba", "Saskatchewan"),
    ("Manitoba", "Ontario"),
    ("Ontario", "Manitoba"),
    ("Ontario", "Quebec"),
    ("Quebec", "Ontario"),
    ("Quebec", "New Brunswick"),
    ("Quebec", "Newfoundland and Labrador"),
    ("New Brunswick", "Quebec"),
    ("New Brunswick", "Nova Scotia"),
    ("Nova Scotia", "New Brunswick"),
    ("Nova Scotia", "Prince Edward Island"),
    ("Prince Edward Island", "Nova Scotia"),
    ("Newfoundland and Labrador", "Quebec"),
    ("Newfoundland and Labrador", "Nova Scotia"),
    ("Newfoundland and Labrador", "New Brunswick"),
]

# dictonary to select colors for each province
province_dict = {
    "Alberta": list(colors),
    "British Columbia": list(colors),
    "Manitoba": list(colors),
    "New Brunswick": list(colors),
    "Newfoundland and Labrador": list(colors),
    "Nova Scotia": list(colors),
    "Ontario": list(colors),
    "Prince Edward Island": list(colors),
    "Quebec": list(colors),
    "Saskatchewan": list(colors)
}

# creating empty dictonary to update the colormap for provinces
province_colormap = {}

# empty list to update color list according to province neighbor
color_assigned = []


# for loop assign province colors
for province, available_colors in province_dict.items():
    chosen_color = random.choice(available_colors)      # selection the random color from available colors
    province_colormap[province] = chosen_color      # setting the choosen color for the province
    color_assigned.append(chosen_color)     #appending the choosen color to avoid neighbors with same color


    # for loop to check province neighbor
    for ngbr1, ngbr2 in neighbor_provinces:
        if province == ngbr1:
            if ngbr2 in province_dict and chosen_color in province_dict[ngbr2]:
                province_dict[ngbr2].remove(chosen_color)



# for loop to print dictonary
print(" --  Province -- ")
for key, value in province_colormap.items():
    print(key," : ", value)     # print dictonary province_colormap

