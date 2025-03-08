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
  frame = cv2.putText(frame, text_for_output, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
    1, (0, 0, 255), 2, cv2.LINE_AA)
  result = {
    "success": True,
    "description": "Perfect!",
    "score":100
  }
  return frame, testData, text_for_output, result
  
