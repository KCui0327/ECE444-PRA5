import pandas as pd
import requests
import json
import csv
import time

url = "http://ece444-pra5-env.eba-v3qb2vkm.us-east-2.elasticbeanstalk.com/test"

def test_api():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
        
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Failed with status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    with open('test_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["Run", "Results", "Time (ms)"]
        writer.writerow(field)
        for i in range(100):
            start = time.perf_counter()
            result = test_api()
            end = time.perf_counter()
            perf = (end - start) * 1000
            writer.writerow([str(i+1), result, str(perf)])
        
    df = pd.read_csv('test_results.csv')
    df.boxplot(by ='Run', column =['Time (ms)'], grid = False) 



