# Kitchen Commander Computer Vision Subsystem

## Goal
The goal of this subsystem is to perceive and understand the current game state in near real time. The input will be a video stream of the game. The output will be a game state matrix representing the current game state.

## Plan of Action
1. I'll be using an HDMI capture card to stream the live game feed to an external computer over USB 3.0.
2. Next, I'll train a yoloV8 model on a custom Overcooked data set. It will be exported to a Jetson Orin Nano for deployment.
3. Lastly, I'll design and implement a game state matrix format that represents all the relevant resources, locations, characters, and everything else in the game. This will need to be published to all of the computers in the network.

The input is USB video feed.
The output is a light weight game state data structure thats easy to parse.

## Execution

## Reflection
