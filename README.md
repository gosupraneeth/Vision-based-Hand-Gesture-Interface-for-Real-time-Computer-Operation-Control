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
