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
    18."unimodel and multimodel method for human activities":Unimodal methods represent human activities from data of a
single modality, such as images, and they are further categorized as: (i) space-time, (ii) stochastic, (iii) rule-based, and (iv) shape- based methods."Space-time methods" involve activity recognition methods,which represent human activities as a set of spatiotemporal features  or trajectories  Stochastic methods recognize activities by applying statistical models to represent human actions (e.g., hidden Markov models) . Rule-based methods use a set of rules to describe human activities . Shape-based methods efficiently represent activities with high-level reasoning bymodeling themotion ofhuman bodyparts.
    "Multimodal methods" combine features collected from different sources and are classified into three categories: (i) affective, (ii) behavioral, and (iii) social networking methods.
       "Affective methods" represent human activities according to emotional communications and the affective state of a person.
       "Behavioral methods" aim to recognize behavioral attributes, non-verbal multimodal cues, such as gestures, facial expressions, and auditory cues.
       "social networking methods" model the characteristics and the behavior of humans in several layers ofhuman-to-human interactions in social events fromgestures, bodymotion, and speech.
   19. "Supervised machine learning was used for activity recognition" 
    "Feed-forward BPNN": Also known as multilayer perceptron, feed-forward BPNN is a useful tool for classification problems. These have three types of layers including the input layer which receives the input data, the output layer at which the output is obtained and the hidden layer/s which lie between the other two types of layers. In this paper, the neural network was implemented using one hidden layer consisting of 14 neurones with sigmoid activation function. The output layer had four neurones with softmax function. About 50% of the data was used for training and 35% for testing. About 15% of the data was used for validation purpose.
    "KNNs classifier": It works on the principle of learning the class of new data samples by finding similar samples from the training data. Class of new data is found by majority voting of its KNNs. A distance function is used to find similarity between the neighbours. In the current research, KNN classifier was implemented using Mahalanobis distance as the distance metrics to find neighbours. The value of k was found by experimentally adjusting until the classifier achieved the lowest error. The empirically calculated value of k was 4
   "SVM classifier": Out of many possible hyperplanes, SVM classifier finds the most optimal hyperplane which maximises the separation between classes. In this paper, MATLAB ECOC classifier was used which is the multiclass model for SVMs. Multiclass learning in this model is achieved by reducing multiclass problem to binary classification using one versus one coding design. A linear kernel function was used in the current research 
   "Discriminant analysis classifier": The type of discriminant used in this research was linear. Linear discriminant classifier searches for linear transformations to achieve best data separation by taking into account interclass and intraclass scatterers. Mean and covariance parameters for each class were found using fitcdiscr function which first calculates the sample mean for each class and then calculates sample covariance by subtracting sample mean from the class observations for each class.
  "Naive Bayes classifier": It uses probability theory and Bayes theorem for predicting the class of unknown data. This classifier was implemented such that Gaussian distribution was used for estimating the model parameters, i.e. mean and standard deviation for each class  
~~~

#### idea
~~~idea

~~~

#### framework

~~~python
1.primary thesis:
  
2.Critical components of the argument that support the thesis: 
  2-1：
  2-2：
  2-3：
  2-4：
  2-5：
3.method & dataset
4.idea&key
~~~

### topic(2015) 

#### topic:(2015)A Review of Human Activity Recognition Methods

Michalis Vrigkas1 , Christophoros Nikou1* and Ioannis A. Kakadiaris2

~~~ python
1.primary thesis:
      In this work, we provide a detailed review of recent and state-of-the-art research advances in the field of human activity classification. We propose a categorization of human activity methodologies and discuss their advantages and limitations.
2.Critical components of the argument that support the thesis:  
    2-1:what is action? where in the video?
    2-2:human activity recognition methods into two main categories:"unimodal" and "multimodal" activity recognition methods. 
    unimodal methods: (i) space-time, (ii) stochastic (iii) rule-based, and (iv) shape-based methods.
    multimodel methods:(i)affective mothods (ii)behavioral methods (iii)social networking methods and (multimodal feature fusion) 
    2-3:and dataset table.
3.method & dataset  
4.idea&key
~~~

#### topic (2015)Semantic human activity recognition: A literature review
Maryam Ziaeefard n, Robert Bergevin

~~~ python
1.primary thesis:
  This paper presents an overview of state-of-the-art methods in activity recognition using semantic features. Unlike low-level features, semantic features describe inherent characteristics of activities
2.Critical components of the argument that support the thesis: 
  2-1:what is semantics?
  2-2:semantic space.we introduceasemantic space as a feature space including only features using human understanding to distinguish activities
  2-3:
3.method & dataset
UT-Interaction [90], Willow datasets [91],and Pascal VOC2010Action
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

