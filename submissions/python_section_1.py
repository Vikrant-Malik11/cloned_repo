from typing import Dict, List

import pandas as pd


def reverse_by_n_elements(lst,n) -> List[int]:
    """
    Reverses the input list by groups of n elements.
    """
    # Your code goes here.
    result = []
    for i in range(0, len(lst), n):
        group = lst[i:i+n]
        reversed_group = []
        
        for j in range(len(group)):
            reversed_group.append(group[len(group) - 1 - j])
        result.extend(reversed_group)
    return result



def group_by_length(strings) -> Dict[int, List[str]]:
    """
    Groups the strings by their length and returns a dictionary.
    """
    # Your code here
    result = {}
    
    for string in strings:
        length = len(string)
        if length not in result:
            result[length] = []
            
        result[length].append(string)
    sorted_dict=dict(sorted(result.items()))

    return sorted_dict

def flatten_dict(d, parent_key='', sep='.'):
    """
    Flattens a nested dictionary into a single-level dictionary with dot notation for keys.
    
    :param nested_dict: The dictionary object to flatten
    :param sep: The separator to use between parent and child keys (defaults to '.')
    :return: A flattened dictionary
    """
    # Your code here
    
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                
                items.extend(flatten_dict({f"{new_key}[{i}]": item}, '', sep=sep).items())
        else:
            items.append((new_key, v))

    return dict(items)
    
    
    return dict

def unique_permutations(List) -> List[List[int]]:
    """
    Generate all unique permutations of a list that may contain duplicates.
    
    :param nums: List of integers (may contain duplicates)
    :return: List of unique permutations
    """
    # Your code here
    from itertools import permutations

    all_perms = permutations(lst)
    
    unique_perms = set(all_perms)
    
    return [list(perm) for perm in unique_perms]



def find_all_dates(text: str) -> List[str]:
    """
    This function takes a string as input and returns a list of valid dates
    in 'dd-mm-yyyy', 'mm/dd/yyyy', or 'yyyy.mm.dd' format found in the string.
    
    Parameters:
    text (str): A string containing the dates in various formats.

    Returns:
    List[str]: A list of valid dates in the formats specified.
    """
    import re

    patterns = [
        r'\b\d{2}-\d{2}-\d{4}\b',  # dd-mm-yyyy
        r'\b\d{2}/\d{2}/\d{4}\b',  # mm/dd/yyyy
        r'\b\d{4}\.\d{2}\.\d{2}\b'  # yyyy.mm.dd
    ]
    

    combined_pattern = '|'.join(patterns)
    
    matches = re.findall(combined_pattern, text)
    
    return matches


def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.
    
    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """
    return pd.Dataframe()


def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotate the given matrix by 90 degrees clockwise, then multiply each element 
    by the sum of its original row and column index before rotation.
    
    Args:
    - matrix (List[List[int]]): 2D list representing the matrix to be transformed.
    
    Returns:
    - List[List[int]]: A new 2D list representing the transformed matrix.
    """
    # Your code here
    n = len(matrix)
    
    rotated_matrix = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
    
    final_matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            row_sum = sum(rotated_matrix[i]) - rotated_matrix[i][j]
            col_sum = sum(rotated_matrix[k][j] for k in range(n)) - rotated_matrix[i][j]
            final_matrix[i][j] = row_sum + col_sum
    
    return final_matrix



def time_check(df) -> pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    import pandas as pd
    
    df.set_index(['id', 'id_2'], inplace=True)
    
    completeness = pd.Series(index=df.index.unique(), dtype=bool)
    
    full_hours = set(range(24))
    full_days = set(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    for idx in df.index.unique():
        subset = df.loc[idx]
        
        hours = set(subset['startTime'].apply(lambda x: int(x.split(':')[0])))
        days = set(subset['startDay'])
        
        completeness[idx] = (hours == full_hours) and (days == full_days)
    
    return completeness

    return pd.Series()
