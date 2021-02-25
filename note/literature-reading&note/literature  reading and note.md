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
    SOM:self-organizing Map
    GDA:generalized discriminant analysis
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
      "hierarchical approaches"hierarchical approaches recognize more complex activities by decomposing them into simple activities (sub-events)
    10."hierarchical layer method":describe high-level human activity by using simple activity called sub-event which are suitable for the  analysis of complex activity.
    11."semantic space":include human knowledge about activity such as body part(pose/poselet),object,scene,and attribute feature. we categorize semantic method into three categorise:method based on body part,method based on scene/object,method based on attributes.
    12."semantic define":Generally, semantics refers to what the sender and receiver of a
message mean and how they infer the context of the message. Semantics is the study of meaning.
In action recognition, the semantic understanding enables users to apply prior knowledge to the recognition process.
    13."deep belief network"(DBN):
    14."depth map" images may contain occlusions, which make the global features unsettled. Additionally, contrasted with color images, the depth images do not have texture but it difficult to apply local differential operators like gradients on because they are generally too noisy in both spatial and tem- poral cases.
    15."random forests(RFs)"RF is a classifier combination that uses Decision Tree (DT)-based classifiers where every DT is made by randomly selecting the data from the available data.
    16."HMM":An HMM can be explained as a stochastic finite-state machine that can be used to model time sequential information. Basically, there are four major parts in a typical HMM: namely states, initial state distribution, state transition matrix, and state observation matrix. A state represents a property or condition that an HMM may have during a particular time. Initial state distribution indicates initially state probability ofan HMM. The state transition matrix characterizes the probabilities among the states and the observation matrix contains the observation probabilities from each state. Once the architecture ofan HMM is defined with the four components, the next step is to train the HMM. To train, the first step is to classify features into a specific number of clusters, generating a codebook consisting of the cluster centroids. Then from the codebook, symbol sequences are generated through vector quantization. These symbol sequences later are used to model sequential patterns in an HMM.
    17:"forward spotting":the human activity or non-activity is segmented in the input sequence using forward spotting. A sliding window technique is used which computes the observation probability of activity or non-activity using a number of continuing observations within the sliding window,
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

#### framework

~~~python
1.primary thesis:
2.Critical components of the argument that support the thesis:  
3.method & dataset
4.idea&key
~~~

#### topic:(2015)Depth Silhouettes Context: A New Robust Feature for Human Tracking and Activity Recognition based on Embedded HMMs

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

#### topic:(2016)Fuzzy Logic Based Human Activity Recognition in Video Surveillance Applications

Slim Abdelhedi, Ali Wali and Adel M. Alimi

~~~python
1.primary thesis:
    This paper is focused on the design and implementation of a Human activity analysis system. The multiple cameras sends captured frames to the monitoring system via the local network. Through the use of human silhouette, acquired from a smart camera, a shape representation of the human beings was built in real-time and a fuzzy logic inference system was developed for fall detection
2.Critical components of the argument that support the thesis: 
    1-1:background subtraction for motion detection
        (1)the Type-2 Fuzzy Gaussian Mixture Models (T2 FGMMs) algorithm [1] was applied to extract foreground images.we used mor- phological operators and filtering methods to obtainmore accurate results
        (2)human detection and tracting.measuring the information of the human silhouette used the bounding box
        (3)Mamdanis fuzzy inference methoh
3.method & dataset
4.idea&key
~~~



#### topic:(2016)Multi‑view human activity recognition based on silhouette and uniform rotation invariant local binary patterns

Alok Kumar Singh Kushwaha1 · Subodh Srivastava1 · Rajeev Srivastava1

~~~python
1.primary thesis:
In this paper, a system framework has been presented to recognize a view invariant human activity recognition approach that uses both contour-based pose features from silhouettes and uniform rotation local binary patterns for view invariant activity representation.
2.Critical components of the argument that support the thesis: 
    2-1：the framework is composed of three consecutive medules:
    (1) detecting and locating people by background subtraction
    (2) combined scale invariant contour-based pose features from silhouettes and uniform rotation invariant local binary patterns (LBP) are extracted, and 
    (3) finally classifying activities of people by Multiclass Support vector machine (SVM) classifier.
    
3.method & dataset 
VideoWeb Multi-view dataset, i3DPost multi-view dataset , and WVU multi-view human action recogni- tion dataset .
4.idea&key # multi-view view invariant activity representation 
~~~

#### topic:(2016)Human activity recognition using segmented body part and body joint features with hidden Markov models

Md. Zia Uddin1

