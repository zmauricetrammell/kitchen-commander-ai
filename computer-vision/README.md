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
2. Next, I'll train a YOLOV8 model on a custom Overcooked data set. It will be exported to a Jetson Orin Nano for deployment.
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

I also need to delineate all of the classes so that I know what I need to collect images of. I'll make a classes.txt list of classes as I collect images.

#### Success Criteria - The Right Images and Enough
I need a lot of images to make a valuable dataset, the same icons in different contexts will diversify the training and create a better end result (apparently). I also need to make sure my model isnt stumped by anything within the game so I need an all inclusive dataset. I'll constrain it to one game area so I can make sure my approach works on a smaller set before trying to cover the whole game.

- [ ] Must contain 100 images of each class.
- [ ] List of classes mus cover every interactable item or obstacle in the game area.
- [ ] Must be pulled from the game (I wont use a pre-made data set).

#### Plan of Action - Play the Game, Get the Data As Play

1. I downloaded Overcooked on Steam and installed it on my PC.
2. I'll use a video recording tool to record my gameplay. I'll use OBS for this.
3. I'll extract frames in post processing.
4. As I play through the first cohesive game area, I'll add classes to "classes.txt" so I can annotate them later.

#### Execution

Install went smoothly. Here we go...  
<img width="700" height="433" alt="image" src="https://github.com/user-attachments/assets/fc0bad08-acd9-4518-8fa3-28b5c4f69af9" />

**Classes**  

A pattern I'm seeing right off the bat is that the key things can be broken into a few large groups:  
1. Resources: I view a "resource" as anything that a character can interact with and pick up/relocate. This includes pots, ingredients (not the ingredient crates), plates, and the fire extinguisher. These things need to be managed and are a part of the environment that can be influenced by planning and action.
2. Locations: a "location" cannot be moved by the character. It is a spot in the environment that has interactive significance. This includes the sink, the delivery window, cutting boards, burners, ovens, the trash can, and ingredient crates. Its a cool coincidence that locations cannot be walked through (so they dont need another special obstacle group). The significance of locations is that the character needs to be at them to perform a key action (get, chop, cook, etc).
3. Miscellaneous: all other stuff, it doesnt have interactive value but it should be tracked because it may pose an obstacle. This is any fires, walls, holes, all that stuff.
4. Icons: an "icon" tells the player useful information about the state of a resource or location. Examples are the "done" icon when an ingredient is fully cooked, a progress bar, or a "warning" icon when an ingredient is about to burn. I want to capture this so that eventually my agent can make creative decisions about the management of resources (maybe it will half cook things? Who knows).
  
I installed OBS Studio (from Steam) and set it up using all of the default settings and selecting to configure for recording over streaming. I set it to take the Overcooked game window as the video input steam. I'll also add it as the audio input stream (unsure if I'll need sound queues).

<img width="1634" height="1124" alt="image" src="https://github.com/user-attachments/assets/42c6f051-3001-450d-86f7-19081cdff1f1" />

This is all the setup I'll do today. Next I'll play the game, record my gameplay, and note the classes I encounter for my future annotation. 

## Reflection
