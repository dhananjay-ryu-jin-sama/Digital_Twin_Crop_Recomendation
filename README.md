# Digital Twin Based Crop Recomendation System
In the face of growing global food demand and the challenges posed by climate change, optimizing agricultural practices has become crucial for sustainable development. The advent of digital technologies presents new opportunities to enhance decision-making in agriculture, leading to improved crop yields and resource management. One such innovative approach is the integration of digital twins into crop recommendation systems.

A Digital Twin is a virtual replica of a physical entity, capable of simulating and analyzing real-time conditions and behaviors. In agriculture, a Digital Twin can model various aspects of crop growth, soil conditions, weather patterns, and more, creating a dynamic and accurate representation of a farm's ecosystem.

# Components Used
Hardware Components : -
  1. Raspberry Pi Zero Two
  2. Arduino Uno
  3. NPK Sensor
  4. pH Sensor
  5. DHT Sensor

Software Components : -
  1. MATLAB
  2. ThingSpeak IoT

# Construction 
The sensors are connected to the Arduino Uno microcontroller, and the collected data is transferred to the Raspberry Pi via a bluetooth module. The Raspberry Pi uses its Wi-Fi connectivity to transfer data to the ThingSpeak IoT platform for data logging and analytics.

# Working Principle 
The Digital Twin of agricultural land is created by combining various soil data such as salt content (Sodium, Potassium, Phosporus), soil moisture level, pH ratio, location, weather report, and so on... This model is created by capturing continuous data from the field over time and generating it with MATLAB. In MATLAB, we utilized a CNN neural network to create a decision matrix to choose the optimum crop for that specific field given the forecasted weather and geographical characteristics. The crop recommendations are based on Tamil Nadu government data from the Tamil Nadu Agricultural University.

We have designed an interactive website that displays all soil data in real time.

