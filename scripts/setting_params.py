#!/usr/bin/env python3
import torch


### Here I will take rosparam that is name...

SETTING = {}
SETTING.update({'name': 'okokok'})
SETTING.update({'env_name': 'env3'})


# Yolo v5 parameter file path
SETTING.update({'yolov5_param_path':'yolov5s.pt'})

# Attack pertubation size
SETTING.update({'alpha': 0.05})

# Optimization learning rate
SETTING.update({'lr_img_gen':0.001, 'lr_img_discrim':0.0012, 'lr_sys_id':0.0032, 'lr_actor':0.0008, 'lr_critic':0.0016, 'betas':(0.5, 0.9)})

# Dimension of the data and the NN networks
#SETTING.update({'image_size':(448,448), 'encoder_image_size':(224,224)})
SETTING.update({'image_size':(448,448), 'encoder_image_size':(32,32)})
SETTING.update({'N_ACT_DIM': 4, 'ACTION_LIM':1.0, 'N_STATE_DIM': 32})

# Ornstein-Uhlenbeck
SETTING.update({'noise_theta':0.10, 'noise_sigma':0.2})

# Minibatch size and time window
SETTING.update({'N_MINIBATCH_IMG':5, 'N_MINIBATCH_DDPG':8, 'N_WINDOW':32})
SETTING.update({'N_SingleTrajectoryBuffer':1000, 'N_TransitionBuffer':1000, 'N_ImageBuffer':5000})

# Image attack loss function parameters
SETTING.update({'LAMBDA_COORD':0.001, 'LAMBDA_NOOBJ':0.001, 'LAMBDA_L2':10, 'LAMBDA_Var':1})

# Reward Choice
#SETTING.update({'reward_function': 'positive_distance'})
#SETTING.update({'reward_function': 'negative_distance'})
#SETTING.update({'reward_function': 'move-up'})
#SETTING.update({'reward_function': 'move-down'})
#SETTING.update({'reward_function': 'move-left'})
SETTING.update({'reward_function': 'move-right'})
#SETTING.update({'reward_function': 'go_to_target'})
#SETTING.update({'reward_function': 'collision'})



# N_Episodes
SETTING.update({'N_Episodes': 50})



FREQ_HIGH_LEVEL = 5
FREQ_MID_LEVEL = 10
FREQ_LOW_LEVEL = 15
filter_coeff = 0.1

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")