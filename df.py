import requests
import pandas as pd
response = requests.get('https://yields.llama.fi/pools')
 
dict = response.json()

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
    
    df.to_csv('pool_ids.csv', index=False)
    df = df.reset_index(drop=True)
    return df
    
if __name__ == "__main__": 
    pooldf = process_pool_ids(dict)
    print(pooldf)


