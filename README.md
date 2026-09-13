# AI-STUDY

개인 **AI / Machine Learning / Computer Vision 학습 기록 저장소**입니다.

단순히 강의 내용을 정리하는 데서 끝내지 않고,
**알고리즘 문제 해결 능력 → ML/DL 기본기 → Computer Vision → 실전 AI/ML Engineering**으로 이어지는 과정을 꾸준히 기록하는 것을 목표로 합니다.

현재는 **알고리즘 심화 학습과 딥러닝 입문 단계까지 진행**했으며, 앞으로 Computer Vision과 실제 AI 시스템 구현 역량으로 확장할 예정입니다.

---

## Current Progress

### Algorithms & Problem Solving

* Python 기반 알고리즘 문제 풀이
* 자료구조 및 알고리즘 기초 학습
* 구현 / 완전탐색 / 정렬 / 이분 탐색
* Stack / Queue / Hash
* DFS / BFS
* Dynamic Programming
* Greedy
* Graph 문제 풀이
* 백준 중심의 지속적인 문제 해결 연습

현재는 기초 문법 및 단순 구현 단계를 넘어 **중급 알고리즘 문제 해결 능력을 강화하는 단계**입니다.

> Code: [`algorithms/baekjoon`](./algorithms/baekjoon)

### Deep Learning

현재 **딥러닝 입문 및 기본 모델 학습 단계**까지 진행했습니다.

학습 범위:

* Machine Learning / Deep Learning 기본 개념
* Neural Network 구조 이해
* Forward / Backpropagation
* Loss Function과 Optimizer
* Training / Validation 과정
* Overfitting과 Regularization
* CNN 기본 구조 및 이미지 분류
* PyTorch 기반 모델 학습 흐름 이해

앞으로는 단순 모델 사용보다 **모델의 동작 원리와 실험 결과를 설명할 수 있는 수준**까지 기본기를 강화할 예정입니다.

---

## Study Direction

앞으로의 학습은 다음 흐름으로 진행합니다.

```text
Algorithms & Data Structures
            ↓
Machine Learning Fundamentals
            ↓
Deep Learning Fundamentals
            ↓
Computer Vision
            ↓
Video / 3D Perception
            ↓
Model Optimization & Deployment
            ↓
Real-world AI/ML Engineering
```

최종적으로는 **Computer Vision / Perception 중심의 AI/ML Engineer**로서 실제 영상과 센서 데이터를 처리하고 모델을 시스템에 적용할 수 있는 역량을 갖추는 것이 목표입니다.

---

## Roadmap

### 1. Algorithm Fundamentals ✅

* Python 기본 문법
* Array / String
* Stack / Queue
* Hash
* Sorting
* Binary Search
* Recursion
* DFS / BFS
* Basic DP

### 2. Advanced Algorithm Practice 🚧

* Graph
* Dynamic Programming
* Greedy
* Implementation / Simulation
* 문제 유형별 풀이 전략 정리
* 시간복잡도와 공간복잡도를 고려한 구현

**Goal**

* 중급 난이도 문제를 스스로 분석하고 해결하기
* 풀이 이후 더 나은 접근법과 복잡도를 설명할 수 있기

### 3. Deep Learning Fundamentals 🚧

* Neural Network
* Backpropagation
* Optimizer / Learning Rate
* Regularization
* CNN
* Transfer Learning
* PyTorch training pipeline

**Goal**

* 모델을 단순히 호출하는 것이 아니라 학습 과정을 이해하고 구현하기
* 실험 결과와 failure case를 분석할 수 있기

### 4. Computer Vision 📌

다음 단계부터 본격적으로 진행할 영역입니다.

* Image Processing
* OpenCV
* Classification
* Object Detection
* Segmentation
* Multi-Object Tracking
* Pose / Keypoint Estimation
* Video Understanding

이후에는 다음과 같은 전통적인 Computer Vision 기본기도 함께 학습할 예정입니다.

* Camera Model
* Coordinate System
* Camera Calibration
* Homography
* PnP
* Epipolar Geometry
* Stereo / Depth

### 5. AI/ML Engineering 📌

모델 학습 이후 실제 시스템에서 사용할 수 있는 수준까지 확장합니다.

* C++
* OpenCV with C++
* Linux
* Docker
* ONNX
* TensorRT
* Edge Inference
* ROS2
* Sensor / Perception Pipeline

---

## Repository Structure

현재 저장소는 학습 진행에 따라 점진적으로 확장하고 있습니다.

```text
AI-STUDY/
├── README.md
├── algorithms/
│   └── baekjoon/       # 알고리즘 문제 풀이
└── plans/              # 학습 계획 및 기록
```

추후 학습이 진행되면서 다음 영역을 추가할 예정입니다.

```text
ml-basics/
deep-learning/
computer-vision/
cpp/
notes/
```

폴더를 먼저 만들어 두기보다 **실제로 공부하고 구현한 내용이 생길 때 기록을 추가하는 방식**으로 관리합니다.

---

## Study Principles

### 1. 직접 구현하기

라이브러리를 사용하는 것에서 끝내지 않고, 가능한 범위에서는 핵심 아이디어를 직접 코드로 구현합니다.

### 2. 이유를 설명하기

코드가 동작하는 것뿐 아니라 다음 질문에 답할 수 있도록 공부합니다.

* 왜 이 알고리즘을 사용하는가?
* 시간복잡도는 어떻게 되는가?
* 왜 이 모델 또는 Loss를 선택했는가?
* 성능이 좋거나 나쁜 이유는 무엇인가?
* 실제 환경에서는 어떤 문제가 발생할 수 있는가?

### 3. Experiment-driven Learning

AI 학습에서는 결과 숫자 하나보다 다음 과정을 중요하게 생각합니다.

```text
Problem Definition
      ↓
Baseline
      ↓
Experiment
      ↓
Evaluation
      ↓
Failure Analysis
      ↓
Improvement
```

### 4. 꾸준히 기록하기

완벽하게 정리된 결과만 올리기보다 **문제를 해결하고 이해해 가는 과정 자체를 기록**합니다.

---

## Long-term Goal

이 저장소의 목표는 많은 기술 이름을 나열하는 것이 아닙니다.

장기적으로는 다음 능력을 갖춘 엔지니어로 성장하는 것을 목표로 합니다.

> **Python과 C++을 기반으로 AI/ML 모델을 이해하고 구현하며, Computer Vision과 실제 센서 데이터를 활용해 현실 세계의 문제를 해결할 수 있는 엔지니어**

앞으로 알고리즘, 딥러닝, Computer Vision, Perception, 모델 최적화 및 배포까지 학습 범위를 단계적으로 확장해 나갈 예정입니다.