~~~python
1.primary thesis:
    in this paper,A novel approach is proposed here for depth video based human activity recognition, using joint-based spatiotemporal features of depth body shapes and hidden Markov models. 
2.Critical components of the argument that support the thesis:  
    The proposed approach consists of video acquisition, segmentation of body parts using a RF, feature generation, and modeling HMMs,the features are classified by generalized discriminant analysis (GDA) in order to make them more robust.
    2-1:activity video acquisition via depth camera
    2-2:the body shape extraction by depth threshold obtained empirically and background subtraction.(Gaussian mixture model)
    2-3：human body parts segmentation from depth video."random forests"
    2-4:feature generaion 3D body skeleton model  spatial feature extraction by joint pair contain polar angle and azimuthal angle
    2-5:generalized discriminant analysis on the spatiotemporal feature(to classify the features .)
    2-6：activity modeling via HMM
3.method & dataset
	MSR Daily Activity 3D dataset, MSR action 3D dataset,
4.idea&key
~~~

#### topic(2016)Robust human activity recognition from depth video using spatiotemporal multi-fused features

Ahmad Jalal a, Yeon-Ho Kim a, Yong-Joong Kim a, Shaharyar Kamal b, Daijin Kim

~~~python
1.primary thesis:
    we propose novel multi-fused features for online human activity recognition (HAR) system that recognizes human activities from continuous sequences of depth map via  the depth sensor.The proposed online HAR system segments human depth silhouettes using temporal human motion information as well as it obtains human skeleton joints using spatiotemporal human body information.it extracts multi-fused features that consist of four skeleton joint features.and one body shape feature. 
2.Critical components of the argument that support the thesis:
    2-1:"feature extration based on multi-fused features",we urilized person specific body part model 15 3D body joints.then extract four skeleton joint features that include torso-bassed distance feature,key-joint based distance feature,spatiotemporal magnitude feature,and spatiotemporal directional angle feature.
     2-2:"Body shape feature"   we propose the other spatiotemporal body shape feature that is based on the depth differential silhouettes (DDS) between two consecutive frames.The depth differential silhouettes (DDS) can be considered as an effective feature that uses the full-body shape information along with motion information from depth silhouettes.
    2-3:"Determining of codebook size"the human activity image is represented by the multi-fused features that combines four skeleton joint features and one body shape feature.The codebook contains the prototype code vectors that are generated from the training fea- ture vectors using vector quantization (VQ) [29]. While, the co- debook size is determined as 128 experimentally using k-mean clustering algorithm
    2-4:"The continuous human activity recognition":The proposed simultaneous activity segmentation and recognition consists of two concurrent modules: the activity segmentation module (i.e., forward spotting) and activity re-cognition module (i.e., accumulative HMMs).
     First, the activity segmentation module computes the competitive differential ob- servation probability ϕ( )t and detects the start point of an activity. Then, it activates the activity recognition module, which performs the recognition task until it receives the activity end signa Existing activity segmentation and HMM models [43,44] need to detect the end point of each sequence. trace back to the start point and send the extracted data to HMMs,It inevitably causes a major time delay, repetition of data, segmentation ambiguities,       we proposed "forward spotting and accumulative HMMs" that segmented some meaningful activities in the forward manner, which enabled continuous modeling and testing over on-going video sequences without any time delay.
    2-5:"Activity recognition using accumulative HMMs"apply the segment to all activity HMMs. Let an observed activity segment be ={ … }
O oo o,, ,tt te , where ts and te denote the s s+1 见图
start and end points of activity, respectively. Then,
3.method & dataset
IM-Daily- DepthActivity, MSRAction3D and MSRDailyActivity3D
Furthermore, we proposed to use the forward spotting scheme that differentiates the observation probability between activity and non-activity, in or- der to segment and recognize random activities during online con- tinuous activity recognition without any time delay，we will improve the effectiveness of our multi- fused features by adding the color information. Besides, we also used the features for more complicated activities including human–object interactions or multi-person interactions.
Acknowledgments
4.idea&key
in this paper,the HAR system utilize multi-fused feature  include skeletion joint,silhouette shape feature, through segmen and detect motion by forward spotting from start to end,put in accumulative HMM to recognition .
~~~

#### topic:(2016)A Depth Camera-based Human Activity Recognition via Deep Learning Recurrent Neural Network for Health and Social Care Services

S. U. Parka, J. H. Parka, M. A. Al-masnia, M. A. Al-antaria, Md. Z. Uddinb, T. -S. Kima*

