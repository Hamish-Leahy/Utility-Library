import subprocess
import os
import time

def capture_packets(interface="Wi-Fi", duration=60, filename="capture.pcapng", filter=""):
    """
    Captures network packets using Wireshark's TShark (command-line version)

    Args:
        interface: Network interface to capture on (e.g., "Wi-Fi", "eth0").
        duration: Capture duration in seconds.
        filename: Name of the output file to save the capture.
        filter: Optional Wireshark display filter to apply (e.g., "http").
    """

    tshark_cmd = [
        "tshark",
        "-i", interface,          # Capture on the specified interface
        "-a", f"duration:{duration}", # Capture for the given duration
        "-w", filename             # Save to the specified file
    ]

    if filter:
        tshark_cmd.extend(["-Y", filter])  # Apply the filter if provided

    try:
        print(f"Capturing packets on '{interface}' for {duration} seconds...")
        subprocess.run(tshark_cmd, check=True)
        print(f"Capture complete. Saved to '{filename}'")

    except FileNotFoundError:
        print("Error: TShark command not found. Make sure Wireshark is installed and in your PATH.")
    except subprocess.CalledProcessError:
        print(f"Error: TShark failed to capture packets. Check interface name and permissions.")

# Example usage
if __name__ == "__main__":
    interface_name = input("Enter interface to capture on (default: Wi-Fi): ") or "Wi-Fi"
    capture_duration = int(input("Enter capture duration in seconds (default: 60): ") or 60)
    capture_filename = input("Enter filename for the capture (default: capture.pcapng): ") or "capture.pcapng"
    capture_filter = input("Enter optional display filter (press Enter to skip): ") 

    capture_packets(interface_name, capture_duration, capture_filename, capture_filter)
