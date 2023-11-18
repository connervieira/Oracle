print("Loading...")

import os # Required to interact with certain operating system functions.
import json # Required to process JSON data.

root_directory = str(os.path.dirname(os.path.realpath(__file__))) # This variable determines the path of the root directory.
config = json.load(open(root_directory + "/config.json")) # Load the configuration database from config.json

import time
import base64 # Required to encode images.
import requests # Required to make network requests.


while True:
    print("Capturing...")
    os.system("fswebcam -d " + str(config["image"]["camera"]["device"]) + " -r " + str(config["image"]["camera"]["resolution"]) +  " " + str(config["image"]["path"]) + " > /dev/null 2>&1")

    print("Uploading...")
    if (os.path.exists(config["image"]["path"]) == True): # Check to make sure the captured image file actually exists before attempting to upload it.
        with open(config["image"]["path"], 'rb') as image_file: # Open the image file.
            encoded_image_file = str(base64.b64encode(image_file.read())) # Read the image file, encoded as base 64, and convert it to a string.

        if (encoded_image_file[0:2] == "b'"): # Check to see if the string has characters indicating that it is a bytes literal.
            encoded_image_file = encoded_image_file[2:-1] # Remove the first two characters and last single character, since they only serve to indicate that the string is a bytes literal.

        image_submission_information = {"image": encoded_image_file, "identifier": config["network"]["identifier"] } # Prepare the image information bundle.
        raw_image_submission_information = json.dumps(image_submission_information) # Convert the image information bundle into a string.

        for target in config["network"]["targets"]: # Iterate over each target set in the configuration.
            request = requests.post(target, data={"image": raw_image_submission_information}, timeout=20) # Submit the JSON string of the image information to the specified target.

    else:
        print("Error: The captured image could not be uploaded, since the file does not exist.")

    print("Delaying...")
    time.sleep(config["general"]["interval"])
