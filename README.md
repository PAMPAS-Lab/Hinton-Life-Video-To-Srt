# Hinton-Life-Video-To-Srt

## Geoffrey Everest Hinton介绍
Geoffrey Everest Hinton（1947年12月6日—），又译杰弗里·欣顿，是英国出生的加拿大计算机学家和心理学家，现任多伦多大学教授。他在类神经网络和深度学习领域做出了杰出贡献，被誉为“深度学习教父”。2018年，他与约书亚·本希奥、杨立昆共同获得图灵奖。2024年，他与约翰·霍普菲尔德共同获得诺贝尔物理学奖。

## 生平
- **教育背景**
  - 1970年：剑桥大学实验心理学学士学位
  - 1978年：爱丁堡大学人工智能博士学位

- **职业经历**
  - 曾在萨塞克斯大学、加州大学圣迭戈分校、剑桥大学、卡内基梅隆大学和伦敦大学学院工作
  - 1998年：当选皇家学会会士
  - 2005年：获得IJCAI杰出学者奖终生成就奖
  - 2011年：获得赫茨伯格加拿大科学和工程金奖
  - 2013年3月：加入Google，同时Google并购了他创办的DNNresearch公司
  - 目前：多伦多大学计算机科学系教授，Vector Institute首席科学顾问

## 研究兴趣
- **主要贡献**
  - **反向传播算法（Backpropagation Algorithm）**：一种用于训练人工神经网络的常用方法，通过误差梯度逐层调整网络权重。
  - **对比散度算法（Contrastive Divergence Algorithm）**：一种用于快速训练受限玻尔兹曼机（Restricted Boltzmann Machine, RBM）的有效算法。
  - **波尔兹曼机（Boltzmann Machines）**：一类基于统计力学的能量模型，能够学习数据的概率分布。其中包括受限玻尔兹曼机（RBM），其结构中不存在单元之间的内部连接。
  - **分散表示（Distributed Representation）**：指每个概念由多个维度的数值来表示，并且这些数值分布在多个节点上，而不是单一节点负责一个概念。
  - **时延神经网络（Time-Delay Neural Networks, TDNNs）**：一种特殊类型的卷积神经网络（CNN），常用于处理时间序列数据或语音信号处理。
  - **专家混合系统（Mixtures of Experts, MoE）**：一种模块化的神经网络架构，其中不同的“专家”子网络处理输入的不同方面，最后由门控网络决定各专家输出的权重。
  - **亥姆霍兹机（Helmholtz Machines）**：一种早期的生成模型，旨在模拟人类大脑如何处理感知信息，包含一个识别网络和一个生成网络。
  - **胶囊神经网络（Capsule Networks, CapsNets）**：一种改进传统卷积神经网络的方法，它使用胶囊（capsules）代替单个神经元，每个胶囊代表一组神经元，专门捕捉特定实体的各种属性如位置、姿态等。

>主要贡献的内容引用自维基百科 
- **代表性研究论文**
  **反向传播算法的使用**
     - Rumelhart D E, Hinton G E, Williams R J. Learning representations by back-propagating errors[J]. Cognitive modeling, 1988, 5(3): 1.
  **CNN语音识别开篇TDN网络**
     - Waibel A, Hanazawa T, Hinton G, et al. Phoneme recognition using time-delay neural networks[J]. Backpropagation: Theory, Architectures and Applications, 1995: 35-61.
  **DBN网络的学习**
     - Hinton G E, Osindero S, Teh Y W. A fast learning algorithm for deep belief nets[J]. Neural computation, 2006, 18(7): 1527-1554.
  **深度学习的开篇**
     - Hinton G E, Salakhutdinov R R. Reducing the dimensionality of data with neural networks[J]. Science, 2006, 313(5786): 504-507.
  **数据降维可视化方法t-SNE**
     - Maaten L, Hinton G. Visualizing data using t-SNE[J]. Journal of Machine Learning Research, 2008, 9(Nov): 2579-2605.
  **DBM模型**
     - Salakhutdinov R, Hinton G. Deep Boltzmann Machines[C]//Artificial Intelligence and Statistics. 2009: 448-455.
  **ReLU激活函数的使用**
     - Nair V, Hinton G E. Rectified Linear Units Improve Restricted Boltzmann Machines[C]//Proceedings of the 27th International Conference on Machine Learning (ICML-10). 2010: 807-814.
  **RBM模型的训练**
     - Hinton G E. A Practical Guide to Training Restricted Boltzmann Machines[M]//Neural Networks: Tricks of the Trade. Springer, Berlin, Heidelberg, 2012: 599-619.
  **深度学习语音识别开篇**
     - Hinton G, Deng L, Yu D, et al. Deep Neural Networks for Acoustic Modeling in Speech Recognition[J]. IEEE Signal Processing Magazine, 2012, 29.
  **深度学习图像识别开篇AlexNet**
     - Krizhevsky A, Sutskever I, Hinton G E. Imagenet Classification with Deep Convolutional Neural Networks[C]//Advances in Neural Information Processing Systems. 2012: 1097-1105.
  **权重初始化和Momentum优化方法的研究**
     - Sutskever I, Martens J, Dahl G, et al. On the Importance of Initialization and Momentum in Deep Learning[C]//International Conference on Machine Learning. 2013: 1139-1147.
  **Dropout方法提出**
     - Srivastava N, Hinton G, Krizhevsky A, et al. Dropout: A Simple Way to Prevent Neural Networks from Overfitting[J]. The Journal of Machine Learning Research, 2014, 15(1): 1929-1958.
  **三巨头深度学习综述**
     - LeCun Y, Bengio Y, Hinton G. Deep Learning[J]. Nature, 2015, 521(7553): 436.
  **蒸馏学习算法**
     - Hinton G, Vinyals O, Dean J. Distilling the Knowledge in a Neural Network[J]. arXiv preprint arXiv:1503.02531, 2015.
  **Capsule Network**
     - Sabour S, Frosst N, Hinton G E. Dynamic Routing Between Capsules[C]//Advances in Neural Information Processing Systems. 2017: 3856-3866.
                                                                                                                                           > 引用自知乎文章(【AI大咖】认真认识一代AI教父Hinton)
## 轶事
- **家族背景**
  - 他是逻辑学家乔治·布尔与数学家和教育家玛丽·埃佛勒斯·布尔的曾曾孙，布尔的工作最终成为了现代电子计算机的基础。
  - 他是外科医生和作家詹姆士·辛顿的后裔。
