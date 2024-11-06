import requests
import pandas as pd

# Fetches the main pools data
response = requests.get('https://yields.llama.fi/pools')
data_dict = response.json()

def process_pool_ids(data):
    # Creating the dictionary with the necessary columns
    cleaned_up_data = {
        "pool_id": [entry['pool'] for entry in data['data']],
        "chain": [entry['chain'] for entry in data['data']],
        "symbol": [entry['symbol'] for entry in data['data']],
        "project": [entry['project'] for entry in data['data']],
        "stablecoin": [entry["stablecoin"] for entry in data['data']],
        "count": [entry["count"] for entry in data['data']]
    }
    
    # Convert dictionary to DataFrame
    df = pd.DataFrame(cleaned_up_data)
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    return df

def get_historical_data(df):
    # Initialize a DataFrame to store all historical data
    historical_df = pd.DataFrame()
    
    # Iterate over each pool_id in the DataFrame
    for index, row in df.iterrows():
        pool_id = row['pool_id']
        chain = row['chain']
        symbol = row['symbol']
        project = row['project']
        stablecoin = row['stablecoin']
        count = row['count']
        
        # Fetch historical data for each pool_id
import requests
import pandas as pd

def get_historical_data(df, max_retries=3, delay=1):
    historical_df = pd.DataFrame()
    
    for index, row in df.iterrows():
        pool_id = row['pool_id']
        chain = row['chain']
        symbol = row['symbol']
        project = row['project']
        stablecoin = row['stablecoin']
        count = row['count']
        try: 
            for attempt in range(max_retries):
           
                # Fetch historical data
                response = requests.get(f"https://yields.llama.fi/chart/{pool_id}")
                
                if response.status_code == 200:
                    historical_data = response.json()["data"]
                    pool_history_df = pd.DataFrame(historical_data)
                    
                    # Add metadata to each historical entry
                    pool_history_df['pool_id'] = pool_id
                    pool_history_df['chain'] = chain
                    pool_history_df['symbol'] = symbol
                    pool_history_df['project'] = project
                    pool_history_df['stablecoin'] = stablecoin
                    pool_history_df['count'] = count
                    
                    # Append to the main historical DataFrame
                    historical_df = pd.concat([historical_df, pool_history_df], ignore_index=True)
                    break  # Exit retry loop on success
                
                else:
                    print(f"Debug: API fetch failed for pool_id: {pool_id} - Status Code: {response.status_code}")
                    print(f"Debug: Response Content: {response.content.decode()}")  # Print response content if any
                    bre
                
        except Exception as e:
                print(f"Attempt {attempt + 1} failed for pool_id: {pool_id}. Error: {e}") 
                break
    return historical_df

if __name__ == "__main__": 
    # Process main pool data
    pooldf = process_pool_ids(data_dict)
    
    # Fetch and add historical data
    historical_df = get_historical_data(pooldf)
    
    # Save combined historical data to CSV
    historical_df.to_csv('all_pool_historical_data.csv', index=False)
    
    print("Historical data saved to all_pool_historical_data.csv")

