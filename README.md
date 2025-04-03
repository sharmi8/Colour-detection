# Color Detection Project

## Introduction  
This project focuses on real-time **yellow color detection** using OpenCV. The goal is to accurately detect and identify yellow objects in an image or video stream.  

## Features  
- Detects yellow objects in real-time  
- Displays HSV and RGB values of detected yellow objects  
- Shows the color name and coordinates on the screen  

## Technologies Used  
- Python  
- OpenCV  
- NumPy  

## Setup Instructions  
1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/color-detection.git
   cd color-detection
   ```
2. Install dependencies:  
   ```bash
   pip install opencv-python numpy
   ```
3. Run the script:  
   ```bash
   python color_detection.py
   ```

## Problems Faced and Solutions  

### 1. **Laptop Not Detecting Yellow**  
   - **Issue:** The system was not detecting yellow properly.  
   - **Solution:** I ran a script to fix the central position and placed a yellow object in the center to observe its HSV values. After tuning the HSV range, we successfully detected yellow.  

### 2. **General Errors Encountered**  
   - **Incorrect HSV Range:** Yellow was not detected properly initially. Adjusting the HSV thresholds fixed this issue.  
   - **Low Camera Resolution:** The webcam's low quality affected detection accuracy. Adjusting brightness and resolution improved results.  
   - **Frame Lag:** The detection caused noticeable lag. We optimized the script by resizing frames and using efficient OpenCV functions.  

## Usage  
- Place a **yellow** object in front of the camera.  
- The program will detect yellow and display its HSV and RGB values in real time.  
- Modify the HSV values if needed for better accuracy.  


## Contributing  
Feel free to fork the repository, create a feature branch, and submit a pull request.  

## License  
This project is licensed under the MIT License.


