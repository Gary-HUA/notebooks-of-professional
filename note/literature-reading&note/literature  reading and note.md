### literature  reading and note

~~~python
---general terms:
    HAR: human activity recognition
    HCI:human computer interaction
    VR:virtual reality
    LBP:local binary pattern 
    BOW:bag of words model
    GP:genetic programming
    VAE:variational auto encoders
    GAN:generative adversarial networks
    DNN:deep neural networks
    CNN:convolutional neural networks
    RNN:recurrent neural networks
    SVM:support vector machine
    HMMs:hidden Markov models
    MCAD:multi-camera action dataset
    
    
~~~

~~~python
---basic concepts:
    1 "HAR systems" attempt to automatically analyze and recognize such HAs using the acquired information from the various types of sensors
    2."application fields of HAR":HCI,VR,security,video surveillance,home monitoring,processes in industry,devices control,extraction of information from video,robotics,video game,medical environments patient moniting,
    3."activity type":gestures, behaviors(action),interaction(activity),group actions, events.
~~~



#### topic 1:(2020)vision -based human activity recognition: a survey   

Author: Djamila Romaissa Beddiar1,3 Abdenour Hadid3· Brahim Nini1 · Mohammad Sabokrou2 ·Abdenour Hadid3

~~~python
1--- primary thesis:
    the paper attempt to review and summarize the progress of HAR systems from the computer vision perspective. the current survey aims to provide the reader and up to date analysis of vision-based HAR related literatureand will highlight the main challenges and future directions. 
2--- Critical components of the argument that support the thesis:
    2-1:HAR systems is divided two mian streams of "HCI":(1)contact-based (2)remote method:
    2-2:HAR approaches are composed of  three inportant components:(1)video frame segmentation for action detection.(2)action exteact and 		representation (3)learning process that recognizes these action.
    2-3 HAR feature extraction process:
        (1)hand-crafted features:rely on human ingenuity and prior knowledge to extract discriminating feature.
            spatial(body models,image models,spatial statistics)-temporal(action grammars,action templates,temporal statistics), 				    appearance-based,LBP,fuzzy logic etc.
        (2)feature learning: 
            traditional approaches:dictionary learning(BOW),GP and Bayesian network;
            deep-learning:
                (1)generative methods:auto-encoder,VAE,GAN
                (2)discriminative methods:DNN,RNN,CNN
                (3)bybrid models
      2-4 HAR approaches according to the recognition stages:
        human activity recognition system are in general composed of three main steps:
            (1)detection:skin color,shape,pixel values,3D models,motion,anisotropic-diffusion(异性扩散),
            (2)tracking:template based mothods(features tracking based on the correlation,contours based tracking,),optimal 						estimation,particle filters,Cam shift   
            (3)classification:SVM,Naive Bayesian classifier,algorithm of K_nearest neighbour,K_mean,mean shift clustering, machines 					finite state,HMMs,dynamic time warping,neural networks, 
	  2-5 HAR according to the source of the input data
    		(1)uni-modal methods
    		(2)multi-modal methods
       2-6 HAR approaches according to the machine learning supervision level
    		(1)supervised methods
             (2)unsupervised methods
             (3)semi-supervised methods
        2-7 dataset:
            (1)action level:KTH,Weizmann,stanford40,IXMAS,MSR,
            (2)behavior level:VISOR,Caviar,MCAD
            (3)interaction level:MSR daily,50 salads,MuHAVI,UCF50,UCF Sports,ETISEO,olypic sports,UT-interaction,UT-tower,
            (4)group activities level:ActivityNet Dataset,The Kinetics Human Action Video Dataset,HMDB-51,Hollywood dataset,Hollywood2 					,UCF-101,YouTube Action Dataset,Behave dataset,Video Web Dataset
         
~~~

#### topic 2:(2020)A survey on video‑based Human Action Recognition: recent updates, datasets, challenges, and applications

Author: Preksha Pareek1 · Ankit Thakkar1

~~~python

~~~











