#### topic(2015):Skeleton-based Human Activity Recognition for Video Surveillance

Ahmed Taha 1, Hala H. Zayed 1, M. E. Khalifa 2 and El-Sayed M. El-Horbaty 3

~~~python
1.primary thesis:
  In this paper, a system for human activity recognition is proposed. We have considered the task of obtaining a descriptive labeling of the activities being performed through labeling human "sub-activities". The activities we consider happen over a long period, and comprise several sub-activities performed in a sequence. The proposed activity descriptor makes the activity recognition problem viewed as a sequence classification problem. The proposed system employs Hidden Markov Models (HMMs) to recognize human activities.
2.Critical components of the argument that support the thesis: 
  2-1:RGB-D sensor,Hidden Markov Models(HMMs),
3.method & dataset
Cornell CAD-60 and Cornell CAD-120
4.idea&key
~~~

#### topic (2015)Hybrid classifier based human activity recognition using the silhouette and cells

D.K. Vishwakarma ⇑, Rajiv Kapoor

~~~python
1.primary thesis:
  	The aim of this paper is to present a new approach for human activity recognition in a video sequence by exploiting the key poses of the human silhouettes, and constructing a new classification model.
2.Critical components of the argument that support the thesis: 
  2-1:extraction of silhouette using texture information.Gaussian Mixture Model (GMM) and Local Binary Pattern (LBP) based background models are widely used
  2-2:feature extraction  the feature detectors, feature descriptors, bag-of-features repre-sentations, and local features based on voting for localization.
  2-3：extracting key poses of the frames.
  2-4:feature computation and representation
  2-5:classification model. Linear Discriminant Analysis (LDA), K-Nearest Neighbor (K-NN) and Support Vector Machine (SVM) classifier.
3.method & dataset
	Weizmann, KTH, and BalletMovement.
4.idea&key
~~~

#### topic(2015)Synoptic Video Based Human Crowd Behavior Analysis for Forensic Video Surveillance

B.Yogameena, K.Sindhu Priya

~~~python
1.primary thesis:
  In this paper, Video synopsis is used to represent a short video while preserving the essential activities for a long video.
2.Critical components of the argument that support the thesis: 
  2-1：foreground extraction  (background model GMM)
  2-2：compact video synopsis -global spatiotemporal optimization.-iteractive object shifting. -modeling compact background synthesis
  2-3：classification of crowd behavior
3.method & dataset
4.idea&key
~~~

#### topic(2015)Human Daily Activity Recognition with Joints plus Body Features Representation Using Kinect Sensor
Ahmad Jalal, Yeonho Kim,Shaharyar Kamal, Adnan Farooq,Daijin Kim

~~~python
1.primary thesis:
  In this paper, we proposed a new feature representation and extraction method using a sequence of depth silhouettes.
2.Critical components of the argument that support the thesis: 
  2-1：depth silhouette preprocessing.ROI
  2-2：feature extraction .rely on the skeleton representation and body shape silhouettes of the human body.
    (1)skin body parts detection feature.(we used body skin color detection method  to model the skeleton joints.)
    (2)Multi-view body shape feature:Due to self-occlusion or missing joints information
  2-3：Training and Recognition(The Self-organizing Map (SOM) is unsupervised learning neural networks)
  2-4：
  2-5：
3.method & dataset,
Online depth dataset: IM-DailyDepthActivity,MSRAction3D,
4.idea&key
~~~

### topic(2016): 

#### topic:(2016)A Survey on Human Activity Recognition from Videos

T.Subetha ,Dr.S.Chitrakala

~~~ python
1.primary thesis:
This paper collectively summarizes and deciphers the various methodologies, challenges etc...This paper collectivelysummarizes and deciphers the various methodologies, challenges and issues of Human Activity Recognition systems. Variants of Human Activity Recognition
various methodologies, challenges and issues of Human Activity Recognition systems. Variants of Human Activity Recognition systems such as Human Object Interactions and Human-Human Recognition systems. Variants of Human Activity Recognition systems such as Human Object Interactions and Human-Human Interactions are also explored. Various benchmarking datasets systems such as Human Object Interactions and Human-Human Interactions are also explored. Various benchmarking datasets and their properties are being explored. The Experimental
Interactions are also explored. Various benchmarking datasets and their properties are being explored. The Experimental Evaluation of various papers are analyzed
2.Critical components of the argument that support the thesis:  
3.method & dataset
4.idea&key
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
    2-1:"MSRC-12 Gesture Dataset and Features"，This dataset consists of sequences of human activities containing 12 activities，from 14 key body parts we extracted 28 joint angle features，The joint angles were calculated in a spherical coordinate so that they are invariant to position and scale. 
    2-2："HMM-based HAR":On the feature matrix, we perform Principal Component Analysis (PCA) to reduce a dimension of the feature
