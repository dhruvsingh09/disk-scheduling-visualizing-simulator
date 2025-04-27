🧠 Disk Scheduling Simulator
This is a Streamlit web application that visually simulates various Disk Scheduling Algorithms with an animated graph! 🚀
It helps you understand how disk head movement happens for different algorithms like FCFS, SSTF, SCAN, CSCAN, LOOK, and CLOOK.

✨ Features
Choose from 6 disk scheduling algorithms.

Input custom disk request queues and initial head positions.

Animated visualization of head movement over time.

Displays the total seek time after simulation.

Clean and simple Streamlit-based interface.

📜 Algorithms Implemented
FCFS (First-Come, First-Served)

SSTF (Shortest Seek Time First)

SCAN (Elevator Algorithm)

CSCAN (Circular SCAN)

LOOK

CLOOK (Circular LOOK)

🚀 How to Run
Clone the Repository

bash
Copy
Edit
git clone https://github.com/dhruvsingh09/disk-scheduling-simulator.git
cd disk-scheduling-simulator
Install Requirements Make sure you have Python 3 installed. Then install the dependencies:

bash
Copy
Edit
pip install streamlit matplotlib pillow numpy
Run the App

bash
Copy
Edit
streamlit run app.py
The app will open automatically in your browser!

🛠️ File Structure
bash
Copy
Edit
📦 disk-scheduling-simulator
 ┣ 📄 app.py          # Main Streamlit application file
 ┗ 📄 README.md       # Project documentation
 
📈 How it Works
Enter the request queue (comma separated values) and initial head position.

Select the algorithm you want to simulate.

Click on Simulate.

The app generates:

An animated graph of the disk head's path.

The total seek time calculated for the algorithm.

The animation is first saved as a temporary GIF file, then displayed in Streamlit, and finally deleted automatically.

🧩 Tech Stack
Python

Streamlit (Web App)

Matplotlib (Plotting & Animation)

Pillow (Saving animations as GIFs)

NumPy (Array operations)


⚡ Author
DHRUV SINGH

