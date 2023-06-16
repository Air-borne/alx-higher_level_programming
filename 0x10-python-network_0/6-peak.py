#!/usr/bin/python3
# finding the peak of unsorted integers
def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted
    integers using a divide-and-conquer
    approach.
    Returns the value of any peak found.
    """
    if not list_of_integers:
        return None

    n = len(list_of_integers)
    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)

    mid = n // 2
    if list_of_integers[mid] < list_of_integers[mid-1]:
        return find_peak(list_of_integers[:mid])
    elif list_of_integers[mid] < list_of_integers[mid+1]:
        return find_peak(list_of_integers[mid+1:])
    else:
        return list_of_integers[mid]
