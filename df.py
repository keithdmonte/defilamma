import requests
import pandas as pd


def process_pool_ids():

    # Fetches the main pools data
    response = requests.get("https://yields.llama.fi/pools")
    data_dict = response.json()

    # Creating the dictionary with the necessary columns
    cleaned_up_data = {
        "pool_id": [entry["pool"] for entry in data_dict["data"]],
        "chain": [entry["chain"] for entry in data_dict["data"]],
        "symbol": [entry["symbol"] for entry in data_dict["data"]],
        "project": [entry["project"] for entry in data_dict["data"]],
        "stablecoin": [entry["stablecoin"] for entry in data_dict["data"]],
        "count": [entry["count"] for entry in data_dict["data"]],
    }

    # Convert dictionary to DataFrame
    df = pd.DataFrame(cleaned_up_data)

    # Remove duplicates
    df = df.drop_duplicates()

    # save to csv
    df.to_csv("data/pools.csv", index=False)

    return df


def get_historical_data(df, max_retries=3, delay=1):
    historical_df = pd.DataFrame()

    for index, row in df.iterrows():
        pool_id = row["pool_id"]
        chain = row["chain"]
        symbol = row["symbol"]
        project = row["project"]
        stablecoin = row["stablecoin"]
        count = row["count"]
        try:
            for attempt in range(max_retries):

                response = requests.get(f"https://yields.llama.fi/chart/{pool_id}")

                if response.status_code == 200:
                    historical_data = response.json()["data"]
                    pool_history_df = pd.DataFrame(historical_data)

                    # Add metadata to each historical entry
                    pool_history_df["pool_id"] = pool_id
                    pool_history_df["chain"] = chain
                    pool_history_df["symbol"] = symbol
                    pool_history_df["project"] = project
                    pool_history_df["stablecoin"] = stablecoin
                    pool_history_df["count"] = count

                    # Append to the main historical DataFrame
                    historical_df = pd.concat(
                        [historical_df, pool_history_df], ignore_index=True
                    )
                    break  # Exit retry loop on success

                else:
                    print(
                        f"Debug: API fetch failed for pool_id: {pool_id} - Status Code: {response.status_code}"
                    )
                    break

        except Exception as e:
            print(f"Attempt {attempt + 1} failed for pool_id: {pool_id}. Error: {e}")
            break
    return historical_df


def main():

    pooldf = process_pool_ids()
    # if pooldf.empty:
    #     print("No data found")
    # else:
    #     # Fetch and add historical data
    #     historical_df = get_historical_data(pooldf)

    #     # Save combined historical data to CSV
    #     historical_df.to_csv("data/pools_historical.csv", index=False)

    #     print("Historical data saved to data/all_pool_historical_data.csv")


if __name__ == "__main__":
    main()
