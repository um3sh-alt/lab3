#!/usr/bin/env python3

# Define the list with initial values
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    """Appends a new item to the end of the list with the value (last item + 1)."""
    if ordered_list:  # Ensure list is not empty
        ordered_list.append(ordered_list[-1] + 1)

def remove_items_from_list(ordered_list, items_to_remove):
    """Removes all values found in items_to_remove list from ordered_list."""
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)

# Main code
if __name__ == '__main__':
    print(my_list)  # Initial list output
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)  # List after adding items
    remove_items_from_list(my_list, [1, 5, 6])
    print(my_list)  # List after removing items
