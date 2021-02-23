### literature  reading and note

#### general terms
~~~python
---general terms:
    HAR: human activity recognition
    HCI:human computer interaction
    VR:virtual reality
    LBP:local binary pattern 
    BOW:bag of words model
    BOVW:bag of visual words
    GP:genetic programming
    VAE:variational auto encoders
    GAN:generative adversarial networks
    DNN:deep neural networks
    CNN:convolutional neural networks
    RNN:recurrent neural networks
    SVM:support vector machine
    RVM:relevant vector machine
    HMMs:hidden Markov models
    CHMM:coupled HMM
    HSMM:hidden semi-Markov model
    MCAD:multi-camera action dataset
    ML: machine learning
    DL: deep learning
    STIP:space-time interest point temporal domain information is added to spatial ones.
    HOVW:histogram of visual word.
    HOG:histogram of oriented gradient
    HOF:histogram of optical Flow
    HOMB:histogram fo Motion Boundary
    LSTM:long short-term memory
    DBN:deep belief network/dynamic Bayesian network
    ROI: region of interest
    GMM:Gaussian mixture models
    STVs:3D space-time volumes
    DFT:discrete Fourier transform
    SIFT:scale-invariant feature transform
    SURF:speed-up robust feature
    CRFS:conditional random fields
    DBNs:deep belief networks
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
~~~
#### basic concepts
~~~python
---basic concepts:
    1 "HAR systems" attempt to automatically analyze and recognize such HAs using the acquired information from the various types of sensors
    2."application fields of HAR":HCI,VR,security,video surveillance,home monitoring,processes in industry,devices control,extraction of information from video,robotics,video game,medical environments patient moniting,video retrieval,entertainment,education,abnormal activity identification,health care,
    3."activity type":human activity have an inherent hierarchical structure that indicates the different levels of it,which can be considered as a three level categorization.first:for the bottom level, there is an atomic element and these action primitives constitute more complex human activity.  after action primitive level, the action/activity comes as the second level. finally ,the complex interaction from the top level,which refers to the human activity that involve more than two persons and objects.
    4. "acquired device": sensors with RGB,range,radar,or wearable sensors,
    5."human activity recognition(HAR)":aims to recognition activity from a series of observations on the action of subjects and the environmental conditions.
    6."global representation": global representation extract global descriptors directly from original videos or iamges and encode them as a whole feature.
    7."local representations":they focus on specific local patches which are determined by interest point detectors or densely sampling.most existing local features are proved to be robust against noise and partial occlusions comparing to global feature.
    8."human tracking":besides the activity calssification approaches,another critical research area is the human tracking approach,whch is concerned in video surveillance systems for suspicious behavior detection.for analyzing human behaviors and identifying potential unsafe or abnormal situations.
    9."sigle-layer method":single layer method present and recognition human activity directly based on sequence images.
    10."hierarchical layer method":describe high-level human activity by using simple activity called sub-event which are suitable for the  analysis of complex activity.
    11."semantic space":include human knowledge about activity such as body part(pose/poselet),object,scene,and attribute feature. we categorize semantic method into three categorise:method based on body part,method based on scene/object,method based on attributes.
    12."semantic define":Generally, semantics refers to what the sender and receiver of a
message mean and how they infer the context of the message. Semantics is the study of meaning.
In action recognition, the semantic understanding enables users to apply prior knowledge to the recognition process.
    13."deep belief network"(DBN):
    14.depth map images may contain occlusions, which make the global features unsettled. Additionally, contrasted with color images, the depth images do not have texture but it difficult to apply local differential operators like gradients on because they are generally too noisy in both spatial and tem- poral cases.
~~~

#### idea
~~~idea
---idea: A suppose: how accuracy and easier extract/represent an activity.
1. 动作的组成: 一个人的动作是由头,脖子,胳膊, 手,腿,脚等部分组合而成的,简单的就是H+A,A+L的组合构成.
	如果我们对人的动作进行分解,那么在行为检测和获取的时候,通过不同部分的检测组合识别,那么可以对动作进行更加精准的识别和分类.单个人得动作组合有他个人得习惯特性.不同人得动作具有相似性.我们通过对动作的组合检测.会不会由更高的识别率和分类准确度. 分离检测会不会更加高效相对于整理复杂计算.
	depth iamge based segmentate body (head,arm,leg)<it is an important part of moveing bady,such as "eating"，it is associated by head,arm and hand with tools  吃饭的动作需要头，胳膊+手，的配合 >
	local feature(partial of body , the main aim is arm+hand , and leg ,head)
	classification/identifacation :head+arm,arm+leg,
~~~

#### dataset

~~~python

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

#### topic3:(2017)A Review on Human Activity Recognition Using Vision-Based Method

Author: Shugang Zhang,1 Zhiqiang Wei,1 Jie Nie,2 Lei Huang,1 Shuang Wang,1 and Zhen Li

