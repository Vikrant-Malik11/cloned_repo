import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here

    ids = df['id'].unique()
    distance_matrix = pd.DataFrame(index=ids, columns=ids).fillna(0)
    
    for _, row in df.iterrows():
        id_start = row['id_start']
        id_end = row['id_end']
        distance = row['distance']
        distance_matrix.at[id_start, id_end] = distance
        distance_matrix.at[id_end, id_start] = distance
    
    for k in ids:
        for i in ids:
            for j in ids:
                if distance_matrix.at[i, j] > distance_matrix.at[i, k] + distance_matrix.at[k, j]:
                    distance_matrix.at[i, j] = distance_matrix.at[i, k] + distance_matrix.at[k, j]
    
    for id in ids:
        distance_matrix.at[id, id] = 0
    
    return distance_matrix


def unroll_distance_matrix(distance_matrix)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
    unrolled_data = []

    for id_start in distance_matrix.index:
        for id_end in distance_matrix.columns:
            if id_start != id_end:
            
                unrolled_data.append([id_start, id_end, distance_matrix.loc[id_start, id_end]])

    
    unrolled_df = pd.DataFrame(unrolled_data, columns=['id_start', 'id_end', 'distance'])

    return unrolled_df



def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
    
    reference_avg_distance = df[df['id_start'] == reference_id]['distance'].mean()

    lower_bound = reference_avg_distance * 0.9
    upper_bound = reference_avg_distance * 1.1

    ids_within_threshold = df.groupby('id_start')['distance'].mean()
    ids_within_threshold = ids_within_threshold[(ids_within_threshold >= lower_bound) & (ids_within_threshold <= upper_bound)].index.tolist()
    
    return df=sorted(ids_within_threshold)



def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
    rates = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    
    for vehicle, rate in rates.items():
        df[vehicle] = df['distance'] * rate
    
    return df

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here
    def apply_discount(row):
        start_time = row['start_time']
        end_time = row['end_time']
        start_day = row['start_day']
        end_day = row['end_day']
        
        if start_day in ['Saturday', 'Sunday']:
            discount_factor = 0.7
        else:
            if time(0, 0) <= start_time < time(10, 0):
                discount_factor = 0.8
            elif time(10, 0) <= start_time < time(18, 0):
                discount_factor = 1.2
            else:
                discount_factor = 0.8
        
        for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:
            row[vehicle] *= discount_factor
        
        return row
    
    df = df.apply(apply_discount, axis=1)
    return df

    return df
