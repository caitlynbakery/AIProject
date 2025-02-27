# Oppkey's RICOH THETA Used Car AI Workflow Optimizer

This is a code example for [article on RICOH THETA developer community](https://community.theta360.guide/t/using-ai-to-accelerate-used-car-sales-process/10494)

## Overview

Oppkey's RICOH THETA Used Car AI Workflow Optimizer is a web application that provides information on used cars. It uses a combination of natural language processing and machine learning to provide a personalized experience for each user, helping to optimize the workflow for used car sales professionals.

## Features

- Get information on a car by VIN through a user-friendly web interface
- Get recommendations for the car identified by the VIN
- Generate AI images of cars based on the VIN information
- Formatted HTML output for better readability
- Loading indicator for better user experience

## Technologies Used

- OpenAI API (GPT-4o and DALL-E 3)
- Python
- Flask web framework
- HTML/CSS/JavaScript

## Setup

1. Clone the repository
2. Install the dependencies `pip install -r requirements.txt`
3. Create a `.env` file and add your OpenAI API key `SECRET_KEY=your_openai_api_key`
4. Run the Flask application `python main.py`
5. Open your browser and navigate to `http://localhost:8000`

## Usage

1. Enter a VIN in the text box and click "Submit"
2. Wait for the AI to generate information and an image of the car
3. Review the detailed information and AI-generated image
4. Enter a new VIN to start a fresh query

## Example

![screenshot](./readme_assets/screenshot.jpg)

The web application provides detailed information about the vehicle, including:

1. **Body Style and Design**
2. **Performance**
3. **Range and Efficiency**
4. **Interior and Features**
5. **Safety and Technology**
6. **Recommendations**

Along with an AI-generated image of the vehicle at the top of the page.

## Web Interface Features

- Clean, responsive design
- Loading spinner during AI processing
- Formatted HTML output with proper paragraphs and lists
- Image display at the top of each response
- New queries automatically clear previous results

## Example Output

---

Example output from the helper is shown below:

---

Here is the detailed report for the vehicle with VIN **5YJSA1E40JF284143**:

## Vehicle Information

- **Year:** 2018
- **Make:** Tesla
- **Model:** Model S
- **Trim:** 75D

## Key Features

- **Engine Type:** Electric
- **Drive Type:** All-Wheel Drive (AWD)
- **Body Style:** Sedan
- **Battery Range:** Approximately 259 miles (EPA estimated for 75D trim)

## Performance

- **Horsepower:** Approximately 518 hp
- **0-60 MPH:** Around 4.2 seconds

## Interior & Technology

- **Seating Capacity:** 5 passengers
- **Interior Features:**
  - Premium heated front and rear seats
  - 17-inch touchscreen display
  - Navigation with real-time traffic updates 

- **Technology:**
  - Advanced Autopilot capabilities
  - Over-the-air software updates
  - Enhanced safety features with collision avoidance and automatic emergency braking

## Exterior

- **Standard Wheels:** 19-inch Slipstream
- **Lighting:** LED headlights and taillights
- **Panoramic Glass Roof**: Standard for a spacious feel

## Recommendations

- **Check Battery Health:** It's essential to review the battery's condition and charging history, as this impacts the vehicle’s range and performance.
- **Software Updates:** Ensure it has the latest software updates to benefit from improved features and security.
- **Service Records:** Verify regular service maintenance, particularly for the electric drive train and braking system.

## Additional Considerations

- **Warranty:** Check if the remaining warranty is transferable, which can be a significant advantage.
- **Autopilot Features:** Confirm the level of Autopilot capability, as this can vary based on software updates.

**Note:** The information is based on typical features for the 2018 Tesla Model S 75D, but specific features may vary. Always review the specific details with the seller or authorized dealership.
