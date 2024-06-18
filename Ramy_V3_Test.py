import numpy as np
import threading
import keyboard

num_arrays = int(input("how much ram you want to test?")) + 2
print("HOLD Q TO STOP!")
input("Start? Press Enter")
while not keyboard.is_pressed('Q'):
  def process_array(data):
    return data * 20000 
  def process_data_threaded(data_list):
    threads = []
    results = []
    for data in data_list:
      result = threading.Thread(target=process_array, args=(data.copy(),))
      threads.append(result)
      result.start()
      results.append(result)
      print(result)
    for result in results:
      result.join()
  if __name__ == "__main__":
    data_size = 1024 * 1024 * 1024
    data_list = []
    for _ in range(num_arrays):
      data = np.full(data_size, 255, dtype=np.uint8)
      data_list.append(data)
  print(data)