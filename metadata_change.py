#! /usr/bin/python

import os
from datetime import datetime
from subprocess import call
from exif import Image

# List of Formats where the date should be changed
list_of_files=["jpeg","JPG","png"]

def extract_original_datetime(file_name, path):
    
    img_path = create_image_path(file_name, path)

    with open(img_path, 'rb') as img_file:
        img = Image(file).datetime_original
    
    return img


def extract_file_ending(file):

    file_ending = file.split(".")[-1]

    return file_ending


def create_image_path(file_name,path):
    img_path = f'{folder_path}/{file}'

    return img_path


def reformat_date_and_time(orginial_date_string):
    
    
    orginial_date_datetime = datetime.strptime(orginial_date_string, '%Y:%m:%d %H:%M:%S')
    
    correct_date_string = datetime.strftime(orginial_date_datetime, '%Y/%m/%d %H:%M:%S')
    
    correct_day = correct_date_string[:10]
    correct_time = correct_date_string[-8:]
    
    return correct_day, correct_time


def create_list_of_all_files(folder_path):
    
    list_of_all_files = os.listdir(folder_path) 
    
    return list_of_all_files




if __name__ == '__main__':
    
    # get current folder paht
    folder_path = os.getcwd()
      
    # Iterate over each file in folder
    for idx,file in enumerate(create_list_of_all_files(folder_path)): 

        # Handling of non-jpeg in folder
        file_ending = extract_file_ending(file)

        print(file_ending)

        if not(file_ending in list_of_files):
            print("True")
            continue

        else:
            print(f"Changing Date from file: {file}")

            # open jpeg
            image_date_original = extract_original_datetime(file, folder_path)

            print(image_date_original)
            # Convert datetime
            correct_day, correct_time = reformat_date_and_time(image_date_original)
            
            # Create the image path
            image_path = create_image_path(file, folder_path)

            # Create the file path
            file_path = folder_path + '/' + image_path

            command = 'SetFile -d ' + f'"{correct_day} "' + f'{correct_time} ' + file_path
            print(f"Successfully changed the creation date from {file}")
            call(command, shell=True)
 