~~~ python
1.primary thesis:
    In this paper, we propose a new HAR system via Recurrent Neural Network (RNN) which is one of deep learning algorithms.We utilize joint angles from multiple body joints changing in time which are represented a spatiotemporal feature matrix (i.e., multiple body joint angles in time). With these derived features,
2.Critical components of the argument that support the thesis:  
	In this section, we introduce our RNN-based HAR system. Our HAR system proceeds to the following steps.First, we create an input feature matrix of joint angles computed from the MSRC-12 activity dataset13. Second, we train RNN with the training feature matrix. Third, we evaluate the trained RNN with test data sets by recognizing twelve human activities. The recognition performance is compared to the results from the conventional HMM- and DBN-based HAR systems.
    2-1:
3.method & dataset
We have evaluated the HAR systems using the MSRC-12 dataset.
4.idea&key
~~~



#### topic:(2017)A Review on Human Activity Recognition Using Vision-Based Method

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

#### topic(2017)A Comprehensive Review on Handcrafted and Learning-Based Action Representation Approaches for Human Activity Recognition

Allah Bux Sargano 1,2,*, Plamen Angelov 1 and Zulfiqar Habib 2 1

~~~ python
1.primary thesis:
    Recently, with the emergence and successful deployment of deep learning techniques for image classification, researchers have migrated from traditional handcrafting to deep learning techniques for HAR.This review paper presents a comprehensive survey of both handcrafted and learning-based action representations, offering comparison, analysis, and discussions on these approaches.
2.Critical components of the argument that support the thesis:  
    2-1：The handcrafted representation-based approach mainly follows the bottom-up strategy for HAR.Generally, it consists of three major phases (foreground detection, handcrafted feature extraction and representation, and classification.Different taxonomies have been used in the survey papers to discuss the HAR approaches. A survey presented in [1], divides the activity recognition approaches into two major categories: single layered approaches and hierarchical approaches.Single-layered approaches recognize the simple activities from the sequence of a video, while hierarchical approaches recognize more complex activities by decomposing them into simple activities (sub-events).                                                                                                                                        2-2:Handcrafted Representation-Based Approach
          ()Space-Time-Based Approaches                                                                                                               (1)Space-Time Volumes (STVs) 
          	(2)Space-Time Trajectory Trajectory-based                                                                                                 (3)Space-Time Features
          ()Appearance-Based Approaches                                                                                                               (1)Shape-Based Approaches
            (2)Motion-Based Approaches                                                                                                               (3)Hybrid Approaches                                                                                                                   ()other approaches
             (1)Local Binary Pattern (LBP)-Based Approaches                                                                                            (2)Fuzzy Logic-Based Approaches Traditional
                                                                                                                                                  2-3:Learning-Based Action Representation Approach 
         	(1)Non-Deep Learning-Based Approaches
              (1-1) Dictionary Learning-Based Approaches                                                                                               (1-2) Genetic Programming  
            (2)Deep Learning-Based Approaches Recent
               (2-1)Generative/Unsupervised Models                                                                                                      (2-1)Discriminative/Supervised Models                              
3.method & dataset                                                                                                                                       
4.idea&key this paper introduction variant handcrafted/learning approaches.after that,it is dataset and application.it is a review that important and comprehensive
~~~



#### topic:(2018)Depth-based human activity recognition: A comparative perspective study on feature extraction

Author: Heba Hamdy Ali a,*, Hossam M. Moftah a, Aliaa A.A. Youssif b

~~~ python
1.primary thesis:
    In this study, we introduce a detailed study of current advances in the depth maps-based image representations and feature extraction process.moreover,wo discuss the state of art datasets and subsequent classification procedure.
2.Critical components of the argument that support the thesis:
    2-1: feature extraction aproaches
        1.3D point features(interest point) 
        2.Spatialetemporal cuboid(立方体) descriptors
        3.Random Occupancy Pattern (ROP) features
        4.Depth silhouette
        5.Surface normals features
        6.Depth and color features
3.method & dataset
The proposed methods are evaluated on three depth-based datasets "MSR Action 3D", "MSR Hand Gesture", and "MSR Daily Activity 3D".
While combining depth and color features on "RGBD-HuDaAct" Dataset

4.idea&key
# compare different feafures extraction techinques. utilize advantage to processing a easier and more accuracy techique
~~~

#### topic:(2019)A Survey on Vision Based Activity Recognition, its Applications and Challenges

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

#### topic :(2020)vision -based human activity recognition: a survey   

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

#### topic :(2020)A survey on video‑based Human Action Recognition: recent updates, datasets, challenges, and applications

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

#### 





























