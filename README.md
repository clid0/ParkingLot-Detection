- Team DI 주제

주차장에서 어떤 요소들이 중요할까?

- 카메라 각도
- 실내 / 실외
- 주차장
- 어떤 모델을 사용할까?
    - Yolo V5
- 1차 결과
    - Pklot 실패
        - 실내/ 실외 실패 ,라벨링의 실패 / 실내 데이터 실패  / 오버피팅 /
    - → 피드백 : 라벨링 직접 / 데이터 부족 인정
- 2차 결과(비슷한 각도)
    - 일부 성공(park.mp4)에서 실패 → 각도가 아닌 주차장이 답
    - → 피드백 : 지형지물의 중요성
- 3차 결과(주차장)
    - 2번,8번,9번 카메라
    - → 피드백 : 주차장이 답이다. 그러나 라벨링의 수작업이 필요함
- 4차 결과(detection들의 앙상블)
    - 10000장의 coco data set + 2,8,9카메라
- 확장성
    - 웹사이트(접근성)
    - person blur(개인정보보호)
- 결론
    - teamdi.xyz
    - 정리
- 데이터 셋
    - 데이터 라벨링

# Team DI 주제

### “아니, 쏘카존에 반납하려니까 만석이라 다른 곳에 주차했더니 패널티라네요.”

[쏘카, 차량 반납존 만석으로 임의 주차시 페널티 부과된다?..."고객센터를 통해 주차할 수 있도록 안내하고 있다"](http://www.newsworker.co.kr/news/articleView.html?idxno=113012)

: 쏘카는 전통적인 차량 렌트 시장과 다르게, 기술을 이용하여 뛰어난 사용자 경험을 제공한다. 차량을 빌리고 반납하는 전 과정이 digital transformation 되었으며, 기존의 대체재보다 월등한 편리성을 제공한다. 

하지만 이용 경험 중 차량 반납 단계에서, 예상치 못하게 주차공간이 없을 때 불편함을 겪는 사용자들이 존재해왔다. 이를 사용자가 문제에 직면하기 전 선제적으로 반응하기 위해, object detection을 이용한 반납 장소 실시간 주차 가능 여부 정보 제공 서비스를 만들자.

### → “우리가 주차장의 상황을 알려주면 되지 않을까?”

### 주차장 상황 및 주차 가능 여부 정보 제공

~~<teamdi.xyz>사진 1장~~

---

## 주차장에서 어떤 요소들이 중요할까?

### **실내 주차장 / 실외 주차장**이 중요할 것이다.

실내 주차장과 실외 주차장의 상황은 다를 것이다. 실내 주차장의 경우 카메라 높이, 카메라의 각도 등의 제약이 있을 수 있고, 실외 주차장의 경우 날씨의 변수, 빛의 양과 각도 등이 있을 수 있다.

### 카메라 각도가 중요할 것이다.

카메라의 각도에 따라서 사진이 모두 다른 것처럼 각도에 따라 학습을 다르게 할 수 있을 것이다.

### 주차장 자체가 중요할 것이다.

주차장마다 주차장 상황이 있고 지형지물의 상태가 모두 다르기 때문에 각 장소의 특성이 중요할 것이다.

---

## 실제 학습을 진행하면서 알아보자!-

## 어떤 모델을 사용할까?

### [Yolo v5](https://github.com/ultralytics/yolov5)

: 현재 Object detection에서 뛰어난 성능을 보이고 있는 Yolo v5를 pretrained model로 활용하기로 했다. 그리고 각 중요하다고 생각하는 요소에 맞춰 detect하도록 fine tuning을 하자.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/38b5787f-acf7-44b2-8808-a57834b9cd14/Untitled.png)

### 데이터는?-

- 주차장의 이미지 데이터는 cctv 혹은 자동차의 블랙박스로 얻을 수 있을 것
- 하지만 쏘카 이용자가 주차장에 가기 전에 주차장에 관한 정보를 제공해주어야 하기 때문에, 블랙박스보다는 cctv 이미지가 더욱더 의미가 있을 것!
- 문제는! 보안상 문제로 직접적으로 전달받을 수 있는 데이터셋이 없기 때문에, 스스로 찾아야 함! → 그래서 팀원 전체가 데이터 수집도 하고 라벨링 작업도 진행

