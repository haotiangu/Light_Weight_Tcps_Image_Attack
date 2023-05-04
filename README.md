# Light_Weight_Tcps_Image_Attack
                            
Online image attack simulaiton video can be found here -> https://www.youtube.com/watch?v=mLpQ3nOqwrU

## Dependency

- [Ubuntu 18.04](https://releases.ubuntu.com/18.04/)
- [ROS melodic](http://wiki.ros.org/ROS/Installation)
- [Anaconda](https://www.anaconda.com/products/distribution#linux)
- [Pytorch](https://pytorch.org/get-started/locally/)
- [Airsim](https://microsoft.github.io/AirSim/airsim_ros_pkgs/)
- [Unreal Engine](https://github.com/EpicGames/UnrealEngine)

Please follow the tutorial in Wiki to configure the [simulation environment](https://github.com/haotiangu/Robost_Vision_Based_Object_Tracking_System_Demo/wiki/The-General-Configuring-Tutorial-of-The-Simulation-Environment).

The yolo version in use is 5.6.1.




## Compile and Run the package



1. Activate the ros environment:
```
conda activate ros_env
```


2. Download the file.

```
cd ~/catkin_ws/src
git clone git@github.com:haotiangu/Robost_Vision_Based_Object_Tracking_System_Demo.git
cd ..
```
3. Install the dependent software byb following the wiki


```
catkin_make
```

4.  Source the file before running the launch package.
```
source ~/catkin_ws/devel/setup.bash
```


5. Run the launch file:
```
roslaunch tcps_image_attack autoflight.launch # object tracking to move demo
roslaunch tcps_image_attack train.launch # attack the object localization  
roslaunch tcps_image_attack train_denoiser.launch # object tracking to move when attack exist
```
