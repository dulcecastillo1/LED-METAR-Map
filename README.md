# ✈️ Metar Map: Real-Time Flight Visibility Display

## 🚀 Project Overview
**Metar Map** is a real-time flight visibility visualization system that retrieves live aviation weather data (METAR reports) from the [NOAA Aviation Weather API](https://aviationweather.gov/api/data/metar) and translates it into an **interactive LED display** using **NeoPixel hardware**.

This project was developed during my internship at **Reliable Robotics**, where I explored how **software and hardware systems communicate** to support aviation safety monitoring.

---

## ⚙️ Core Features
- **Real-Time Data Retrieval:** Uses Python’s `requests` library to fetch live METAR weather data for multiple Bay Area airports.  
- **API Integration:** Parses and processes aviation weather data from NOAA’s public REST endpoints.  
- **Embedded Systems Interaction:** Utilizes **CircuitPython** and **NeoPixel** libraries to display flight categories on an LED strip.  
- **Dynamic Color Coding:**  
  - 🟢 **Green:** Visual Flight Rules (VFR — clear skies)  
  - 🔵 **Blue:** Marginal VFR (MVFR — moderate visibility)  
  - 🔴 **Red:** Instrument Flight Rules (IFR — limited visibility)  
  - 🟣 **Purple:** Low IFR (LIFR — poor visibility)  
- **Automated Updates:** Refreshes all API requests and LED outputs every 5 minutes for continuous accuracy.  

---

## 🧩 Technical Stack
| Component | Description |
|------------|--------------|
| **Language** | Python |
| **Libraries** | `requests`, `neopixel`, `board`, `fractions` |
| **Hardware** | Adafruit NeoPixel LED strip, Raspberri Pi-compatible microcontroller |
| **Data Source** | NOAA Aviation Weather API (METAR reports) |
| **Environment** | CircuitPython runtime environment |

---

## 🧠 What I Learned
- Implemented real-world **API integration** for continuous data retrieval.  
- Developed foundational **embedded systems** skills by connecting software logic to physical hardware outputs.  
- Strengthened understanding of **data parsing**, **debugging**, and **real-time system design**.  
- Learned to visualize **aviation safety parameters** through data-driven outputs.  

---

## 🔧 How It Works
1. Sends HTTP GET requests to multiple airport METAR endpoints.  
2. Parses each text report to extract **visibility** and **ceiling height** data.  
3. Determines flight categories based on FAA-defined visibility thresholds.  
4. Lights up corresponding LEDs in different colors to represent live flight conditions.  
5. Waits five minutes, then repeats the process for updated data.  

---

## 🛠️ Future Improvements
- Add a **graphical dashboard** alongside the physical LED visualization.  
- Implement **JSON parsing** for more efficient and scalable data handling.  
- Add **error handling and logging** for API timeouts or incomplete responses.  

---

## 🌎 Demo Preview
<img width="496" height="594" alt="Screenshot 2025-10-18 at 3 00 26 PM" src="https://github.com/user-attachments/assets/820ea18c-7772-4599-b60a-d10e06ee5408" />
<img width="1414" height="594" alt="Screenshot 2025-10-18 at 3 00 11 PM" src="https://github.com/user-attachments/assets/6f3b2efc-b84c-4c18-8da6-50c662a196de" />

---

## 👩‍💻 Author
**Dulce Castillo**  
- Software Engineering Intern @ Reliable Robotics (Summer 2024)  
- Pursuing B.S. in Computer Science — Washington University in St. Louis  

---

## 🧭 Keywords
`Python` · `API Integration` · `Embedded Systems` · `CircuitPython` · `Raspberry Pi` · `Data Visualization` · `Aviation Weather` · `Hardware-Software Communication`
