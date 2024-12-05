# **Lesson 1: Sandbox**

## **Objective**  
Test the setup of the ESP32 microcontroller and familiarize yourself with basic peripheral control.


## **Introduction**  

In this setup, you have access to some peripherals, including a **seven-segment display**, which allows you to display numeric values.  

Below is an image of the seven-segment display:  

![Seven-Segment Display](https://github.com/autolab-fi/course-template/blob/main/images/module-1/image_for_lesson_1.jpg?raw=true)  

### **How the Display Works**  
You can control each segment of the display by sending **HIGH** or **LOW** signals to the following pins on the ESP32:  

| **Segment Pin** | **ESP32 Pin** |
|:---------------:|:-------------:|
| A               | 19            |
| B               | 21            |
| C               | 25            |
| D               | 27            |
| E               | 33            |
| F               | 23            |
| G               | 22            |
| Decimal Point   | 26            |

Each pin corresponds to a specific segment of the display. By activating the correct combination of segments, you can display numbers from 0 to 9.


## **Assignment**  

1. **Basic Task:**  
   Display any number (0–9) on the seven-segment display.  

2. **Challenge Task:**  
   Make the displayed number **blink** by alternating between turning it on and off with a 1-second delay.

### **Hints:**  
- Use the GPIO library in the Arduino IDE or another preferred programming environment to control the pins.  
- You can use the `digitalWrite()` function to set a pin HIGH or LOW.  
- To implement blinking, use the `delay()` function to create a pause between turning the display on and off.


## **Conclusion**  
Once you have successfully displayed and blinked the number, the test is complete.  

In this lesson, you’ve:  
- Set up and tested the ESP32.  
- Controlled a seven-segment display.  
- Created a simple blinking effect.  

You are now ready to move on to more advanced peripheral control!
