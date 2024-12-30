# Angle Determination from Image

## Overview

This project is a small program that determines the angle of a rectangular or square-shaped object placed on a wooden table. By placing a white sheet in front of the table, the program can find the contours of the object in the image and calculate the angle based on its position.

## Features

- Detects contours of rectangular or square objects.
- Calculates the angle of the detected object.
- Simple and easy-to-use interface.

## Requirements

You can install the required libraries using pip:

```bash
pip install -r requirements.txt
```
This will install all the libraries with the versions that I used in my system.

Recommendation :- Please make a virtual environment and install the libraries inside it. This will help to have no clashes between present library version and installed library versions

### Making a virtual environment

```bash
python -m venv venv
source venve/bin/activate
pip install -r requirements.txt
python server/server.py
```


## File Structure

Here is the recommended file structure for this project:

```bash
project-root/
├── README.md
├── src/
│   ├── main.py
│   └── output_logic.py
└── sample_input/
    └── sample_image.jpg
```

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/Manas-Suri/Angle_Calculator.git
cd Angle Calulator
```

2. Prepare Your Image: Place a white sheet in front of a wooden table and take a picture of a rectangular or square object on the table. Save the image in the sample_input directory as sample_image.jpg.
3. Run the Program:

Navigate to the src directory and run the program:

```bash
python main.py
```

4. View the Output: The program will display the source image and the calculated angle based on the detected contours.

## Usage

- Ensure that the object you want to measure is clearly visible in the image.
- The program will automatically detect the contours and calculate the angle.

## Contact

manassuri1998@gmail.com