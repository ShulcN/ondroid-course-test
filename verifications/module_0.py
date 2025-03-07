import cv2
from auto_tests.base import Result 


def draw(frame, testData, robot):
  if not testData:
    testData = {"counter": -1}
  testData["counter"] += 1
  text_for_output = f"Counter value: {testData['counter']}"
  frame = cv2.putText(frame, text_for_output, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 
    1, (0, 0, 255), 2, cv2.LINE_AA)
  result = Result(True,"Perfect!",score=100)
  return frame, testData, text_for_output, result
  