## 1차 시도(실외 vs 실내)-

- 실내 주차장
    - 전체 주차장의 실내, 실외 주차장 빈도를 보았을 때 실내 주차장이 높다!
        
        ![실내주차장1.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6bdaf11f-2d61-489c-b0ec-45bd22d4398b/실내주차장1.jpg)
        
        ![실내주차장2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3ae95691-b339-4c15-99b5-394507d359ca/실내주차장2.jpg)
        
    - 하지만 공개되어있는 실내 주차장 데이터셋을 찾을 수 없었다.
    - 모델을 돌릴 수 있을 정도의 양과 질의 데이터셋을 찾을 수 없었다. 왜일까? 고민한 결과 → 사람 얼굴 등 개인정보의 문제가 있겠구나 판단
    - → 그래서 공개되어있는 실외 주차장 데이터셋을 최대한 활용하기로
- 실외 주차장
    - Federal University of Parana에서 공개한 [PKLot 데이터](https://public.roboflow.com/object-detection/pklot)로 학습 진행
        
        ![pklot1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/686eb20d-37f8-4c3b-a328-cfe7ba463a46/pklot1.png)
        
        - pktlot: 총 12,416의 실외 주차장 이미지 데이터셋으로 train, valid, test가 각각 8,691, 2,483, 1,243의 이미지로 구성됨
    - 학습
        - train데이터(8,691장)
        valid데이터(2,483장)
        test데이터(1,243장)
        - 8,691장의 학습( epochs 20 / batches 32 )
            
            ![PKLot 학습 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f561c051-972a-4ff8-8090-d0cbb8ea6fa6/pklot_results.png)
            
            PKLot 학습 결과
            
    - 결과
        - PKLot test데이터 결과
            
            [PKLot test 데이터 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6cb3f094-f6e2-4f69-aa39-89576891d80a/pklot_test.jfif)
            
            PKLot test 데이터 결과
            
        - 기타 데이터 결과
            
            ![PKLot 모델에 다른 test 데이터 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/71cc5fe1-8143-4b84-a98c-e7b423679166/pklot_test.png)
            
            PKLot 모델에 다른 test 데이터 결과
            
            - 위에 사진은 PKLot 에서 학습한 사진이라 괜찮은 결과를 보이지만 방향이 다른 상황에서는 detect에 한계가 보인다.

### 1차 시도의 결론 및 피드백-

1. 실내 데이터는 개인정보의 문제로 인해 부족하기 때문에 실외 데이터로 진행하자. 
2. 하지만 PKLot 학습 데이터가 8000장이 대부분 비슷한 사진들(2개의 카메라 밖에 없음)이고, 라벨링에 대한 부분도 실제로 확인해보니 아쉬운 부분이 있어 직접 라벨링을 하는 것이 좋을 거 같다.
3. 카메라 각도가 비슷한 사진들은 조금 detect 하는 것을 보니 카메라 각도가 중요한 feature이지 않을까?                                                                                                       

---

## 2차 시도(카메라 각도에 따른 학습-)

- 데이터셋
    - CNR park
        - 총 9개의 카메라로 한 주차장의 이미지를 수집함
        - 각 카메라는 다른 각도를 가지고 있기 때문에, 각 카메라 별로 따로 학습을 시켜주어 테스트해보자!
        - ~~CNR park 사진 2장~~
- 학습
    - 2번 카메라
        - 2015/11/13 - 2015/11/29 train데이터 (260장)
        2015/12/01 - 2015/12/05 valid데이터(43장)
        2016/01/14 - 2016/01/16 test데이터(43장)
        - 260장의 학습( epochs 50 / batch 30 )
        
        ![2번카메라_results.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/328e9b3d-61ab-4a55-808e-9c46f1359618/2번카메라_results.png)
        
    - 8번 카메라
        - 2015/11/13 - 2015/11/29 train데이터 (371장)
        2015/12/01 - 2015/12/05 valid데이터(38장)
        2016/01/14 - 2016/01/16 test데이터(40장)
        - 371장의 학습( epochs 50 / batch 30 )
        
        ![8번카메라_results.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/af9caf16-9294-4fd7-9801-e0e9c38064e3/8번카메라_results.png)
        
    - 9번 카메라
        - 2015/11/13 - 2015/11/29 train데이터 (407장)
        2015/12/01 - 2015/12/05 valid데이터(43장)
        2016/01/14 - 2016/01/16 test데이터(40장)
        - 407장의 학습( epochs 50 / batch 30 )
        
        ![9번카메라_results.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2ddd436b-4ef3-4515-8355-c22d65aae60d/9번카메라_results.png)
        
- 결과
    - 2번 카메라
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8fa1e823-bc40-4767-92d7-b7c43b5fdbf3/Untitled.png)
        
    - 8번 카메라
    - 9번 카메라
    - 8번 카메라 학습한 모델로 기타
        
        ![8번카메라로 park.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b578ebc1-9c68-4ab7-b780-d7693bd3880e/8번카메라로_park.png)
        

