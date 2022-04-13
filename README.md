# Computer Controlling Operations using Hand Gestures
## How to start
There three folders names **_models_**, **_main_** and **_model_train_**. 
In the _models_ folder there are different versions and experimented models. 

In the _main_ folder there are working files which need to be run in the terminal or idle where the device has the direct access to the camera.

_model\_train_ folder has the notebook where the model is trained with data, it also has the details of the data and the model.

To start the application
> In the terminal if in current folder

`` cd main ``
  
`` python start_app.py``


> using idle or some python iterpreters 

 directly run the _start_app.py_ file.

## How it works

After running the python file it will loads the model and starts the primary camera available.

when the hand is captured in the camera then it will take the frame of it and passes to media-pipe to get the skeleton data. 

This data is inputted to model loaded and predicts the gesture.

Based on the gesture recognised it will makes the action using the Pyautogui.

## How to use

When the file is running and camera is on, you need to show the gesture to it.

The gestues are:

<img src="https://user-images.githubusercontent.com/59569250/163226890-0485aeab-f61e-4fe3-b94a-4de898217503.png" width="100" height="100"> &emsp; Pointer

<img src="https://user-images.githubusercontent.com/59569250/163226881-ab74c92a-46ad-4f2c-b0b8-0815e12565e5.jpg" width="100" height="100"> &emsp; Left Click

<img src="https://user-images.githubusercontent.com/59569250/163226895-98c96f23-0b97-4725-ab6c-2848622e88a6.jpg" width="100" height="100"> &emsp; Right Click

<img src="https://user-images.githubusercontent.com/59569250/163226869-4b91f761-92f2-4b6d-90ec-54a844e209c0.jpg" width="100" height="100"> &emsp; Left Arrow

<img src="https://user-images.githubusercontent.com/59569250/163226891-cf7cfd94-f2bc-4a85-8a2c-4be1a644daba.jpg" width="100" height="100"> &emsp; Right Arrow

<img src="https://user-images.githubusercontent.com/59569250/163226897-d84a8890-fc39-4db9-b296-44301eb60e90.jpg" width="100" height="100"> &emsp; Scroll Up

<img src="https://user-images.githubusercontent.com/59569250/163226896-314fd3ce-6529-4118-be76-da4b0a41274f.jpg" width="100" height="100"> &emsp; Scroll Down

<img src="https://user-images.githubusercontent.com/59569250/163226902-50279a35-d7ac-4e5a-8e76-120c1dd0c50c.jpg" width="100" height="100"> &emsp; Double Click

<img src="https://user-images.githubusercontent.com/59569250/163226907-38dedaa7-2104-44ed-901f-ff981fd58b1e.jpg" width="100" height="100"> &emsp; Hold And Drag

As the gestures mentioned above respective actions will takes place in your computer.


**_Enjoy the technology!_**
