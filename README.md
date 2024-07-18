# Speedtest CLI Python Script

This Python script uses the `speedtest-cli` library to measure the internet connection speed by checking the download, upload, and ping speeds. It also retrieves information about the best Speedtest server based on ping.

## Prerequisites

- Python 3.x

## Installation

Before running the script, you need to install the `speedtest-cli` library. You can install it using `pip` or `pip3`:

```bash
pip install speedtest-cli
```

or

```bash
pip3 install speedtest-cli
```

## Usage
Clone this repository or download the script.

Ensure you have installed the speedtest-cli library as mentioned in the installation section.

Run the script using Python:

```bash
python3 perform_speedtest.py
```

## Example Output

```bash
Best Server: {'host': 'xyz.example.com:8080', 'latency': 10.123, 'name': 'City', 'country': 'Country', 'sponsor': 'ISP', 'id': '1234', 'url': 'http://xyz.example.com/speedtest/upload.php', 'd': 10.123, 'lat': 12.345, 'lon': 67.890}
Ping: 10.12 ms
Download Speed: 123.45 Mbps
Upload Speed: 67.89 Mbps
```