~~~python
1.primary thesis:
    this review highlights the advances of state of art activity recognition approaches,especially for the activity representation and classification methods.
2.Critical components of the argument that support the thesis:
    2-1:global representation:2D sulhouettes and shapes,optical flow,3D space-time volumes(STVs), discrete Fourier transform,
    2-2:local representation:BOVW,STIP(2D/3D),further exploration VQ,SA-K,LLC,FV,VLAD,SVC
    2-3:depth-based representation:representation based on depth map, skeleton-based representation(20/25joints)
    2-4:activity classification approaches:
            (1)template based approaches(template matching,dynamic time wraping,)
            (2)generative models(HMMs,CHMMs,HSMM,dynamic Bayesian network(DBN),)
            (3)discriminative models(support vector machine),
            (4)conditional random fields(CRFS) 
            (5)deep learning architectures:DNN,CNN,RNN,
    2-5:Human tracking approaches: 
            (1)filter-based tracking(kalma filter(KF),particle filter(PF))
            (2)kernel-based tracking(or mean shift tracking):          
                
                
                
~~~

#### topic4:(2019)A Survey on Vision Based Activity Recognition, its Applications and Challenges

Author: Ashwin Geet D’Sa, Dr. B G Prasad

~~~python
1.primary thesis:
    here is an paper that introduce advantage and challenge in human activity recognition of computer vision.
2.Critical components of the argument that support the thesis:
   2-1: type of activity recognition based on the device used:
        (1)sensor based activity recognition
        (2)vision based activity recognition
        (3)human activity recognition based on complexity(gesture,action,interaction,group activity)
        (4)type os vision based activity recognition based on perspective(first-person/third-person perspective
        (5)type of activity recognition based on approaches(single-layer,hierarchical approach)
   2-2:application of activity recognition:
       (1)behavior bio-metrics
       (2)content based video analysis                                                                      (3)security and suveillance 
       (4)interaction application and environment
       (5)animation and synthesis
       (6)healthcare system
       (7)rehabilitation application                                                                    2-3:challenge in vision based HAR
       (1)human behavior
       (2)intra class variability                                                                   
       (3)inter class similarity                                                                   
       (4)illumination change                                                                   
       (5)shadow effect                                                                  
       (6)partial or full occlusions                                                                 
       (7)self occlusions
       (8)scaling
       (9)bootstrapping
       (10)camera jitter                                                                   
       (11)camera automatic adjustment                                                               
       (12)noise frame in video                                                                  
       (13)camouflage                                                                   
       (14)moving background objects or human                                                                                                                    
~~~

#### topic5:(2017)A Comprehensive Review on Handcrafted and Learning-Based Action Representation Approaches for Human Activity Recognition

Author: Allah Bux Sargano 1,2,*, Plamen Angelov 1 and Zulfiqar Habib 

~~~python
1.primary thesis:
    This review paper presents a comprehensive survey of both handcrafted and learning-based action representations, offering comparison, analysis, and discussions on these approaches.and public dataset
2.Critical components of the argument that support the thesis:
    
~~~

#### topic6:(2015)Depth Silhouettes Context: A New Robust Feature for Human Tracking and Activity Recognition based on Embedded HMMs

Author: Ahmad Jalal1, Shaharyar Kamal2 and Daijin Kim1

~~~python
1.primary thesis:
    in this paper,a video-based novel approach for human activity recognition is presented using robust hybrid feature and emmbedded HMMs
2.Critical components of the argument that support the thesis:
    2-1:In the proposed HAR framework, depth maps are analyzed by temporal motion identification method to segment human silhouettes from noisy background and compute depth silhouette area for each activity to track human movements in a scene. Several representative features, including invariant, depth sequential silhouettes and spatiotemporal body joints features were fused together to explore gradient orientation change, intensity differentiation, temporal variation and local motion of specific body parts.
    2-2:benchmark depth datasets: MSRDailyActivity3D and IM-DailyDepthActivity
    2-3:"embedded HMM"is introduced which focused specifically at active areas of human body parts such as arms, legs, feet and shoulders.
    2-4:These hybrid features are symbolized by the codebook that is generated from Linde-Buzo-Gray (LBG) clustering algorithm.
~~~

#### topic7:(2018)Depth-based human activity recognition: A comparative perspective study on feature extraction

Author: Heba Hamdy Ali a,*, Hossam M. Moftah a, Aliaa A.A. Youssif b

~~~ python
1.primary thesis:
    In this study, we introduce a detailed study of current advances in the depth maps-based image representations and feature extraction process.
2.Critical components of the argument that support the thesis:
    2-1: feature extraction aproaches
        1.3D point features(interest point) 
3.method & dataset
The proposed methods are evaluated on three depth-based datasets "MSR Action 3D", "MSR Hand Gesture", and "MSR Daily Activity 3D".
While combining depth and color features on "RGBD-HuDaAct" Dataset
4.idea&key
~~~





