### 2차 시도의 결론 및 피드백

1. 여전히 다른 주차장에서 아쉬운 결과를 보이는데, 차와 빈 자리를 논리적으로 찾는 것이 아니라 라벨링 되어있는 그 부분의 지형지물을 학습하는 것으로 보인다. 차량의 방향도 중요하지만 그와 함께 있는 지형 지물이 중요함을 알 수 있다.
2. 날짜별 학습이 가능하다
5. 혹시 카메라 방향마다 학습한 이 모델들을 앙상블하면 더 좋은 모델을 만들 수 있지 않을까.

---

## 3차 시도

데이터가 부족한 상황이라고 할 때 우린 어떻게 대처할 수 있을까. 현실에서 카메라 각도나 

- rotation
- 데이터셋(test 200장)
    - parking net(100장)
        - ~~parking net 사진 2장~~
    - parking net(200장)
- 학습
    - ~~결과 표~~
- 결과
    - ~~테스트 결과 사진 good~~
    - ~~비슷한 주차장인 park.mp4 실패~~
- 결론 및 피드백
    - 데이터가 부족한 상황에서도 augmentation으로 어느 정도 극복할 수 있다.
    - 하지만 많은 데이터가 확실히 좋다.

---

## 4차 시도

서비스 형태가 되기 위해서 바로 투입이 가능한 형태의 모델이 필요하다.

- COCO 데이터 10,000장 학습한 모델
    - 결과
        - ~~park.mp4 의 결과~~
- coco + 2번, 8번, 9번 모든 모델
    - 결과
        - ~~park.mp4의 결과~~
- 결론
1. 
2. 한 class만 detect하는 상황이면 앙상블 효과가 좋다.
3. 각도 및 주차장의 지형지물이 비슷한 곳이라면 기존에 학습시킨 모델을 pre_trained모델로 사용해서

---

## 확장성

- 웹사이트
    - [teamdi.xyz](http://teamdi.xyz) url
        - 비공식 id / 비공식 비밀번호
        abcd@naver.com / 123
    - 
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/baa170b4-10ff-429c-b70a-0b880cfb221d/Untitled.png)
        
        - 아마존 EC2 서버가 작고 GPU성능이 많이 떨어지기 때문에 Google drive 와 DB가 connect
        - SOCAR ZONE정보와 주차장 사진을 서버와 DB가 connect
        - client는 정보에 접근만 가능
- person blur(개인정보보호)
    - 정보보호가 매우 중요한 상황
        - ~~정보보호 관련 기사~~
    - 학습
        - COCO data에서 사람만 10,000장 학습
    - 결과 + blur
        - ~~mirotic 사진~~
- Time(정확성)
    - 주차장의 정보가 어느 시점인지 client가 궁금
        - ~~시간이 찍힌 사진~~
        

---

## 결과물

