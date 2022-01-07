![back](https://user-images.githubusercontent.com/19771164/148502115-a99d69d5-c5ae-4d3b-be4c-88e2a8014fe9.png)

# Team DI 주제

### “아니, 쏘카존에 반납하려니까 만석이라 다른 곳에 주차했더니 패널티라네요.”

![뉴스](https://user-images.githubusercontent.com/19771164/148502420-82ad41be-a154-4dd5-9c88-707636e15700.png)(http://www.newsworker.co.kr/news/articleView.html?idxno=113012)

: 쏘카는 전통적인 차량 렌트 시장과 다르게, 기술을 이용하여 뛰어난 사용자 경험을 제공한다. 차량을 빌리고 반납하는 전 과정이 digital transformation 되었으며, 기존의 대체재보다 월등한 **편리성**을 제공한다. 

하지만 이용 경험 중 차량 반납 단계에서, 예상치 못하게 주차공간이 없을 때 불편함을 겪는 사용자들이 존재해왔다. 이를 사용자가 문제에 직면하기 전 선제적으로 반응하기 위해, object detection을 이용한 **반납 장소의 실시간 주차 가능 여부**를 파악할 수 있는 서비스를 만들고자 하였다. 

### → “우리가 주차장의 상황을 알려주면 되지 않을까?”

### 주차장 상황 및 주차 가능 여부 정보 제공

---

## 주차장에서 어떤 요소들이 중요할까?

### **실내 주차장 / 실외 주차장**이 중요할 것이다.

실내 주차장과 실외 주차장의 상황은 다르다. 실내 주차장의 경우 카메라 높이, 카메라의 각도 등의 제약이 있을 수 있고, 실외 주차장의 경우 날씨의 변수, 빛의 양과 각도 등이 주차 공간을 찾는데 중요한 변수가 될 수 있을 것이라 가정했다.  

### 주차장의 종류와 관계없이 카메라 각도가 중요할 것이다.

비교적 단순한 차와 빈 공간을 구분하는데에는 카메라의 각도에 따라 차량이 어느 정도 보이는지, 카메라의 설정에 따라 얼마나 왜곡된 각도로 찍힌 사진인지, 이런 요소는 주차장과 상관없이 중요한 학습 요소로 작용할 것이라고 가정했다.  

### 주차장 자체가 중요할 것이다.

주차장마다 주차 할 수 있는 공간의 각도, 주차선의 선명도와 굵기와 같은 개별 요소들이 있고 지형지물의 상태가 모두 다르기 때문에 각 장소의 특성이 중요할 것이라 가정했다.  


---


## 실제 학습을 진행하면서 알아보자!

### 어떤 모델을 사용할까?

### [Yolo v5](https://github.com/ultralytics/yolov5)

: 현재 Object detection에서 뛰어난 성능을 보이고 있는 Yolo v5를 pretrained model로 활용하기로 했다. 그리고 각 중요하다고 생각하는 요소에 맞춰 detect하도록 fine tuning을 하자.  

![지단](https://user-images.githubusercontent.com/19771164/148505749-88dab2d1-7871-4ce5-b999-add485a4cbdb.png)  

### 어떤 데이터를 사용할까?

- 주차장의 이미지 데이터는 cctv 혹은 자동차의 블랙박스로 얻을 수 있을 것이라 판단했다.
- 하지만 쏘카 이용자가 주차장에 가기 전에 주차장에 관한 정보를 제공해주어야 하기 때문에, 블랙박스보다는 cctv 이미지가 더욱더 의미가 있을 것이라 판단했다.
- 문제는! 보안상 문제로 직접적으로 전달받을 수 있는 데이터셋이 없기 때문에, 스스로 찾아야 한다.→ 그래서 팀원 전체가 데이터 수집도 하고 라벨링 작업도 진행하기로 했다.
- Dataset
    - CNR park
    - pklot dataset
    - **[Microsoft COCO 2017 Dataset](https://public.roboflow.com/object-detection/microsoft-coco-subset)**
  
  ---

## 1차 시도(실외 vs 실내)

### 실내 주차장

- 전체 주차장의 실내, 실외 주차장 빈도를 보았을 때 실내 주차장이 높다.
    
    ![실내주차장1](https://user-images.githubusercontent.com/19771164/148506247-5fbe3a82-63df-4eb6-8ad6-01285529e4dd.jpg)
    
    ![실내주차장2](https://user-images.githubusercontent.com/19771164/148506256-470dfb1b-0229-4fe1-a433-0a4a8750f53c.jpg)
    
- 하지만 공개되어있는 실내 주차장 데이터셋을 찾을 수 없었다.
- 모델을 돌릴 수 있을 정도의 양과 질의 데이터셋을 찾을 수 없었다.
- 왜일까? 
→ 비교적 낮고 가까운 곳에서 사진을 찍을 수 밖에 없는 실내 주차장 구조 상, 해당 사진들을 사용할 경우 추후 개인 정보 (얼굴, 자동차 번호 등) 노출로 인한 문제제기가 가능하기에 실내 주차장 학습은 무리가 있다고 판단하였다.
- → 그래서 공개되어있는 실외 주차장 데이터셋을 최대한 활용하기로 결정했다.

### 실외 주차장

- [PKLot 데이터](https://public.roboflow.com/object-detection/pklot)
    
    : Federal University of Parana에서 공개한 오픈 데이터로 자유로운 활용이 가능하고, Yolo에서 필요한 labels의 자료가 있어 잘할 수 있을 것이라 판단했다. 
    
    ![pklot_data](https://user-images.githubusercontent.com/19771164/148506281-70aab702-af54-4465-b46f-bdd7454c616a.png)
    
    PKLot data
    
    ![PKLot Labels](https://user-images.githubusercontent.com/19771164/148506428-76749635-007b-4121-a856-f6811e697953.png)
    
    PKLot Labels
    
- 학습
    - train데이터(8,691장)
    valid데이터(2,483장)
    test데이터(1,243장)
    - 8,691장의 학습( epochs 20 / batches 32 )
        
        ![PKLot 학습 결과](https://user-images.githubusercontent.com/19771164/148506586-c030d896-fe6a-4b70-b385-e3ffe58e6c4a.png)
        
        PKLot 학습 결과
        
    - mAP 0.5 : 0.991
    mAP 0.95 : 0.867
- 결과
    - PKLot test데이터 결과
        
        ![PKLot test 데이터 결과](https://user-images.githubusercontent.com/19771164/148506719-c5d9d3f3-4175-47cc-b496-d6f5c8a52573.jpg)
        
        PKLot test 데이터 결과
        
        
        
        

      
        
        - 위에 사진은 PKLot 에서 학습한 사진이라 괜찮은 결과를 보이지만 아래 사진의 경우 우려했던 카메라의 각도라는 변수 때문에 detect에 한계가 보인다.

### 1차 시도의 결론 및 피드백

1. 실내 데이터는 개인정보의 문제로 인해 부족하기 때문에 실외 데이터로 진행하자. 
2. 라벨링에 대한 부분도 실제로 확인해보니 주차장의 정확한 범위(지나가는 차와 주차되어 있는 차를 정확히 구분)를 일관되게 설정하는 것이 중요함을 알게 되었다. 
3. PKLot 데이터가 train이 8000장이지만 4000장씩 2개의 카메라만 존재해서 생각보다 빠른 시간(5epoch에서)내에 overfitting에 도달했다. 그에 따라 다른 데이터에 확장성은 많지 않았다.
    
    ![PKLot 모델에 다른 test 데이터 결과](https://user-images.githubusercontent.com/19771164/148506977-39bdaf18-35e7-463a-b6ff-c59d9abb62fd.png)
    
    위 사진은 PKLot 학습과 비슷한 주차장, 아래 사진은 상이한 주차장
    
4. 카메라 각도가 비슷한 사진들은 80%까지 detect 하는 것을 보니 **카메라 각도**가 중요한 feature이지 않을까?  

---

## 2차 시도(카메라 각도에 따른 학습)

### 데이터셋

- CNR park
    - 총 9개의 카메라로 한 주차장의 이미지를 수집한 데이터이다.
    - 각 카메라는 다른 각도를 가지고 있기 때문에, 각 카메라 별로 따로 학습을 시켜주어 테스트해보자!
    - 예시
        
        ![cnr_data.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/480c1c28-26fc-4e72-bf26-ea2f6e5e0705/cnr_data.png)
        
- 데이터 라벨링
    - 1차 시도에서 사용한 PKLot 데이터 라벨링 방식을 바탕으로 일관된 라벨링을 진행하였다.
    - [LabelImg](https://github.com/tzutalin/labelImg)을 (PASCAL VOC format, Yolov5 format 등을 지원)을 이용하였다.
        - 총 약 1,300장의 이미지에 라벨링을 부여함
        - 라벨링 class는 총 두가지: ‘car’, ‘emtpy’
        - (새벽 4시까지 라벨링하고 올려주시는 팀원님들...)
            
            ![KakaoTalk_Snapshot_20220103_201009.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/27161659-965c-48f1-b2ab-6da289085faf/KakaoTalk_Snapshot_20220103_201009.png)
            
    - 예시)
        
        ![LabelImg 프로그램을 이용한 Yolov5 라벨링 예시](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a2e652fa-e98e-4552-9776-6c41e418cb00/라벨링.jpg)
        
        LabelImg 프로그램을 이용한 Yolov5 라벨링 예시
       
![1](https://user-images.githubusercontent.com/19771164/148508934-81b61491-210c-4c7b-9398-e1ce54868ea2.png)

