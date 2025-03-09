import cv2
import time

def text(frame, testData, robot):
  if not testData:
    testData = {
      "end_time": time.time()+20
    }
  text_for_output = "Module 1. Task text robo"
  frame = robot.draw_info(frame)
  frame = cv2.putText(frame, text_for_output, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
  result = {
    "success": True,
    "description": "Perfect 2!",
    "score":100
  }
  return frame, testData, text_for_output, result
  