- 웹사이트
    - [teamdi.xyz](http://teamdi.xyz) url
        - 비공식 id / 비공식 비밀번호
        abcd@naver.com / 123
- car & empty & person
    - ~~사진~~

---

## 예상 질문들

### Q. 몇 장의 데이터면 주차장을 학습할 수 있나요?

A. 현재 150장 사진을 라벨링 할 수 있으면 90% 이상의 정확도로 가능하다고 판단합니다.

~~150장 활용 / 200장 활용 / 350장 활용~~

### Q. 1,047개의 쏘카존을 어떻게 해결할 수 있나요?

A. 200장 기준 대략 3시간이 걸리는데 최저시급으로 (1047*3시간*최저시급) = 4,000만원 이라고 판단됩니다.

 하지만 앙상블 기법을 통해서 모델들의 앙상블을 통해 정확히 차의 개수만 파악할 수 있으면 정확한 주차장 라벨링을 굳이 하지 않아도, 주차장의 ‘주차 가능한 차량 개수’만 입력해도 계산할 수 있다고 판단됩니다.

---

# Modeling

## Objection Detection Model Selection

<aside>
💡 두 가지 모델의 혼용(모델 앙상블) = x + person detection

</aside>

### Camera2

- 2015/11/13 - 2015/11/29 train데이터 (260장)
2015/12/01 - 2015/12/05 valid데이터(43장)
2016/01/14 - 2016/01/16 test데이터(43장)
- 260장의 학습( epochs 50 / batch 30 )

![results.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4e7f8586-7b5b-4907-8959-042dcc1b99c9/results.png)

- Test data 결과(2016-01-15_0734.jpg)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8fa1e823-bc40-4767-92d7-b7c43b5fdbf3/Untitled.png)

- 왼쪽 위 모닝을 인식하지 못한 이유
    - 비오는 사진으로 noise가 많아서
    - train 데이터 2015/11/15에 비가 오는 사진이 있지만 
    당시에 차가 얼마 없어서 학습이 힘들었을 것
    

→ CNR park dataset with labelling on

→ 카메라별 학습

### Only car detection

→ open image v4 public dataset

→ yolov5를 이용한 fine-tuning

### Person detection

→ person image public dataset

→ yolov5를 이용한 fine-tuning

---

# Questions

## 확장 문제

### Q. 1047개의 쏘카존을 어떻게 해결할 수 있나?

→ 200장의 이미지를 라벨링하는데 소요된 시간 2~3시간

→ 최저시급 기준 총 4,000만원

→ 방향 1. 100장으로 train 이미지를 제한했을 때, 어느정도 accuracy level까지 올릴 수 있나?
→ 방향 2. only car detection model만 사용했을 때

### 방향 1. test accuracy > x 을 위해서 몇 장의 사진이 필요한가?

### 방향 2. car detection model의 정확성은?

---

# Abstract

쏘카는 전통적인 차량 렌트 시장과 다르게, 기술을 이용하여 뛰어난 사용자 경험을 제공한다. 차량을 빌리고 반납하는 전 과정이 digital transformation 되었으며, 기존의 대체재보다 월등한 편리성을 제공한다. 

하지만 이용 경험 중 차량 반납 단계에서, 예상치 못하게 주차공간이 없을 때 불편함을 겪는 사용자들이 존재해왔다. 이를 사용자가 문제에 직면하기 전 선제적으로 반응하기 위해, object detection을 이용한 반납 장소 실시간 주차 가능 여부 정보 제공 서비스를 만들었다.

데이터 수집에는 개인 정보 및 다른 보안 이슈로 인해 공공 데이터셋을 사용하였고, 모델에 맞게 핸드 라벨링을 진행하였다. object detection에 뛰어난 성능을 보이는 yolov5를 pretrained model로 선택해 각 학습에 맞게 fine-tuning을 진행하였고, 이미지 안에 의도와 다르게 포함될 수 있는 개인 정보 이슈를 막기 위해 person detect and blur 기술을 구현하였다.

