# Point-to-Point Testing

## Overview
This Python script is designed to test the performance of point-to-point links in corridors over extended periods. By running continuous tests and collecting network data from a Ubiquity device's web interface, the script helps monitor the connection's stability and identify any significant changes or anomalies in the network performance. The data from both the `iperf3` tests and the ubiquiti's webpage status are logged into JSON files for further analysis.

## Key Operations
1. **Authentication with Ubiquity Device:**
   The script authenticates with the Ubiquity device via HTTP POST requests using a predefined username and password. A session is maintained throughout the data collection process using the `requests` library.

2. **Retrieving Network Data:**
   The script collects network-related data from the Ubiquity device, including:
   - `amdata`
   - `airviewdata`
   - `status`
   
   Each of these data points is saved in separate JSON files with a timestamp, ensuring accurate logging of the device's state at different times.

3. **Running `iperf3` Performance Tests:**
   The script runs several types of `iperf3` tests to evaluate the point-to-point link performance:
   - **TCP Test**: Measures TCP performance (send and receive rates).
   - **UDP Test**: Assesses UDP performance with a fixed bandwidth of 100 Mbps.
   - **Reverse TCP Test**: Runs a TCP test in reverse (client-side acting as server).
   - **Reverse UDP Test**: A reverse test to measure UDP performance with a fixed bandwidth of 100 Mbps.
   
   The results of each test are parsed to extract both the sending and receiving data rates.

4. **Saving Test Results:**
   All results from the `iperf3` tests are organized into a dictionary and saved into a JSON file, with a timestamp in the filename to track changes over time.

5. **Looping:**
   The script operates in an infinite loop, running tests and retrieving data every 10 seconds. This allows continuous monitoring of the point-to-point link, making it easier to detect any significant changes or performance issues.

## File Paths
The script organizes the fetched data and test results into different directories:`amdata_path`, `airview_path`, `status_path`, `iperf_path`.

## Dependencies
The script requires the following Python libraries:
- `requests`: For making HTTP requests.
- `json`: For handling JSON data.
- `time`: For handling delays.
- `subprocess`: For running `iperf3` commands.
- `os`: For interacting with the file system.
- `datetime`: For generating timestamps.

To install the necessary libraries:
```bash
pip install requests
```

Additionally, `iperf3` must be installed on the system where this script is executed.

## Usage
1. Set the appropriate `USER` and `PASS` values for authentication with the Ubiquity device.
2. Define the desired paths for storing data by modifying the `amdata_path`, `status_path`, `airview_path`, and `iperf_path` variables.
3. Run the script, and it will begin collecting data and performing network tests. Each cycle will log the results to new JSON files.

## Example Output:
For each cycle, the following files will be created:
- `amdata_data <timestamp>.json`
- `airview_data <timestamp>.json`
- `status_data <timestamp>.json`
- `iperf3_results <timestamp>.json`

Each file contains the respective data in JSON format, providing a detailed record of the point-to-point link performance and device status over time.

## Notes
- The script assumes the device is accessible at `https://10.1.1.2` and is using self-signed certificates (hence the `verify=False` in requests).
- Make sure to have proper permissions for writing to the directories specified in the script.
- Adjust the `iperf3` server IP (`10.1.1.10`) as needed for your environment.
