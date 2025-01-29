1. Using Timeseries Analysis of # of packets

2. targeted data = Atlanta and Dallas

3. Thinking of doing it minutely or hourly window then aggregating the # of packets

4. Since the JSON is not perfectly formatted, loading the data successfully into a Pandas DataFrame is already a significant step. However, storing and reloading this data efficiently in the future can be simplified by using formats like Pickle or Parquet, which are more efficient for large datasets than JSON. 

5. Steps to Combine Multiple Days of Data:

Load Each Day’s Data: Use the same method to load each file separately.
Concatenate the DataFrames: You can concatenate the DataFrames from multiple days into one large DataFrame using pd.concat().
Save as a Single File: Store the combined data in a more efficient format (Parquet).

6. 