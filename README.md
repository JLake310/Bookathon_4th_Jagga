# 2023 SKKU AI x Bookathon 4th

## 00. Introduction
<img width="917" alt="image" src="https://user-images.githubusercontent.com/82494506/213676966-0f24a37e-dae6-443e-8209-d5cb9adb38c9.png">
성균관대학교에서 주최한 본 대회는 인공지능 모델을 활용하여, 주어진 키워드를 주제로 수필을 작성하는 것을 목적으로 하였습니다.
</br>
</br>

수필의 키워드는 ```담대한(Daring)```이었으며, </br>
```소신(小身)의 소신(所信) : 두렵지만, 소신있고, 담대하게```라는 제목의 **13,539**자 분량의 수필을 생성했습니다.
</br>
### 🏆 4th of 15 teams

그 결과, 장려상이라는 좋은 결과를 낼 수 있었습니다.

* [소신(小身)의 소신(所信)](https://github.com/JLake310/Bookathon_4th_Jagga/blob/main/result_essay/%EC%86%8C%EC%8B%A0(%E5%B0%8F%E8%BA%AB)%EC%9D%98%20%EC%86%8C%EC%8B%A0(%E6%89%80%E4%BF%A1).md) 보러가기
* [발표자료](https://github.com/JLake310/Bookathon_4th_Jagga/blob/main/presentation/%EC%9E%91%EA%B0%80%EB%8B%98%EB%A7%88%EA%B0%90%EC%96%B8%EC%A0%9C%EB%8F%BC%EC%9A%94_%EB%B0%9C%ED%91%9C.pdf) 보러가기

## 01. 데이터 수집
> 독후감 데이터(기본 제공)
2000-2022 신춘문예 수상작  
남산백일장 수상작  
글틴 수필  
Brunch 수필  
책사랑 주부수필 수상작  
한국산문 작가협회 수필 공모전  
보령_의사수필 수상작  
동서식품 수필 수상작  
수필.net  
추천수필  
신현식의 수필세상  
문학광장  
다르마칼리지  
성균색

총 15 종류, **13,829**개의 데이터를 수집하였습니다.
(사용 데이터는 저작권 관련 문제로 깃허브에 공개하지 않겠습니다.)

## 02. 데이터 전처리
1. 중복, 결측 데이터 제거
2. 데이터 정규화 
3. 맞춤법 검사
4. 구어체 제거 및 종결어미 통일
5. 혐오, 차별, 정치 등 관련 데이터 제거

* ```KLUE : Korean Language Understanding Evaluation``` 에서 사용한 전처리 기법 사용  
* 인간 전처리기(?) 사용


## 03. 주제 선정
### 다산 정약용의 철학
> ### “아침에 햇살을 받는 곳이 저녁에 먼저 그늘지고, 일찍 꽃 피면, 지는 것도 빠르다.”  


📌 정약용 선생님의 철학은 절망을 맞닥뜨려도, 좌절하지 않고, 받아들이는 법에 대하여 이야기합니다. 따라서 우리가 전하고자 하는 교훈은 ```"소란한 세상에서 담대하게 자신을 잃지 않는 법"```입니다.

<img width="727" alt="image" src="https://user-images.githubusercontent.com/82494506/213694113-0995731a-814f-47a9-8166-cd499ce0d1bf.png">

## 04. 데이터 선정
### JSearch : 문장 색인과 토큰 역색인을 활용한 자체 제작 데이터셋 구성 툴 
```
자체 제작 툴인 JSearch를 활용해 각 소주제 별 선정한 Query를 논리 연산자를 활용하여  
Filtered data를 구성했습니다.
```

<img width="800" alt="image" src="https://user-images.githubusercontent.com/80453200/215392872-f2ea9642-c5fd-4d5b-9550-184d1a6919ee.png">

<img width="800" alt="image" src="https://user-images.githubusercontent.com/80453200/215394162-8b74e7af-ddb5-4e0d-a409-2b933cef556d.png">


## 05. 모델 학습
### 사용 모델 : SKT/kogpt2-base-v2
📌 모델 선정 기준
* **수식어구**가 자연스러운가?
* 앞 뒤 **문맥**과 문장의 **흐름**이 자연스러운가?
* **반복**되는 문장은 없는가?  
   
   
대회에서 제공해준 GPT2와 SKT-KoGPT2를 같은 환경에서 1 epoch을 학습시켜보았을 때,  
GPT2보다 **SKT-KoGPT2**가 저희가 선정한 모델 선정 기준에 부합했습니다.

✔ **Fine-tuning**   
```
사전에 수집한 데이터들로 1차적으로 학습된 모델을 브런치 사이트에서   
주제와 관련된 공통 키워드로 뽑아낸 데이터들로 2차 fine-tuning을 진행했습니다.  
```
![fine](https://user-images.githubusercontent.com/80453200/213722200-b9acf3c1-15b7-4291-9358-83425b45ad21.PNG) 


✔ **Transfer Learning**      
```
각 소주제 별로 키워드를 뽑아 Filtered Dataset 4개를 만들었습니다.  
그 후 Common Keyword로 학습된 모델을 각각의 주제 별로 transfer learning을 진행했습니다.   
결과적으로 4개의 소주제 모델을 형성했습니다.
```
![transfer](https://user-images.githubusercontent.com/80453200/213724930-3da456ef-799c-467c-9be7-2036ec9ede58.PNG)  
## 06. 수필 생성

### 샘플링 방식
✔ **Top-p 샘플링 사용**   
```
Top-p 와 Top-k 샘플링 방식을 비교했을 때, Top-p의 샘플링 방식의 성능이 더 좋았습니다.
따라서, Top-p 샘플링 방식을 사용했습니다.
```
  
✔ **jiN-best 샘플링 사용**    
```
TF-IDF와 Pororo Similarity를 활용한 자체 제작 샘플링 툴입니다.
```
<img width="800" alt="image" src="https://user-images.githubusercontent.com/80453200/215406197-a5d63c44-f336-45bd-be06-1ef221c00a3e.png">

✔ **인간 샘플링 사용**    
```
마지막은 저희 팀원들이 직접 읽어보며 샘플링을 진행했습니다. 인간의 개입을 최소화하기 위해 가장 마지막에 검토 느낌으로 활용했습니다.  
문장의 내용을 일절 수정하지 않았으며 필요없는 문장과 문맥을 잃어버리는 경우에만 문장을 삭제했습니다.
```

#### 📌 샘플링 전체 구조
<img width="800" align="center" alt="image" src="https://user-images.githubusercontent.com/80453200/215407301-98b9f8ae-d2e7-4113-aa70-c11bb263f9d6.png">

다음은 저희 모델이 생성한 가장 ```담대한``` 문장입니다.

<div align="center">
  <b>"그렇게 되면 나만의 인생관이 정립되고, 그것이 나를 위한 길이 되고, <br>
     나아가 진정한 사람이 되는 길을 만들어 나갈 수도 있을거라 생각한다."</b>
</div>



## 07. 팀원 소개

### 2023 SKKU AI x Bookathon 4th, 작가님마감언제돼요

|                      김재연                       |                엄계현                |                이예진               |
| :---------------------------------------------: | :----------------------------------: | :------------------------------: |
|<img src="https://avatars.githubusercontent.com/u/86578246?v=4" alt="JLake310" width="100" height="100">|<img src="https://avatars.githubusercontent.com/u/80453200?v=4" alt="KaeHyun" width="100" height="100">|<img src="https://avatars.githubusercontent.com/u/82494506?v=4" alt="leeyejin1231" width="100" height="100">| [JLake310](https://github.com/JLake310) | [KaeHyun](http://github.com/KaeHyun) | [leeyejin1231](http://github.com/leeyejin1231) |


## _작성중 !!!_

