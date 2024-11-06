import requests
import pandas as pd
import time


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


def get_historical_data(df, attempts=30):
    historical_df = pd.DataFrame()
    pool_ids = df["pool_id"].tolist()

    for pool_id in pool_ids:
        success = False
        for attempt in range(attempts):
            try:
                response = requests.get(f"https://yields.llama.fi/chart/{pool_id}")
                if response.status_code == 200:
                    historical_df["pool_id"] = pool_id
                    historical_data = response.json()["data"]
                    pool_history_df = pd.DataFrame(historical_data)
                    historical_df = pd.concat(
                        [historical_df, pool_history_df], ignore_index=True
                    )
                    success = True
                    break
                else:
                    print(
                        f"Debug: API fetch failed for pool_id: {pool_id} - Status Code: {response.status_code}"
                    )
                    break
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:
                    print(
                        f"Rate limit exceeded for pool_id: {pool_id}, attempt {attempt + 1}/{attempts}"
                    )
                    time.sleep(20)  # Increased sleep time to 20 seconds
                    continue  # Try again with the same pool_id
            except Exception as e:
                print(f"Attempt failed for pool_id: {pool_id}. Error: {e}")
                break

        if not success:
            print(
                f"Failed to fetch data for pool_id: {pool_id} after {attempts} attempts"
            )

    return historical_df


def main():

    pooldf = process_pool_ids()
    if pooldf.empty:
        print("No data found")
    else:
        # Fetch and add historical data
        historical_df = get_historical_data(pooldf)

        # Save combined historical data to CSV
        historical_df.to_csv("data/pools_historical.csv", index=False)

        print("Historical data saved to data/all_pool_historical_data.csv")


if __name__ == "__main__":
    main()