- **个人生活**
  - 有两任妻子，两个孩子。
- **观点**
  - 2023年5月，他称其后悔研发人工智能，担心人工智能会为世界带来严重危害。

## 个人主页
- [Geoffrey Hinton的个人主页](http://www.cs.toronto.edu/~hinton/bio.html)

## 获奖
- 1998年：当选皇家学会会士
- 2005年：IJCAI杰出学者奖终生成就奖
- 2011年：赫茨伯格加拿大科学和工程金奖
- 2018年：图灵奖
- 2024年：诺贝尔物理学奖
  
---

## 2007

### **12月**
- **2007/20071204 The Next Generation of Neural Networks**  
  - **日期**: 12月4日
  - **视频类型**：讲座
  - **采访机构**：Google Tech Talks
  - **机构介绍**：Google Tech Talks是 Google 组织的一个技术讲座系列，旨在促进前沿科技知识的分享与交流。  
  - **核心内容**: 探讨神经网络的下一代发展，可能涉及深度学习的早期架构创新。  
  - [链接](./2007/20071204The%20Next%20Generation%20of%20Neural%20Networks.md)

---

## 2010

### **3月**
- **2010/20100319 Recent Developments in Deep Learning**  
  - **日期**: 3月19日
  - **视频类型**：讲座
  - **采访机构**：Google Tech Talks
  - **机构介绍**：Google Tech Talks是 Google 组织的一个技术讲座系列，旨在促进前沿科技知识的分享与交流。  
  - **核心内容**: 总结当时深度学习领域的最新进展与挑战。  
  - [链接](./2010/20100319Recent%20Developments%20in%20Deep%20Learning.md)

---

## 2012

### **8月**
- **2012/20120824 Dropout and the Evolution of Neural Networks**  
  - **日期**: 8月24日
  - **视频类型**：讲座
  - **采访机构**：Google Tech Talks
  - **机构介绍**：Google Tech Talks是 Google 组织的一个技术讲座系列，旨在促进前沿科技知识的分享与交流。
  - **核心内容**: 可能涉及神经科学与人工智能的交叉研究，探讨大脑启发的AI模型。  
  - [链接](./2012/20120824Brains.md)

---

## 2013

### **5月**
- **2013/20130530 Recent Developments in Deep Learning**  
  - **日期**: 5月30日
  - **视频类型**：大学讲座
  - **采访机构**：University of British Columbia，即不列颠哥伦比亚大学
  - **机构介绍**：该校是加拿大U15研究型大学联盟、环太平洋大学联盟、全球大学高研院联盟、Universitas 21和英联邦大学协会的成员之一。  
  - **核心内容**: 再次聚焦深度学习进展，可能讨论卷积网络或反向传播的优化。  
  - [链接](./2013/20130530Geoff%20Hinton%20-%20Recent%20Developments%20in%20Deep%20Learning.md)

---

## 2014

- **2014/2014 What's wrong with convolutional nets**  
  - **录制日期**:2014 
  - **视频**：大学讲座
  - **采访机构**：University of Toronto，即多伦多大学
  - **机构介绍**：是加拿大最古老、最大的大学之一，位于安大略省的多伦多市。它成立于1827年，最初名为“国王学院”，直到1849年才改为现名并成为一所非宗教性质的学府。 
  - **核心内容**: 分析卷积神经网络的局限性及改进方向。  
  - [链接](./2014/20140000_Whats_wrong_with_convolutional_nets.md)

---

## 2016

- **2016/2016 CIFAR Annual Dinner Keynote Address**  
  - **录制日期**: 2016年
  - **视频类型**：技术问答
  - **采访人**：Nora Young
  - **采访机构**：Canadian Institute for Advanced Research（加拿大高等研究所），即CIFAR
  - **机构介绍**：CIFAR是一个知名的国际组织，它支持和资助全球范围内的高级研究项目，并聚集了来自世界各地的顶尖学者来探讨和解决一些最复杂的科学和社会问题。  
  - **核心内容**: 探讨AI如何重新定义人类对心智与认知的理解。  
  - [链接](./2016/20160000_Geoffrey_Hinton-Artificial_Intelligence_Redefining_Mind_Understanding.md)

### **3月**
- **2016/20160304 The Rise of Deep Learning**  
  - **日期**: 3月4日
  - **视频类型**：新闻采访
  - **采访机构**：TVOntario，即简称TVO
  - **机构介绍**：TVO是安大略省的公共教育媒体机构，自1970年成立以来，TVO一直致力于通过各种平台提供终身学习的机会，包括电视、网站、社交媒体以及移动应用程序等。 
  - **核心内容**: 探讨Hinton在深度学习领域的开创性贡献。  
  - [链接](./2016/20160304Geoffrey%20Hinton%20The%20Godfather%20of%20Deep%20Learning.md)

### **4月**
- **2016/20160417 Can sensory cortex do backpropagation?**  
  - **日期**: 4月17日
  - **视频类型**：讲座  
  - **核心内容**: 探讨大脑感觉皮层是否可能实现反向传播算法（Backpropagation），并提出新的神经计算模型。  
  - [链接](./2016/20160417_Sensory_Cortex_Backpropagation-Geoffrey_Hinton.md)

---
## 2017

### **8月**
- **2017/20170809 The Evolution of Deep Learning**  
  - **日期**: 8月9日
  - **视频类型**：人物采访
  - **采访人**：Andrew Ng，即吴恩达  
  - **核心内容**: 回顾Hinton在AI和深度学习领域的个人历程，探讨其关键技术贡献（如反向传播、受限玻尔兹曼机、胶囊网络），并展望未来发展方向。  
  - [链接](./2017/20170809Heroes_of_Deep_Learning_Andrew_Ng_interviews_Geoffrey_Hinton.md)

### **9月**
- **2017/20170912 The Brain Doesn't Do Backprop**  
  - **日期**: 9月12日
  - **视频类型**：人物访谈 
  - **核心内容**: 从神经科学视角探讨深度学习的发展历程、局限性及未来方向。  
  - [链接](./2017/20170912Meet_Geoffrey_Hinton.md)

### **11月**
- **2017/20171103 The Future of Neural Networks**  
  - **日期**: 11月3日
  - **视频类型**：技术研讨会
  - **采访人**：Cade Metz
  - **采访机构**：The New York Times，即纽约时报
  - **机构介绍**：《纽约时报》（The New York Times）是美国乃至全球最具影响力的日报之一，以其深度报道、高质量的新闻评论和对重要事件的详尽分析而闻名。 
  - **核心内容**: 从神经科学视角探讨深度学习的发展历程、局限性及未来方向。  
  - [链接](./2017/20171103The_Times_Interviews_Geoffrey_Hinton.md)
  
---

## 2018

### **6月**
- **2018/20180626 This Canadian Genius Created Modern AI**  
  - **日期**: 6月26日
  - **视频类型**：人物访谈
  - **采访人**：Ashlee Vance
  - **采访机构**：Bloomberg，即彭博社
  - **机构介绍**：彭博社是一个全球领先的金融数据、新闻和媒体公司，提供广泛的财经资讯服务、数据分析工具以及新闻报道。  
  - **核心内容**: 追溯Hinton坚持神经网络研究40年的历程，揭示深度学习革命的转折点。  
  - [链接](./2018/20180626This%20Canadian%20Genius%20Created%20Modern%20AI.md)

---

## 2019

### **1月**
- **2019/20190113 creative destruction lab**  
  - **日期**: 1月13日
  - **视频类型**：技术讲座  
  - **核心内容**: 揭示生物智能的多时间尺度适应机制及其对AI发展的启示。  
  - [链接](./2019/20190906_AI_Revolution-Toronto_Global_Forum_Keynote.md)

### **2月**
- **2019/20190226 geoffrey hinton - capsule networks**  
  - **日期**: 2月26日
  - **视频类型**：技术讲座
  - **采访机构**：University of York，即约克大学
  - **机构介绍**：约克大学是一所位于英国英格兰约克郡的公立研究型大学。它成立于1963年，是英国罗素大学集团的一员，这个集团包含了英国一些最顶尖的研究型大学。 
  - **核心内容**: 分析传统卷积神经网络（ConvNets）的局限性，提出胶囊网络（Capsule Networks）作为改进方案，解决视角变化和几何关系的建模问题。  
  - [链接](./2019/20190226geoffrey%20hinton%20-%20capsule%20networks.md)

### **5月**
- **2019/20190510 Fireside Chat with Turing Award Winner Geoffrey Hinton**  
  - **日期**: 5月10日
  - **视频类型**：人物访谈
  - **采访机构**：Google I/O 2019
  - **机构介绍**：Google I/O 2019是谷歌举办的年度开发者大会。  
  - **核心内容**: 本次对谈覆盖Hinton从1980年代开始的神经网络研究，包括早期挫折、2000年代关键突破（如反向传播算法优化），以及他对意识、教育变革和AI伦理的前瞻思考。Hinton以生物学启发的视角，解释为何坚信神经网络是智能的唯一路径。  
  - [链接](./2019/20190510A%20Fireside%20Chat%20with%20Turing%20Award%20Winner%20Geoffrey%20Hinton.md)

### **6月**
- **2019/20190624 Insights into Neural Networks and Machine Learning**  
  - **日期**: 6月24日
  - **视频类型**：技术讲座
  - **采访机构**：2018 ACM（Association for Computing Machinery，美国计算机协会）
  - **机构介绍**：ACM是一个国际性的科技教育及科学 computing 学会。ACM 成立于1947年，是世界上最大的教育和科研计算机领域组织，拥有来自学术界、工业界和政府的超过10万名会员。  
  - **核心内容**: 探讨了监督学习、无监督学习、强化学习、记忆网络在解决视觉和推理问题中的应用，以及这些技术对社会的影响。  
  - [链接](./2019/20190624_Geoffrey_Hinton_and_Yann_LeCun.md)

### **9月**
- **2019/20190906 The Evolution of AI and Deep Learning**  
  - **日期**: 9月6日
  - **视频类型**：技术论坛
  - **论坛成员**：Yoshua Bengio，Heather Reisman（主持人）
  - **采访机构**：International Economic Forum of the Americas，即IEFA
  - **机构介绍**：IEFA 是一个非营利组织，成立于1995年，总部位于加拿大蒙特利尔，旨在通过国际峰会、论坛和多媒体内容推动全球经济对话与合作。  
  - **核心内容**: 探讨AI从符号主义到神经网络的范式转变，深度学习的核心概念及其应用前景，Hinton分享其技术信念与社会影响思考。  
  - [链接](./2019/20190906_AI_Revolution-Toronto_Global_Forum_Keynote.md)

---

## 2020

### **2月**
- **2020/20200210 胶囊网络与自我监督学习的未来**  
  - **日期**: 2月10日
  - **视频类型**：技术讲座
  - **采访机构**：Association for the Advancement of Artificial Intelligence，美国人工智能促进协会，即AAAI
  - **机构介绍**：AAAI是人工智能（AI）领域最具影响力的国际学术组织之一，成立于1979年，致力于推动AI研究、教育及伦理实践。其年度旗舰会议 AAAI Conference on Artificial Intelligence 被公认为AI领域的顶级会议之一。  
  - **核心内容**: 批判卷积神经网络(CNNs)的局限性，提出胶囊网络(Capsule Networks)的革新设计，并探讨自我监督学习的前景。  
  - [链接](./2020/20200210_AAAI_20_Keynotes_Turing_Award_Winners_Event_Geoff_Hinton.md)

### **8月**
- **2020/20200809 The Future of Neural Networks and Unsupervised Learning**  
  - **日期**: 8月9日
  - **视频类型**：技术讲座
  - **采访机构**：Special Interest Group on Information Retrieval，信息检索专业组，即SIGIR
  - **机构介绍**：SIGIR是国际计算机协会 ACM 旗下的核心学术组织之一，专注于信息检索（IR）、搜索引擎、推荐系统及相关领域的研究与技术发展。其年度旗舰会议 ACM SIGIR Conference 是信息检索领域的全球顶级会议，被誉为“IR领域的奥林匹克”  
  - **核心内容**: 探讨神经网络的过去与未来，重点阐述无监督学习的重要性、技术演进及应用潜力，同时反思大脑学习机制与深度学习的差异。  
  - [链接](./2020/20200809图灵奖得主Geoffrey%20Hinton最新演讲透露下一代神经网络模型的构想丨SIGIR%202020.md)

---

## 2021

### **5月**
- **2021/20210517 Is There a Mathematical Model of the Mind?**  
  - **日期**: 5月17日
  - **视频类型**：小组研讨会
  - **采访机构**：Google Tech Talks
  - **机构介绍**：Google Tech Talks是 Google 组织的一个技术讲座系列，旨在促进前沿科技知识的分享与交流。 
  - **成员**：Bin Yu - UC Berkeley，Geoffrey Hinton - University of Toronto and Google，Jack Gallant - UC Berkeley，
              Lenore Blum - CMU/UC Berkeley，Percy Liang - Stanford University ，Rina Panigrahy - Google (moderator)  
  - **核心内容**: 探索心智的数学模型可能性，对比人脑与深度学习系统的差异。  
  - [链接](./2021/20210517_Is_There_a_Mathematical_Model_of_the_Mind_Panel_Discussion.md)

### **8月**
- **2021/20210823 Distillation and the brain**  
  - **日期**: 8月23日
  - **视频类型**：技术讲座  
  - **核心内容**: 大脑如何通过“蒸馏”（Distillation）机制实现知识共享，提出“通用胶囊”（Universal Capsules）架构与脑科学模型的关联性。  
  - [链接](./2021/20210823Distillation%20and%20the%20brain.md)

---

## 2022

### **6月**
- **2022/20220601 Insights into Neural Networks and AI Evolution**  
  - **日期**: 6月1日
  - **视频类型**：人物访谈
  - **采访机构**：The Robot Brains Podcast
  - **机构介绍**："The Robot Brains Podcast" 是一档专注于人工智能（AI）领域的播客节目，它通过深入的访谈和讨论，探索AI技术的发展及其对社会的影响。这档播客由Pieter Abbeel主持，他是加州大学伯克利分校的教授，同时也是AI研究领域的重要人物之一。
  - **主持人**：Pieter Abbeel
  - **核心内容**: 探讨了神经网络的工作原理、无监督学习的重要性、卷积神经网络（ConvNets）的局限性以及未来可能的发展方向。 
  - [链接](./2022/20220601eason%202%20Ep%2022%20Geoff%20Hinton%20on%20revolutionizing%20artificial%20intelligence...%20again.md)

### **8月**
- **2022/20220812 Representing Part-Whole Hierarchies in a Neural Network**  
  - **日期**: 8月12日
  - **视频类型**：大学讲座
  - **采访机构**：Stanford University，即斯坦福大学
  - **机构介绍**：斯坦福大学是位于美国加利福尼亚州的一所私立研究型大学，成立于1885年。它以其卓越的教学质量、丰富的科研资源和创新精神在全球享有极高的声誉。
  - **核心内容**: 演讲结合认知心理学实验、计算机视觉任务和自然语言处理模型（如BERT），阐述如何通过层级化动态路由实现生物可解释的视觉解析树（parse tree）建模。 
  - [链接](./2022/20220812Stanford%20CS25%20V2%20I%20Represent%20part-whole%20hierarchies%20in%20a%20neural%20network.md)

---

## 2023

### **2月**
- **2023/20230222 The Forward-Forward Algorithm: A New Approach to Training Neural Networks**  
  - **日期**: 2月22日
  - **视频类型**：演讲
  - **采访机构**：MoroccoAI Conference
  - **机构介绍**：MoroccoAI Conference 是摩洛哥及北非地区聚焦人工智能（AI）技术发展与行业应用的重要会议，旨在推动本地及全球AI生态的交流与合作。尽管该会议的历史相对较短（可能于近年发起），但其目标明确——通过连接学术界、企业界和政策制定者，加速AI技术在北非及阿拉伯语地区的落地与创新。  
  - **核心内容**: 探讨了神经网络的新训练方法——前向-前向算法（Forward-Forward Algorithm），并讨论了无监督学习、卷积神经网络的局限性以及未来的发展方向。  
  - [链接](./2023/20230325_Godfather_of_artificial_intelligence_talks_impact_and_potential_of_new_AI.md)

### **3月**
- **2023/20230325 _Godfather of artificial intelligence_ talks impact and potential of new AI**  
  - **日期**: 3月25日
  - **视频类型**：新闻采访
  - **采访机构**：Columbia Broadcasting System, CBS
  - **机构介绍**：CBS是美国三大全国性商业广播电视网之一，成立于1927年，总部位于纽约。CBS提供新闻、娱乐、体育等多种类型的节目，并在全球范围内拥有广泛的影响力。
  - **采访人**：Brooke Silva-Braga 
  - **核心内容**: 记者Brooke Silva-Braga探访多伦多AI研究重镇，采访Hinton及其弟子对ChatGPT等技术的看法，涉及技术原理、应用场景与伦理争议 
  - [链接](./2023/20230325_Godfather_of_artificial_intelligence_talks_impact_and_potential_of_new_AI.md)

### **5月**
- **2023/20230502 The Godfather of AI Quits Google Over Dangers of Artificial Intelligence**  
  - **日期**: 5月2日
  - **视频类型**：新闻采访
  - **采访机构**：BBC News，即British Broadcasting Corporation, BBC旗下的新闻部门。
  - **机构介绍**：它是全球最具影响力的新闻媒体之一。BBC News不仅为英国本土提供详尽的新闻报道，还以其全球视角和深入洞察影响着世界各地的信息流动。  
  - **核心内容**: 反思 AI 发展的风险，警告人工智能可能超越人类智能，并被恶意利用。  
  - [链接](./2023/20230502_AI_godfather_quits_Google_over_dangers_of_Artificial_Intelligence_-_BBC_News.md)
    
- **2023/20230503 AI May Figure Out How to Kill People – Geoffrey Hinton**  
  - **日期**: 5月3日
  - **视频类型**：新闻采访
  - **采访机构**：美国有线电视新闻网（Cable News Network，简称CNN）
  - **机构介绍**：CNN是一个在全球范围内极具影响力的新闻媒体。
  - **核心内容**: 反思 AI 发展潜在的风险，警告 AI 可能会学会操纵甚至伤害人类。  
  - [链接](./2023/20230503_Godfather_of_AI_warns_that_AI_may_figure_out_how_to_kill_people.md)
    
- **2023/20230506 Possible End of Humanity from AI**  
  - **日期**: 5月6日
  - **视频类型**：技术研讨会
  - **采访机构**：Massachusetts Institute of Technology，简称MIT，即麻省理工学院
  - **机构介绍**：这是一所位于美国马萨诸塞州剑桥市的世界顶尖私立研究型大学，不仅是一个培养高级科技人才的摇篮，也是一个推动科学技术前沿探索的重要力量。
  - **核心内容**: AI技术（尤其是大语言模型）的潜在生存威胁，数字智能超越生物智能的可能性，以及人类应对策略的探讨。  
  - [链接](./2023/20230506_Possible_End_of_Humanity_from_AI_Geoffrey_Hinton_at_MIT_Technology_Review_EmTech_Digital.md)
    
- **2023/20230509 Godfather of AI discusses dangers the developing technologies pose to society**  
  - **日期**: 5月9日
  - **视频类型**：新闻采访
  - **采访机构**：Amanpour and Company
  - **机构介绍**：Amanpour and Company 是美国公共电视网（PBS）与英国第四频道（Channel 4）联合制作的深度新闻访谈节目。
  - **采访人**：Christiane Amanpour。
  - **核心内容**: 人工智能的潜在风险，包括超级智能AI失控的可能性。  
  - [链接](./2023/20230509_Godfather_of_AI_discusses_dangers_the_developing_technologies_pose_to_society.md)
    
- **2023/20230511 Geoffrey Hinton helped create AI. Now he’s worried it will destroy us.**  
  - **日期**: 5月11日
  - **视频类型**：新闻采访
  - **采访机构**：Columbia Broadcasting System, CBS
  - **机构介绍**：CBS是美国三大全国性商业广播电视网之一，成立于1927年，总部位于纽约。CBS提供新闻、娱乐、体育等多种类型的节目，并在全球范围内拥有广泛的影响力。
  - **采访人**：Adrienne Arseualt  
  - **核心内容**: 探讨了AI技术的发展现状、潜在风险以及Hinton对未来的担忧，特别是关于AI可能带来的伦理和社会问题。  
  - [链接](./2023/20230511_Geoffrey_Hinton_helped_create_AI_Now_he_is_worried_it_will_destroy_us.md)

### **6月**
- **2023/20230605 Two Paths to Intelligence**  
  - **日期**: 6月5日
  - **视频类型**：讲座
  - **采访机构**：University of Cambridge，即剑桥大学
  - **机构介绍**：剑桥大学是一所位于英国英格兰剑桥市的世界著名公立研究型大学，是英语世界中第二古老的大学，也是世界现存第四古老的大学。它的前身是一个学者协会。 
  - **核心内容**: 对比数字计算（Digital Computation）与生物计算（Biological Computation）的优劣，探讨人工智能超越人类智能的可能性及潜在风险。  
  - [链接](./2023/20230605_Geoffrey_Hinton_Two_Paths_to_Intelligence.mdd)
    
- **2023/20230623 The Godfather in Conversation Why Geoffrey Hinton is worried about the future of AI**  
  - **日期**: 6月23日
  - **视频类型**：人物访谈
  - **采访机构**：University of Toronto，即多伦多大学
  - **机构介绍**：是加拿大最古老、最大的大学之一，位于安大略省的多伦多市。它成立于1827年，最初名为“国王学院”，直到1849年才改为现名并成为一所非宗教性质的学府。 
  - **核心内容**: AI技术突变的潜在风险、数字智能与生物智能的本质差异、社会应对策略。  
  - [链接](./2023/20230623_The_Godfather_in_Conversation_Why_Geoffrey_Hinton_is_worried_about_the_future_of_AI.md)

### **7月**
- **2023/20230720 In conversation with the Godfather of AI**  
  - **日期**: 7月20日
  - **视频类型**：人物访谈
  - **采访机构**：Collision Conference
  - **机构介绍**：Collision Conference是一个备受瞩目的科技会议，被誉为北美发展最快的科技大会之一，也是世界上规模最大、最具影响力的科技盛会之一。该会议旨在汇集全球科技产业的领导者与创新公司，共同探讨当今科技领域的热点问题和未来趋势。
  - **主持人**：Nick Thompson  
  - **核心内容**: 综合讨论AI伦理、技术与未来挑战。  
  - [链接](./2023/20230720_In_conversation_with_the_Godfather_of_AI.md)

### **8月**
- **2023/20230826 The Godfather of A.I. Geoffrey Hinton and Andrew Ng say that AI models understand the world**  
  - **日期**: 8月26日
  - **视频类型**：人物访谈
  - **采访人**：Andrew Ng，即吴恩达  
  - **核心内容**: 与Andrew Ng共同探讨AI模型对世界的理解能力。  
  - [链接](./2023/20230826_The_Godfather_of_A_I_Geoffrey_Hinton_and_Andrew_Ng_say_that_AI_models_understand_the_world.md)

### **9月**
- **2023/20230900 AI's Potential and Perils**  
  - **日期**: 9月
  - **视频类型**：新闻采访
  - **采访机构**：The 60 Minutes Interview
  - **机构介绍**："60 Minutes" 是美国哥伦比亚广播公司（CBS）制作并播出的一档知名新闻杂志节目，自1968年开始播出以来，它已经成为电视新闻报道的一个标志性节目。该节目以其深入的调查报告、尖锐的问题和对重要人物的访谈而闻名。
  - **采访人**：Scott Pelley
  - **核心内容**: 探讨人工智能（AI）的起源、当前能力、未来发展及其潜在风险与益处，Hinton 从神经网络先驱的视角反思技术影响。  
  - [链接](./2023/20230900_Godfather_of_AI_Geoffrey_Hinton_The_60_Minutes_Interview.md)

### **10月**
- **2023/20230104 Geoffrey Hinton in conversation with Fei-Fei Li — Responsible**  
  - **日期**: 10月4日
  - **视频类型**：技术讨论
  - **采访机构**：Radical Ventures
  - **机构介绍**：Radical Ventures是一家位于加拿大多伦多的风险投资公司，专注于早期人工智能（AI）初创公司的投资。自2017年成立以来，该公司已经迅速成长为在AI领域颇具影响力的投资机构之一。 
  - **核心内容**: 从ImageNet到ChatGPT的AI发展历程，以及AI对社会的影响与责任。  
  - [链接](./2023/20231004_Geoffrey_Hinton_in_conversation_with_Fei_Fei_Li_Responsible.md)

### **12月**
- **2023/202301209 大型语言模型在医学中的理解与共情能力**  
  - **日期**: 12月9日
  - **视频类型**：技术讨论
  - **采访机构**：Ground Truths
  - **机构介绍**：Ground Truths是一个由美国著名医学专家Eric Topol医学博士创办的播客(Podcast)和在线内容平台，专注于探讨医学、科学、技术(尤其是人工智能)与社会的交叉领域。其核心目标是揭示复杂议题背后的“真实”(Ground Truth)，即基于证据、数据和科学的事实，而非猜测或炒作。
  - **采访人**：Eric Topol 
  - **核心内容**: 探讨AI在医疗领域的突破性应用及其对人类智能的挑战。  
  - [链接](./2023/20231209Geoffrey_Hinton_Large_Language_Models_in_Medicine_They_Understand_and_Have_Empathy.md)
  
- **2023/202301216 Will Digital Intelligence Replace Biological Intelligence?**  
  - **日期**: 12月16日
  - **视频类型**：技术讲座
  - **采访机构**：2023 Arthur Miller Lecture in Science and Ethics
  - **机构介绍**：2023 Arthur Miller Lecture in Science and Ethics 是一项以科学史学家、作家 Arthur I. Miller 命名的年度讲座，聚焦于科学进步与伦理挑战的交汇点。该讲座通常由顶尖科学家、哲学家或公共知识分子主讲，探讨技术革新背后的道德困境与社会责任。
  - **核心内容**: 数字计算与生物计算的本质差异，大型语言模型的理解能力，以及超级智能的伦理挑战。  
  - [链接](./2023/20231216Geoffrey_Hinton_discussed_Will_Digital_Intelligence_Replace_Biological_Intelligence.md)
   
---

## 2024

### **2月**
- **2024/20240208 AI could be smarter than people in 20 years**  
  - **日期**: 2月8日
  - **视频类型**：新闻采访
  - **采访机构**：Columbia Broadcasting System, CBS
  - **机构介绍**：CBS是美国三大全国性商业广播电视网之一，成立于1927年，总部位于纽约。CBS提供新闻、娱乐、体育等多种类型的节目，并在全球范围内拥有广泛的影响力。
  - **采访人**：Travis Dhanraj   
  - **核心内容**: 预测AI在20年内可能超越人类智能。  
  - [链接](./2024/20240208AI_could_be_smarter_than_people_in_20_years.md)

- **2024/20240229 eoffrey Hinton 教授在 Sheldonian Romanes Lecture**  
  - **日期**: 2月29日
  - **视频类型**：技术讲座
  - **采访机构**：University of Oxford，即牛津大学
  - **机构介绍**：牛津大学是英语世界历史最悠久的大学，也是全球顶尖的研究型学府之一，不仅是学术圣地，更是人类文明演进的缩影。  
  - **核心内容**: 在牛津大学Sheldonian剧院的演讲，探讨AI与人类智能的未来。  
  - [链接](./2024/20240229_Geoffrey_Hinton_教授在_Sheldonian.md)

### **4月**
- **2024/20240408 Geoffrey Hinton Awarded UCD Ulysses Medal: Key Insights from the 2024 Ceremony**  
  - **日期**: 4月8日
  - **视频类型**：颁奖讲座
  - **采访机构**：University College Dublin, UCD(即都柏林大学)
  - **机构介绍**：都柏林大学是爱尔兰规模最大、国际声誉最高的研究型大学之一，也是欧洲领先的高等教育机构。  
  - **核心内容**: 深度学习革命历程与AI伦理挑战。  
  - [链接](./2024/20240408Geoffrey_Hinton_Awarded_UCD_Ulysses_Medal_Key_Insights_from_the_2024_Ceremony.md)
  
- **2024/20240411 "Digital Superintelligence: Threat or Hope?" - Kurzweil & Hinton Debate**  
  - **日期**: 4月11日
  - **视频类型**：研讨会
  - **采访机构**：the 2024 Abundance360 Summit
  - **机构介绍**：2024 Abundance360 Summit 是由未来学家、企业家 Peter Diamandis（奇点大学联合创始人）主办的年度高端峰会，聚焦指数级技术（如人工智能、量子计算、合成生物学等）的颠覆性潜力及其对商业、社会和人类未来的影响。
  - **讨论人**：Ray Kurzweil
  - **主持人**：Peter Diamandis  
  - **核心内容**:数字智能与生物智能的本质差异。  
  - [链接](./2024/2024411Ray%20Kurzweil%20&%20Geoff%20Hinton%20Debate%20the%20Future.md)

### **5月**
- **2024/20240515 Geoffrey Hinton On working with Ilya Sutskever & The Evolution of AI**  
  - **日期**: 5月15日
  - **视频类型**：人物对话
  - **采访机构**：Sana AI
  - **机构介绍**：Sana AI 是由瑞典科技公司 Sana Labs 开发的一款企业级人工智能平台，专注于知识管理、学习与协作的智能化转型。其核心目标是通过AI技术整合组织内外的知识资源，提升团队效率与决策能力。
  - **对话人**：Joel Hellermark  
  - **核心内容**: 回顾与Ilya Sutskever的合作经历，反思AI发展的关键节点。  
  - [链接](./2024/20240515_Geoffrey_Hinton_On_working_with_Ilya.md)

### **6月**
- **2024/20240607 Keynote interview with Geoffrey Hinton (remote) and Nicholas Thompson (in-person)**  
  - **日期**: 6月7日
  - **视频类型**：主题访谈
  - **采访机构**：AI for Good Global Summit(人工智能向善全球峰会)
  - **机构介绍**：AI for Good Global Summit是由 联合国国际电信联盟（ITU） 牵头，联合 40余家联合国机构（如UNESCO、WHO、WFP等）共同主办的全球性年度峰会，旨在推动人工智能技术加速实现联合国 可持续发展目标（SDGs），同时确保技术应用的伦理与包容性。
  - **主持人**：Nicholas Thompson  
  - **核心内容**: AI技术发展带来的机遇与生存威胁，数字智能超越生物智能的机制，以及社会监管框架的紧迫需求。  
  - [链接](./2024/20240607_Keynote_interview_with_Geoffrey_Hinton_remote_and_Nicholas_Thompson_in_person.md)

- **2024/20240615 AI will become smarter than humans Geoffrey Hinton|BNN Bloomberg**  
  - **日期**: 6月15日
  - **视频类型**：新闻采访
  - **采访机构**：BNN Bloomberg
  - **机构介绍**：BNN Bloomberg是加拿大一个专注于商业新闻的电视频道和服务，它结合了Business News Network (BNN) 和 Bloomberg LP 的资源，提供深入的市场分析、金融资讯及经济报道。
  - **核心内容**: AI超越人类智能的必然性、失控风险与安全治理路径。  
  - [链接](./2024/20240615_AI_will_become_smarter_than_humans_Geoffrey_Hinton.md)

- **2024/20240628 Q&A with Geoffrey Hinton**  
  - **日期**: 6月28日
  - **视频类型**：新闻采访  
  - **核心内容**: 问答环节中讨论AI对就业、医疗及社会结构的长期影响。  
  - [链接](./2024/20240628_Q_and_A_with_Geoffrey_Hinton.md)

### **7月**
- **2024/20240702 Geoffrey Hinton 担忧 AI 的未来**  
  - **日期**: 7月2日
  - **视频类型**：人物访谈  
  - **核心内容**: 表达对AI失控风险的担忧，呼吁全球合作制定安全协议。  
  - [链接](./2024/20240702_Geoffrey_Hinton_担忧_AI_的未来.md)

### **10月**
- **2024/20241009 ‘Godfather of AI’ on AI “exceeding human intelligence” and it “trying to take over|BBC Newsnight”**  
  - **日期**: 10月9日
  - **视频类型**：人物访谈
  - **采访机构**：British Broadcasting Corporation，简称BBC，即英国广播公司。
  - **机构介绍**：英国广播公司是英国的公共广播公司，也是世界上最大的广播组织之一。
  - **采访人**：Faisal Islam  
  - **核心内容**: 强调AI超越人类智能的紧迫性，并警告技术失控的潜在威胁。  
  - [链接](./2024/20241009_Godfather_of_AI_on_AI_exceeding_human_intelligence_and_trying_to_take_over.md)

- **2024/20241009 多伦多校长线上会议hinton|University of Toronto Press Conference**  
  - **日期**: 10月9日
  - **视频类型**：会议采访
  - **采访机构**：University of Toronto，即多伦多大学
  - **机构介绍**：是加拿大最古老、最大的大学之一，位于安大略省的多伦多市。它成立于1827年，最初名为“国王学院”，直到1849年才改为现名并成为一所非宗教性质的学府。
  - **采访人**：Meric Gertler  
  - **核心内容**: 与多伦多大学校长讨论AI教育、研究及伦理治理。  
  - [链接](./2024/20241009多伦多校长线上会议hinton.md)

- **2024/20241010 瑞典皇家科学院宣布 2024 年诺贝尔物理学奖获奖者及成果介绍**  
  - **日期**: 10月10日
  - **视频类型**：颁奖演讲
  - **采访机构**：瑞典皇家科学院(Royal Swedish Academy of Sciences)
  - **机构介绍**：瑞典皇家科学院是瑞典的一个重要学术机构，成立于1739年，总部设在瑞典首都斯德哥尔摩。它是一个独立的非政府组织，旨在促进科学，特别是自然科学和数学的发展。 
  - **核心内容**: 表彰John Hopfield和Geoffrey Hinton在人工神经网络领域的奠基性贡献。  
  - [链接](./2024/20241010_瑞典皇家科学院宣布_2024_年诺贝尔物理学奖获奖者及成果介绍.md)

### **11月**
- **2024/20241116 Questions & Answers with Dr. Geoffrey Hinton - Turing Minds 2024|Turing Minds 2024**  
  - **日期**: 11月16日
  - **视频类型**：技术问答
  - **采访机构**：Georgia Institute of Technology，即乔治亚理工学院
  - **机构介绍**：乔治亚理工学院，是一所位于美国乔治亚州亚特兰大市的顶尖公立研究型大学。该校以其工程学、计算机科学和信息技术课程闻名于世，但同时也提供了包括商业管理、人文科学、建筑设计等多个领域的优秀教育项目。
  - **主持人**：Parsa Khazaeepoul和Zack Axel  
  - **核心内容**: 在Turing Minds会议上回答公众提问，涵盖AI伦理、监管及技术突破。  
  - [链接](./2024/20241116_Questions_and_Answers_with_Dr_Geoffrey_Hinton_Turing_Minds_2024.md)

### **12月**
- **2024/20241201 AI教父Hinton十一月访谈|KBS**  
  - **首映日期**: 12月1日
  - **视频类型**：技术访谈
  - **采访机构**：KBS指的是韩国放送公社
  - **机构介绍**：KBS是韩国最具代表性和历史最为悠久的公共广播电视台之一。  
  - **核心内容**: 深度学习的生物学基础、AI技术的社会影响、超级智能的伦理挑战。  
  - [链接](./2024/20241201_AI教父Hinton_十一月KBS访谈.md)

- **2024/20241205 Seminar with Professor Geoffrey Hinton**  
  - **日期**: 12月5日
  - **视频类型**：小组讨论
  - **采访机构**：Kungliga Ingenjörsvetenskapsakademien，简称IVA，即瑞典皇家工程科学院
  - **机构介绍**：瑞典皇家工程科学院是全球历史最悠久的工程科学学术机构之一，成立于1919年。它位于瑞典，并且在推动工程科学、经济和技术领域的进步方面扮演了重要角色。
  - **小组成员**：Kia Höök、Anders Sandberg、Staffan Truvé和Anette Novak  
  - **核心内容**: 批判传统卷积神经网络（ConvNets）的局限性，提出“胶囊网络”（Capsule Networks）的架构设计。  
  - [链接](./2024/20241205_Seminar_with_Professor_Geoffrey_Hinton_Critique_of_ConvNets_and_Introduction_to_Capsule_Networks.md)

- **2024/20241208 Nobel Prize Lecture by Geoffrey Hinton**  
  - **日期**: 12月8日
  - **视频类型**:颁奖演讲
  - **采访机构**：Nobel Prize，即诺贝尔奖。
  - **机构介绍**：诺贝尔奖（Nobel Prize）是根据瑞典发明家阿尔弗雷德·诺贝尔的遗嘱设立的一系列国际奖项，旨在奖励那些在物理学、化学、生理学或医学、文学以及和平领域为人类做出最大贡献的人士。  
  - **核心内容**: 玻尔兹曼机（Boltzmann Machines）的理论突破及其对深度学习的奠基性贡献。  
  - [链接](./2024/20241208_Nobel_Prize_lecture_Geoffrey_Hinton_Boltzmann_Machines_and_the_Deep_Learning_Revolution.md)

- **2024/20241212 Geoffrey Hinton: "AI教父在获得VinFuture奖时的讲话"**  
  - **日期**: 12月12日
  - **视频类型**：颁奖采访
  - **采访机构**：VinFuture Foundation
  - **机构介绍**：VinFuture Foundation 是一个成立于2020年12月20日的非营利组织，由越南首富 Phạm Nhật Vượng 及其妻子 Phạm Thu Hương 创立。该基金会致力于通过表彰和奖励具有突破性的科技创新来推动全球科技和社会进步。VinFuture Prize 是其核心项目，旨在鼓励那些能够对日常生活产生重大积极影响并有助于解决全球性挑战的科学和技术成就。  
  - **核心内容**: 探讨了人工智能领域的关键人物及其贡献，讨论了奖项的意义、技术预测及对未来的展望。  
  - [链接](./2024/20241212_Geoffrey_Hinton_AI教父在获得VinFuture奖时的讲话.md)

- **2024/20241218 AI Unpacked with Nobel Laureate Geoffrey Hinton**  
  - **日期**: 12月18日
  - **视频类型**：人物访谈
  - **采访机构**：Valence
  - **机构介绍**：Valence 是一家专注于 AI 驱动的组织教练解决方案的公司，特别关注人才发展和领导力提升。其核心产品是一个名为 Nadia's AI 教练，旨在为经理提供个性化的、始终可用的教练服务，适应每个组织的文化和价值观。 
  - **核心内容**: 探讨了人工智能的发展历程、关键突破及其对未来的展望，特别强调了深度学习的重要性及面临的挑战。  
  - [链接](./2024/20241218_AI_Unpacked_with_Nobel_Laureate_Geoffrey_Hinton.md)

- **2024/20241223 AI教父在InfoTech Live 2023上的访谈**  
  - **日期**: 12月23日
  - **视频类型**：人物访谈
  - **采访机构**：Info-Tech Research Group
  - **机构介绍**：Info-Tech Research Group 是一家提供战略、技术和研究服务的信息技术（IT）咨询公司，它帮助企业中的首席信息官（CIOs）和IT领导者做出战略性决策。
  - **采访人**：Robert Meikle  
  - **核心内容**: 探讨了人工智能的发展历程、关键突破及其对未来的展望，特别强调了深度学习的重要性及面临的挑战。  
  - [链接](./2024/20241223_DIGITP_Executive_Sponsor_Robert_Meikle_interviews_Geoffrey_Hinton.md)

- **2024/20241229 Even in 5 years we will create AGI. Superintelligence**  
  - **日期**: 12月29日
  - **视频类型**：技术讲座
  - **采访机构**：瑞典皇家科学院(Royal Swedish Academy of Sciences)
  - **机构介绍**：瑞典皇家科学院是瑞典的一个重要学术机构，成立于1739年，总部设在瑞典首都斯德哥尔摩。它是一个独立的非政府组织，旨在促进科学，特别是自然科学和数学的发展。
  - **核心内容**: 探讨了AI的发展现状、技术突破及其对未来的展望，特别是关于通用人工智能（AGI）的预测和超级智能的风险。  
  - [链接](./2024/20241229_Even_in_5_years_we_will_create_AGI_Superintelligence.md)

---

## 2025

### **1月**
- **2025/20250118 Why The Godfather of AI Now Fears His Own Creation**  
  - **日期**: 1月18日
  - **视频类型**：技术讨论
  - **采访机构**：Theories of Everything，简称万物理论
  - **机构介绍**："Theories of Everything" 是一个由博主 Curt Jaimungal 主持的频道和播客，专注于深度探讨科学、哲学和技术等领域的重要话题。Curt Jaimungal 对话的对象通常是各个领域的专家、学者和思想领袖。
  - **采访人**：Curt Jaimungal 
  - **核心内容**: Hinton反思AI技术的快速发展及其对人类社会的潜在威胁，探讨AI意识、安全性及伦理问题。  
  - [链接](./2025/20250118_Why_The_Godfather_of_AI_Now_Fears_His_Own_Creation_Geoffrey_Hinton.md)

- **2025/20250126 教父对话：Geoffrey Hinton为何担忧AI的未来**  
  - **日期**: 1月26日
  - **视频类型**：人物访谈
  - **采访机构**：University of Toronto，即多伦多大学
  - **机构介绍**：是加拿大最古老、最大的大学之一，位于安大略省的多伦多市。它成立于1827年，最初名为“国王学院”，直到1849年才改为现名并成为一所非宗教性质的学府。  
  - **核心内容**: 从神经网络先驱到AI风险警示者——分析数字智能的进化优势与生存风险。  
  - [链接](./2025/20250126_The_Godfather_in_Conversation_Why_Geoffrey_Hinton_is_worried_about_the_future_of_AI.md)

- **2025/20250131‘Godfather of AI’ predicts it will take over the world|LBC**  
  - **日期**: 1月31日
  - **视频类型**：新闻采访
  - **采访机构**：London Broadcasting Company，简称LBC，即伦敦广播公司
  - **机构介绍**：伦敦广播公司是一家位于英国的广播电台。它最初成立于1973年，是英国首个商业广播电台，主要服务于伦敦地区。LBC 的成立标志着英国广播业的一个重要里程碑，因为它打破了BBC长期以来对广播市场的垄断。
  - **采访人**：Andrew Marr  
  - **核心内容**: AI发展速度、失控风险、就业冲击及监管挑战。  
  - [链接](./2025/20250131_Godfather_of_AI_predicts_it_will_take_over_the_world_LBC.md)

### **2月**
- **2025/20250204 Geoffrey Hinton: Consciousness & Control in AI Systems**  
  - **日期**: 2月4日
  - **视频类型**：技术问答  
  - **核心内容**: 大语言模型的意识可能性、智能体自主目标形成的风险机制，以及社会应对策略。  
  - [链接](./2025/20250204_dtv_net_25_Geoff_Hinton_s_Latest_Interview_Are_LLMs_Conscious.md)

### **3月**
- **2025/20250315 Geoffrey Hinton on AI Risks and Personal Reflections**  
  - **日期**: 3月15日
  - **视频类型**：获奖采访
  - **采访机构**：Nobel Prize，即诺贝尔奖。
  - **机构介绍**：诺贝尔奖（Nobel Prize）是根据瑞典发明家阿尔弗雷德·诺贝尔的遗嘱设立的一系列国际奖项，旨在奖励那些在物理学、化学、生理学或医学、文学以及和平领域为人类做出最大贡献的人士。   
  - **核心内容**: AI发展时间线、存在性风险、科学伦理与个人科研历程。  
  - [链接](./2025/20250315_Geoffrey_Hinton.md)
