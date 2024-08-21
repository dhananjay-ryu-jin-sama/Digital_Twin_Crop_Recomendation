import serial
import requests
import time

# Constants
API_URL = "https://api.thingspeak.com/update"
API_KEY = "MEANKEDTWORSX600"  # Replace with your actual API key
SERIAL_PORT = '/dev/ttyACM0'  # Adjust to your serial port
BAUD_RATE = 4800
TIMEOUT = 1

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=TIMEOUT)

try:
    while True:
        # Read data from Arduino
        data = ser.readline().decode('utf-8').strip()
        print("Received data from Arduino:", data)

        # Split data into readings
        readings = data.split()

        # Check if we have the expected number of readings
        if len(readings) >= 5:
            # Assign readings to variables
            N, P, K, PH, Moisture, Temp = readings

            # Prepare data to send to ThingSpeak
            data_to_send = {
                'api_key': API_KEY,
                'field1': N,        # Example field mapping
                'field2': P,
                'field3': K,
                'field4': PH,
                'field5': Moisture,
                'field6': Temp
            }

            # Send data to ThingSpeak
            response = requests.post(API_URL, params=data_to_send)

            if response.status_code == 200:
                print("Data sent successfully")
            else:
                print(f"Failed to send data to ThingSpeak. Status code: {response.status_code}")
                print(response.text)
        else:
            print("Invalid data")

        # Wait for 5 seconds before the next read
        time.sleep(5)

except KeyboardInterrupt:
    # Clean up and close serial port on keyboard interrupt
    ser.close()
    print("Data collection ended.")