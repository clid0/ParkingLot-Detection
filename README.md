# TeamDI2
# Team DI가 주목한 문제

### 주제: 주차 반납

### 배경: 쏘카 이용 경험 funnel 중 주차 반납에서의 pain point

### 목표: pain point 해결을 위해 주차 가능 여부 정보 제공

# 데이터 수집

## 수집

### CCTV vs. blackbox

### CCTV 데이터 acquisition → blur.py

## 라벨링

### 라벨링 방법

# Modeling

## 주차장 데이터에서 가장 중요한 요소는? 중요한 feature 찾기

### 가정들

## Objection Detection Model Selection

### 두 가지 모델의 혼용 = x + person detection

### Car and empty space detection

### Only car detection

### Person detection

# Questions

## 확장성 문제

### Q. 1704개의 쏘카존을 어떻게 커버할 수 있나?

→ 최저시급 기준 총 4,000만원

→ 방향 1. 100장으로 train 이미지를 제한했을 때, 어느정도 accuracy level까지 올릴 수 있나?
→ 방향 2. only car detection model만 사용했을 때,

### 방향 1. test accuracy > x 을 위해서 몇 장의 사진이 필요한가?

### 방향 2. car detection model의 정확성은?
