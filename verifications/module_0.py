import cv2
import time

def draw(frame, testData, robot):
  if not testData:
    testData = {
      "counter": -1,
      "end_time": time.time()+10
    }
  testData["counter"] += 1
  text_for_output = f"Counter value: {testData['counter']}"
  frame = robot.draw_info(frame);
  result = {
    "success": True,
    "description": "Perfect!",
    "score":100
  }
  return frame, testData, text_for_output, result
  
