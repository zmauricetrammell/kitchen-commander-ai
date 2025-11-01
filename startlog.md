# KITCHEN COMMANDER - MULTI-AGENT AI 

## My Goal:
I want to build a multi-agent AI system that can surpass humans in the Overcooked2 videogame. I want it to organize itself like a classically trained kitchen team.

## My Plan of Action:
In order to max Overcooked, I need to accomplish a few things.

1. Create a method for this system to interact with the game console (a Nintendo Switch)
   Like this:
   [INSERT DIAGRAM]

   NINTENDO -----(computer vision)------> THIS   
   SWITCH <----(console control inputs)- SYSTEM

   This can be broken up into two subsystems:
   
   **Subsystem 1**: Computer Vision - Game Perception  
   This is the ability for the system to "see" what is going on in the game. (I could do this with a camera watching the TV screen - but I'm not a sadist so I wont).
   - I plan to use an HDMI Capture Card to stream the game into the system over USB. This leverages the existing I/O interfaces of the console.
   - Next, I'll need to create a way for the system to understand what it's seeing (so I can teach it to do stuff...). This is the object detection sub-subsystem. The system needs to detect key items and locations (also the characters) to "make sense" of the game visuals that are streamed to it.
   - Have you played overcooked? The cute cartoon co-op cooking game? Let's walk through the sparknotes game loop:
     You: <img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/21f44646-b76c-49fd-be38-45796ff6ef1f" />
     and 3 friends: <img width="75" height="100" alt="image" src="https://github.com/user-attachments/assets/5e569280-97c4-4a8e-8ec0-4c11819e86c0" />
     are chefs in a tiny cartoon kitchen:
     <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/04904b75-071f-461e-a7e4-b01cc40fd9c6" />

     You get orders: <img width="300" height="100" alt="image" src="https://github.com/user-attachments/assets/467ceb69-41b3-49cd-b028-d437cbd06298" /> and you identify ingredients: <img width="100" height="100" alt="image" src="https://github.com/user-attachments/assets/f1138fa7-8519-486d-947d-42e984b5038a" /> go get them, find the closest appliance <img width="102" height="101" alt="image" src="https://github.com/user-attachments/assets/4408d4aa-f213-4af8-b8f7-61f7bbe624b4" /> (like a burner) and do a cooking thing. You and your team do this for every ingredient until you're ready to find a plate <img width="51" height="46" alt="image" src="https://github.com/user-attachments/assets/0d978eb8-f87d-4ad4-a625-a1004db772cd" /> and put the meal on it. Once plated, you take the finished order to the order window <img width="95" height="123" alt="image" src="https://github.com/user-attachments/assets/d87f011c-f35c-4d8e-85c3-244f7eece329" />.

   - In order for a computer to make sense of the picture of the game, I'll train a computer vision model to recognize specific items relevant to gameplay.
     As an output, I'll make a board or matrix with symbols that correspond to all of the key resources, applicances, locations, character positions, and obstacles.
     A map like this: <img width="1400" height="788" alt="image" src="https://github.com/user-attachments/assets/ef118453-8ca5-44ad-b051-4f421c880d6b" />

     could be represented SOMETHING like this:  
     WALL , FIREEX. , COUNTER , CUTB.  , CUTB. , CUTB. , COUNTER , COUNTER , COUNTER , ORDER WINDOW , ORDER WINDOW , COUNTER , WALL ;
     WALL ,                                                                                                                    WALL ;

     WALL     ,         ,         ,        , COUNTER, FISH , NORI    ,                            ...                                   ;



     WALL , COUNTER , COUNTER , COUNTER , COUNTER,TRASH, COUNTER , BURNER , BURNER , BURNER , COUNTER , COUNTER , WALL;

     **Subsystem 2**: Game Control - Controller Inputs  
     I need to create a method of controlling the game from my system.
     - Since this will be played on Steam on a PC, I'll be emulating usb keyboard inputs and combining them using a USB hub to multiplex the 4 control input streams into the 1 PC.
     - To accomplish USB keyboard emulation, I'll use 4 Arduino microcontrollers for USB control.
     
     

     
 








     
   
