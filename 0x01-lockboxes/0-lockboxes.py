#!/usr/bin/python3
def canUnlockAll(boxes):
  # Initialize a set with the key for the first box
  keys = {0}
  # Loop until there are no more keys to try
  while True:
    # Keep track of the keys added in this iteration
    new_keys = set()
    # Loop through all the boxes
    for i, box in enumerate(boxes):
      # If we have the key for this box, add its keys to the new_keys set
      if i in keys:
        new_keys.update(box)
    # If no new keys were added, we are done
    if not new_keys - keys:
      break
    # Otherwise, update the keys set and continue
    keys.update(new_keys)
  # Return True if we have keys for all the boxes, False otherwise
  return len(keys) == len(boxes)