vector from 28 to 17, which includes more than 99% of information of the frame. Then each of the reduced feature vectors of (1×17) is clustered to be one of 64 codes via Linde-Buzo-Gray algorithm14.
    2-3："DBN-based HAR"
    2-4："RNN-based HAR"
3.method & dataset
We have evaluated the HAR systems using the MSRC-12 dataset.we have compared the accurarcy of  HAR based on HMM,DBN and RNN.
4.idea&key it is compared the accuracy of HAR based on  HMM,DBN,RNN
~~~

### topic(2017)

#### topic:(2017)Hidden Markov Model Based Human Activity Recognition using Shape and Optical Flow Based Features

Maheshkumar H. Kolekar, Deba Prasad Dash

~~~ python
1.primary thesis:
 In this paper shape and optical flow features are fused together and used for human activity recognition. Features extracted are found to be efficient as concluded by ANOVA test. Hidden Markov Model are generated for each activity.System is trained and tested in various indoor and outdoor environment. The method adapted is made shape and angle invariant. Accuracy achieved using least square support vector machine classifier is 80% for all activities. Hidden Markov Model resulted in better accuracy as compared to least square support vector machine classifier with accuracy of 100.00% for walking, 100.00% for hand waving, 90% for bending, 84.61% for running and 90% for side gallop activities. 100% accuracy is achieved in recognizing activity in different angle with respect to camera.
2.Critical components of the argument that support the thesis:  
    
3.method & dataset
4.idea&key
~~~



#### topic:(2017)Recent Advances in Video-Based Human Action Recognition using Deep Learning: A Review

Di Wu, Nabin Sharma, and Michael Blumenstein

~~~python
1.primary thesis:
 This paper presents a review of various state-of-the- art deep learning-based techniques proposed for human action recognition on the three types of datasets. 
2.Critical components of the argument that support the thesis:  
    2-1:"single viewpoint dataset":The single viewpoint datasets normally use a single camera recording human actions from a certain invariant angle without camera movement.such as Weizmann [1] KTH [36] UCF sports [37] Hollywood [2
    2-2:"Multiple Viewpoint Datasets":In a real-world scenario, multiple cameras are used for monitoring large public spaces.The advantages of these datasets is that they model a 3D human body shape from different angles and occlusion problems are avoided in contrast with single viewpoint streams.such as IXMAS [38] i3DPost [39] MuHAVi [40] Videoweb [41]CASIA Action [42]
    2-3:"Depth and RGB Datasets":Depth and RGB video datasets are normally generated by specific devices, such as a depth camera or an RGB camera.The depth and RGB videos not only contain video frames, but also have special data called depth maps, which are used to measure the depth of the objects from the observation point.such as MSR-Action3D [43] DailyActivity3D [44] Multiview 3D [45] CAD-60 [46]
3.method & dataset
4.idea&key
~~~

#### topic:(2017)Trajectory-Based Human Activity Recognition from Videos

Boubakeur Boufama, Pejman Habashi, Imran Shafiq Ahmad

~~~python
1.primary thesis:
    This paper proposes a new method using trajectories, as mid-level features, for human activity recognition,We have used a simple shape descriptor and the standard bag of word algorithm for human activity classification
2.Critical components of the argument that support the thesis:  
    2-1:Interest Point Tracking
    2-2:Lucas Kanade Trajectories
    2-3:Farnback Trajectories
    2-4: bag of wirds algorithm.
3.method & dataset
	a stereo vision created a stereo dateset .
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

#### topic(2017) Suspicious human activity recognition: a review @

Rajesh Kumar Tripathi1· Anand Singh Jalal1 · Subhash Chand Agrawal1 

~~~python
1.primary thesis:
In this paper, we present the state-of-the-art which demonstrates the overall progress of suspicious activity recognition from the surveillance videos in the last decade.
2.Critical components of the argument that support the thesis: 
    2-1："Foreground object detection Background subtraction"
    2-2："Object detection" in the video frames is done through either the nontracking based approaches or tracking based approaches，Tracking based approach is employed to make the trajectory of an object over time by locating its position in every frame of the video
    2-3："Feature extraction"，Shape and motion based features of the object are extracted through various algorithms for object identification and sometimes, its feature vector is supplied as input to the classifier,There are different techniques to classify the objects such as Support Vector Machine, Haar-classifier, Bayesian, K-Nearest Neighbor, Skin color detection, and Face recognition.
    2-4："Object classification",After recognizing the objects from the video through classification, activity analysis is performed to compare with the different threshold value to assure abnormal activity. 
3.method & dataset
4.idea&key
~~~

### topic(2018)

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

### topic(2019)

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

### topic(2020)

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

### topic(2021)





























