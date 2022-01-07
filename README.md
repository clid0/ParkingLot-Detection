       <p align="center">
  <img src="https://user-images.githubusercontent.com/19771164/148502115-a99d69d5-c5ae-4d3b-be4c-88e2a8014fe9.png" alt="Sublime's custom image"/>
</p>

# Team DI 주제

### “아니, 쏘카존에 반납하려니까 만석이라 다른 곳에 주차했더니 패널티라네요.”

![뉴스](https://user-images.githubusercontent.com/19771164/148502420-82ad41be-a154-4dd5-9c88-707636e15700.png)(http://www.newsworker.co.kr/news/articleView.html?idxno=113012)

- 쏘카 반납 단계에서 예상치 못하게 추자공간이 없을 때 불편함을 겪는 사용자들이 존재
- → **“우리가 주차장의 상황을 알려주면 되지 않을까?”**

### 주차장 상황 및 주차 가능 여부 정보 제공
                 
<p align="center">
  <img src="https://user-images.githubusercontent.com/19771164/148516059-91da5206-12af-45cb-9737-20854d1df2bb.gif" alt="Sublime's custom image"/>
</p>




## 주차장에서 어떤 요소들이 중요할까?

- ### **실내 주차장 / 실외 주차장**이 중요할 것이라 판단  

     

- ### 주차장의 종류와 관계없이 **카메라 각도**가 중요할 것이라 판단

    

- ### 주차장 자체가 중요할 것이라 판단
<br>

  
  

## 어떤 모델을 사용할까?  

### [Yolo v5](https://github.com/ultralytics/yolov5)

- 현재 Object detection에서 뛰어난 성능을 보이고 있는 Yolo v5를 pretrained model로 활용  

- 각각 중요하다고 생각하는 요소에 맞춰 detect하도록 fine tuning  
<p align="left">
  <img width="500" height="300" src="https://user-images.githubusercontent.com/19771164/148505749-88dab2d1-7871-4ce5-b999-add485a4cbdb.png" alt="Sublime's custom image"/>
</p>



## 어떤 데이터를 사용할까?

- 실내 데이터의 경우 블랙박스보다는 cctv 이미지가 더욱더 의미가 있을 것이라 판단
- 문제는! 보안상 문제로 직접적으로 전달받을 수 있는 데이터셋이 없음  
-> 팀원 모두가 라벨링을 수작업으로 진행하기로 결정
- Dataset
    - **[PKLlot Dataset]()**
    - **[CNR Park]()**
    - **[Microsoft COCO 2017 Dataset](https://public.roboflow.com/object-detection/microsoft-coco-subset)**
  
---  
<br><br>
  
  
  

## 1차 시도(실외 vs 실내)

### 실내 주차장

<p align="left">
   
  <img width="500" height="300" src="https://user-images.githubusercontent.com/19771164/148506256-470dfb1b-0229-4fe1-a433-0a4a8750f53c.jpg" alt="Sublime's custom image"/>
</p>
   
- 공개되어있는 실내 주차장 데이터셋을 찾을 수 없음
- 모델을 돌릴 수 있을 정도의 양과 질의 데이터셋을 찾을 수 없음
- 개인정보 문제 등 여러 보안문제가 발생할 수 있음
- → 그래서 공개되어있는 실외 주차장 데이터셋을 최대한 활용하기로 결정

### 실외 주차장

- [PKLot 데이터](https://public.roboflow.com/object-detection/pklot)
    
    - Federal University of Parana에서 공개한 오픈 데이터로 자유로운 활용이 가능
    - Yolo에서 필요한 labels의 자료가 있어 잘할 수 있을 것이라 판단
     <p align="left">
       <img width="800" height="300" src="https://user-images.githubusercontent.com/19771164/148506281-70aab702-af54-4465-b46f-bdd7454c616a.png" alt="Sublime's custom image"/>
     </p>

- 학습 결과
     <p align="left">
       <img width="50%" height="50%" src="https://user-images.githubusercontent.com/19771164/148506719-c5d9d3f3-4175-47cc-b496-d6f5c8a52573.jpg" alt="Sublime's custom image"/>
     </p>



    
### 1차 시도의 결론 및 피드백

1. 실내 데이터는 개인정보의 문제로 인해 부족하기 때문에 실외 데이터로 진행
2. 라벨링을 일관되게 설정하는 것이 중요함을 알게 됨
3. PKLot 데이터가 train이 8000장이지만 4000장씩 2개의 카메라만 존재해서 생각보다 빠른 시간(5epoch에서)내에 overfitting에 도달  
  따라서 다른 데이터에 적용되기 힘듬
     <p align="left">
       <img width="50%" height="50%" src="https://user-images.githubusercontent.com/19771164/148506977-39bdaf18-35e7-463a-b6ff-c59d9abb62fd.png" alt="Sublime's custom image"/>
     </p>
    위 사진은 PKLot 학습과 비슷한 주차장, 아래 사진은 상이한 주차장

4. 카메라 각도가 비슷한 사진들은 80%까지 detect 하는 것을 보니 **카메라 각도**가 중요한 feature이지 않을까?  

---  
<br><br>

## 2차 시도(카메라 각도에 따른 학습)

### 데이터셋

- CNR park
    - 총 9개의 카메라로 한 주차장의 이미지를 수집한 데이터
    - 각 카메라는 다른 각도를 가지고 있기 때문에, 각 카메라 별로 따로 학습을 시켜주어 테스트 진행
    - 예시
        
        <p align="left">
          <img width="70%" height="70%" src="https://user-images.githubusercontent.com/19771164/148528862-8b403995-561c-43dc-9a24-ea564690e080.png" alt="Sublime's custom image"/>
          </p>
        
- 데이터 라벨링
    - 1차 시도에서 사용한 PKLot 데이터 라벨링 방식을 바탕으로 일관된 라벨링을 진행
    - [LabelImg](https://github.com/tzutalin/labelImg)을 (PASCAL VOC format, Yolov5 format 등을 지원)을 이용
    - <p align="left">
          <img width="70%" height="70%" src="https://user-images.githubusercontent.com/19771164/148529084-24b532e1-e4ee-4b04-9174-770ff7f17eaf.jpg" alt="Sublime's custom image"/>
          </p>
- 학습
     - 2번 카메라 
      
            
- 학습 및 결과
     - 2번 카메라 데이터
          - 2015/11/13 - 2015/11/29 train데이터 (260장)  
2015/12/01 - 2015/12/05 valid데이터(43장)  
2016/01/14 - 2016/01/16 test데이터(43장)
     - 2번 카메라 결과<p align="left">
          <img width="100%" height="70%" src="https://user-images.githubusercontent.com/19771164/148529709-ffe6a05a-6dbb-4330-8814-84009e4fedb0.png" alt="Sublime's custom image"/>
          </p>
     - 8번 카메라 데이터
          - 2015/11/13 - 2015/11/29 train데이터 (371장)  
2015/12/01 - 2015/12/05 valid데이터(38장)  
2016/01/14 - 2016/01/16 test데이터(40장)
     - 8번 카메라 결과<p align="left">
          <img width="100%" height="70%" src="https://user-images.githubusercontent.com/19771164/148529713-ad85bfe6-56db-4eb8-9dc2-6c0f75096d3b.png" alt="Sublime's custom image"/>
          </p>
     - 9번 카메라 데이터
          - 2015/11/13 - 2015/11/29 train데이터 (407장)  
2015/12/01 - 2015/12/05 valid데이터(43장)  
2016/01/14 - 2016/01/16 test데이터(40장)
     - 9번 카메라 결과<p align="left">
          <img width="100%" height="70%" src="https://user-images.githubusercontent.com/19771164/148529727-5090282c-4795-42c0-a707-974a80a7a89e.png" alt="Sublime's custom image"/>
          </p>
        
### 2차 시도의 결론 및 피드백

1. 한 주차장을 잘 학습한다면 해당 주차장의 다른 시간대에서 충분히 좋은 결과를 낼 수 있음
2. 비슷한 각도라고 판단되는 8번 카메라 모델로 다른 주차장에서 아쉬운 결과를 보이는데,   차와 빈 자리를 논리적으로 찾는 것이 아니라 라벨링 되어있는 그 부분의 **지형지물**을 학습하는 것으로 보임.   차량의 방향도 중요하지만 그 주차장 고유의 상황이 더 중요함
    - 8번 카메라 모델로 다른 test 결과
    
    <p align="left">
          <img width="70%" height="70%" src="https://user-images.githubusercontent.com/19771164/148531446-74dea4b5-4698-4046-a6cb-46cd63289fc1.png" alt="Sublime's custom image"/>
          </p>
    

    
3. 그렇다면 데이터가 많이 부족한 상황에서 **어떤 기법**을 사용하는 것이 좋을까?
        
 ---  
<br><br>
## 3차 시도(데이터 최적화)

데이터가 부족한 상황, 우린 어떻게 대처할 수 있을까?

→ 주차장 고유의 상황이 중요하다면, 서로 다른 주차장에서의 데이터는 서로 커버할 수 없을까?

- 데이터가 부족하니 data augmentation을 진행해보자
    - default 값에 적용되지 않는 방법들로 학습 진행(→image rotation, shear, mixup)
    - image rotation, shear, mixup의 기법을 사용한 결과, **같은 데이터셋**에서는 좋은 성능을 나타냄
        <p align="left">
          <img width="100%" height="70%" src="https://user-images.githubusercontent.com/19771164/148532040-cc581bd3-a2bb-4190-9b45-e555f723ac9c.png" alt="Sublime's custom image"/>
          </p>
### 3차 시도 결과 및 피드백

- 데이터가 많지 않은 상황에서 image augmentation은 성능을 향상시킬 수 있는 중요한 기법으로 사용될 수 있음
- 하지만 어떤 image augmentation 기법이, 얼마나 사용되어야 하는지는 각 데이터셋마다 다름
- 따라서, 하나의 모델을 사용하는 것은 많은 종류의 쏘카존을 보완해야하는 ‘확장성’의 문제에 부딪히게 된다.

---
<br><br>
## 4차 시도(확장성)

### 앙상블

- 주차장을 학습하는 것이 가장 좋은 방법이지만 많은 자원(시간, 인력)이 필요로 하기 때문에 이를 해결하고 서비스 형태가 되기 위해서 바로 투입이 가능한 형태의 모델이 필요하다고 판단
- 주차장의 지형지물이 아닌 car를 학습한 모델을 학습
- COCO 데이터 12,000장 학습한 모델
    - **[Microsoft COCO 2017 Datase](https://public.roboflow.com/object-detection/microsoft-coco-subset)t**
        
        COCO Dataset(121,408장)에서 차가 존재하는 이미지만을 사용해서 12,000장의 이미지로 학습을 진행

- COCO + augmentation COCO
    - 결과
        
        Yolov5와 비교하는 도표
        
        ![car_detect.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3f12336a-186a-41cc-9021-59c9991ac501/car_detect.png)
 
### 4차 시도 결과 및 피드백

- ‘car’만 12,000장 학습한 모델과 해당 데이터를 augmentation한 모델을 앙상블했을 때 결과가 상당히 좋음
- 차의 갯수가 확인이 되면 빈 자리의 여부도 알려줄 수 있음
     - 빈자리 수 - 전체 자리 수 - 차의 갯수
<br>
## 확장성을 위한 추가 기능들

### person blur(개인정보보호)
- '개인 정보'는 요즘 가장 중요한 이슈임
- 사진에서 사람을 분류하고 그 사람을 blur처리해서 개인 정보 문제에 대응
- 학습
     - Microsoft COCO 2017 Dataset 데이터 10,000장의 person 데이터를 학습
- 결과
          <p align="left">
          <img width="60%" height="60%" src="https://user-images.githubusercontent.com/19771164/148534237-e2444a17-4cc6-4003-b0ea-0a840ec4de69.png" alt="Sublime's custom image"/>
          </p>
<br>

### Time(정확성)
- 주차장의 사진이 어느 시점에 찍혔는지 알아야 사용자가 정확한 주차 가능 여부를 파악할 수 있음
- 사진 위에 detect 시점의 시간 정보를 추가
          - <p align="left">
          <img width="60%" height="60%" src="https://user-images.githubusercontent.com/19771164/148534298-58374ffa-2dda-4a22-8bd0-b949d9e7e55a.jpg" alt="Sublime's custom image"/>
          </p>

---
<br><br>
## 결과물

### 웹사이트 구조
- 실질적인 사용자 경험 개선을 위해서 우리가 찾은 주차 공간을 알리고자 웹사이트를 구현
          <p align="left">
          <img width="55%" height="55%" src="https://user-images.githubusercontent.com/19771164/148534847-c80c57de-382f-484c-b3cb-40e6443043b9.png" alt="Sublime's custom image"/>
          </p>
    
   
        
- 데이터 베이스 종류
    - SOCAR_ZONE
    : 쏘카존 이름, 쏘카존 위도, 쏘카존 경도, 주소, 현재 주차장 빈자리 수, 주차장 만차 수
    - Client
    : 이메일, 비밀번호, 이름
    - File
    : 쏘카존 이름, 주차장 사진
    
### 최종 결과물

[teamdi.xyz](http://teamdi.xyz/) <- 클릭

- 공식 id / 공식 비밀번호  
abcd@naver.com / 123
- Client 사용 방법
          <p align="center">
  <img width="100%" height="100%" src="https://user-images.githubusercontent.com/19771164/148516059-91da5206-12af-45cb-9737-20854d1df2bb.gif" alt="Sublime's custom image"/>
</p>
- 데이터 넣는 방법
