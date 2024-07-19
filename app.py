import speedtest

def perform_speedtest():
    st = speedtest.Speedtest()
    
    # Get the best server based on ping
    best_server = st.get_best_server()
    print(f"Best Server: {best_server}")

    # Get ping (latency)
    ping = st.results.ping
    print(f"Ping: {ping:.2f} ms")

    # Get upload and download speed
    download_speed = st.download()
    upload_speed = st.upload()
    download_speed_mbps = download_speed / 1024 / 1024
    upload_speed_mbps = upload_speed / 1024 / 1024
    print(f"Download Speed: {download_speed_mbps:.2f} Mbps")
    print(f"Upload Speed: {upload_speed_mbps:.2f} Mbps")

if __name__ == "__main__":
    perform_speedtest()
