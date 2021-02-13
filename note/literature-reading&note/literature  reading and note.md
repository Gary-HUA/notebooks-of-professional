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
    ML: machine learning
    DL: deep learning
    STIP:space-time interest point temporal domain information is added to spatial ones.
    HOVW:histogram of visual word.
    HOG:histogram of oriented gradient
    HOF:histogram of optical Flow
    HOMB:histogram fo Motion Boundary
    LSTM:long short-term memory
    DBN:deep belief network
    
    
    
~~~

~~~python
---basic concepts:
    1 "HAR systems" attempt to automatically analyze and recognize such HAs using the acquired information from the various types of sensors
    2."application fields of HAR":HCI,VR,security,video surveillance,home monitoring,processes in industry,devices control,extraction of information from video,robotics,video game,medical environments patient moniting,video retrieval,entertainment,education,abnormal activity identification,
    3."activity type":gestures, behaviors(action),interaction(activity),group actions, events.
    4. "acquired device": sensors with RGB,range,radar,or wearable sensors,
~~~

~~~idea
---idea:
	depth iamge based segmentate body (head,arm,leg)<it is an important part of moveing bady,such as "eating"，it is associated by head,arm and hand with tools  吃饭的动作需要头，胳膊+收，的配合 >
	local feature(partial of body , the main aim is arm+hand , and leg ,head)
	classification/identifacation :head+arm,arm+leg,
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
   key&idea or shortage/increase
         
~~~

#### topic 2:(2020)A survey on video‑based Human Action Recognition: recent updates, datasets, challenges, and applications

Author: Preksha Pareek1 · Ankit Thakkar1

~~~python
1.primary thesis:
    in this paper, we have discusses various ML and DL techniques for HAR,challenge,public dataset, future directions in HAR
2.Critical components of the argument that support the thesis:
    2-1:prior survey
        (1)still image-based action recognition  low-level feature extraction and high-level representation for action.
        (2)action representation and analysis based HAR
        (3)abnormal activity detection
        (4)sensor based activity recognition
    2-2:complete process:
        (1)action representation:involves the extraction of a set of features form lacal/global feature.
        (2)feature extraction and encoding:STIP,trajectory based,depth based,pose based RGB-D(2D,3D),motion based,shape based,hybrid(shape+motion)
    2-3:discussion: 
            traditional ML depend on handcrafted featuer representation.STIP feature are suitable for simple action and gestures,
            the trajectory based method can analyze movements robust to view-invariant manner.
            depth sensor,action detection is simpler and effective than using RGB data.advanced human pose estimation algorithms can make 			 it easier to gain accurate 3D skeleton data.
       
    
~~~











































