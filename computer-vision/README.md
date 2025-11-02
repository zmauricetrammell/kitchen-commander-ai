# Kitchen Commander Computer Vision Subsystem

## Goal
The goal of this subsystem is to perceive and understand the current game state in near real time. The input will be a video stream of the game. The output will be a game state matrix representing the current game state.

## Success Criteria
- [ ] Must take in live video stream from the game.
- [ ] Must be able to detect and track all interactable or relevant objects in the game 99% of the view time.
- [ ] Must process faster than or equal to human perception (30 FPS).
- [ ] No modifications can be made to the game platform or hosted device.
- [ ] Must be deployable on an embedded GPU system.

## Plan of Action
1. I'll be using an HDMI capture card to stream the live game feed to an external computer over USB 3.0.
2. Next, I'll train a yoloV8 model on a custom Overcooked data set. It will be exported to a Jetson Orin Nano for deployment.
3. Lastly, I'll design and implement a game state matrix format that represents all the relevant resources, locations, characters, and everything else in the game. This will need to be published to all of the computers in the network.

The input is USB video feed.
The output is a light weight game state data structure thats easy to parse.

## Execution

### Log 01 November 2025
I have more questions than answers at this point. I intend to use the "YOLO" object detection model for this project because it is open source, relatively light weight, lightning fast, and very accurate. I want to do this myself and control the quality of the model to eliminate errors in the overall complex system so I want to train a model on a custom data set I collect, manage, and label myself. I also want to test and compare the parameters in the different generations, sizes, and training choices between each model to balance performance, speed and size.  

Up front, I have these questions:
1. How can I collect data for overcooked and label it to train and test a YOLO model?
2. Which YOLO model has the best performance, size, speed balance for my project constraints?
3. How can I implement a smooth training pipeline that isnt compute intensive and slow?

I found this awesome tutorial video for a smaller project: https://youtu.be/r0RspiLG260?si=4l_HoHRc8aW-lMRC (Credit to Edje Electronics). It makes use of Google Colab. This is a great option to reduce my compute requirements. I can aggregate a dataset, train a model, and test it all in a Colab notebook without needing to tax my own hardware and manage a bunch of dependencies.

**Starting My Dataset**  
I'll start with collecting data for a dataset. How big should it be? Reddit and Stack Overflow seems to suggest 1000 - 1500 minimum for each class (this will be very time intensive and laborious, let's see if there are any optimizations or if I can come up with a quick and efficient workflow).

I'll start with 100-200 images for each class. I'll pull them directly from the game video stream. Since I'll be working with the dataset in the cloud, I'll collect it in cloud storage in Google Drive.

#### Goal - Collect Images of Overcooked For An Image Dataset  
I'll collect at least 100 images of each of the classes I want to detect.

First, I need to delineate all of the classes so that I know what I need to collect images of. I'll make a classes.txt list of classes.


## Reflection