학습 결과, 학습의 주요한 원인으로써는 각 카메라마다 학습을 진행해야한다는 가정을 증명할 수 있었다. 하나의 데이터셋에서 모델을 학습하게 되면, 실내, 실외, 카메라의 각도 등 여러 특징을 가지고 있는 이미지에서 높은 정확성을 구현할 수 없었다(pklot 실외 데이터셋 이용 학습 결과). 또한 다른 주차장, 비슷한 각도에서 얻은 데이터로 학습한 결과보다도 여러 카메라로 수집한 실외 주차장 데이터셋(cnr park)을 활용했을 때, 모든 데이터에 대해 학습한 결과보다 각 카메라에서 수집한 결과값이 월등이 좋은 성능을 보였다. 

이러한 결과를 토대로, 약 1,700개의 쏘카존에 도입할 수 있는 방안은 다음과 같다.

1. 학습의 결과물을 고려했을 때 각 쏘카존의 카메라마다 yolov5를 활용한다면 각 쏘카존에서 150장의 이미지가 있다면 x% 이상의 정확도로 주차 가능 여부를 예측할 수 있다. 즉 각 쏘카존에서 최소 150장의 이미지 수집과 라벨링 작업이 필요
    1. 현재 150장의 이미지를 이용한다면 x% 이상의 test accuracy를 가질 수 있었다.
    2. 추가적으로, 노이즈 추가기법, 이미지 전환 등을 사용한다면 100장(or 150장)의 이미지로 x%의 test accuracy를 가질 수 있었다.
2. car만 detect할 수 있는 모델을 활용하여 주차 가능 여부 제공
    1. car detection model만 활용할 경우, 다음과 같은 결과값을 얻을 수 있었다.

딥러닝을 이용한다면, 기존 센서를 활용한 기술보다 센서 구입 및 관리 등에서 비용을 아낄 수 있으며, 이미 쏘카존에 탑재되어있는 cctv를 이용하게 된다면, 효율적인 관리가 가능하다. 

---

# Data

## 수집

주차장의 이미지 데이터를 수집할 수 있는 대표적인 경로는 cctv와 쏘카 차량에 부착된 블랙박스이다. 하지만 풀고자 하는 문제를 고려해보았을 때 블랙박스 데이터는 실시간으로 주차장의 주차 가능 여부를 파악하지 못하기 때문에 cctv에서 수집할 수 있는 이미지 데이터를 얻는 것이 가장 결정적이다.

하지만 많은 쏘카존에서 접근 가능한 cctv 이미지는 한정적이다. 많은 쏘카존들이 속해있는 주차 건물은 쏘카가 아닌 다른 기업에서 운영되고 있으며, cctv가 녹화한 이미지에는 민감한 정보가 들어있을 수 있기 때문이다. 특히 사람이 나온 이미지가 강력한 예시가 될 수 있는데, 이를 고려하여 사람을 판별하여 blur할 수 있는 모델도 개발하였다.

프로젝트를 진행하며 쏘카 측에서 이런 직접적인 데이터들을 제공받을 수 없어, 공개 데이터셋들을 이용하였다. 공개 데이터셋들을 사용하는 모델과 호환될 수 있게, 학습을 원하는 객체를 대상으로 총 x개의 이미지에 대해 라벨링을 진행했다.

## 라벨링

### 라벨링 방법

Objection detection model에 사용할 pretrained model은 yolov5이다. yolov5는 아래와 같은 형식의 txt 파일의 라벨링을 가지고 있어, 이를 위해 ...를 이용하려 라벨링을 작업하였다. 총 x개의 이미지에 대해 person, car, empty space에 대해 building box를 만들었다. 총 작업 소요 시간은 ...이다.dr

# Dataset

- CNR park
- pklot dataset
- **[Microsoft COCO 2017 Dataset](https://public.roboflow.com/object-detection/microsoft-coco-subset)**
    
    → Person & Car 
    

# Dataset Labeling

- CNR park
- pklot Dataset
- **Microsoft COCO 2017 Dataset**
    - 11만장의 데이터를 모두 활용할 필요가 없기 때문에, 
    car & person이 있는 파일들만 정제해서 사용
    - car가 **Microsoft COCO 2017 Dataset에서** 18번 class인 것을 
    프로젝트에 맞게 학습시키기 위해 4번 class로 수정
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/560752a1-f314-4839-b5f6-36e33238b2c2/Untitled.png)
    
    - 결과적으로 car 12000장, person 10000장으로 축소

---
