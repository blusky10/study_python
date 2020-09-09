# study_python

- https://github.com/blackdew/tensorflow1 
- https://www.youtube.com/playlist?list=PLl1irxoYh2wymOvcj_PKzAjx4empHQgF8

## t02

1. 과거의 데이터를 준비
2. 모델의 구조 만들기

    ```
    X = tf.keras.layers.Input(shape=[1])
    Y = tf.keras.layers.Dense(1)(X)
    model = tf.keras.models.Model(X, Y)
    model.compile(loss='mse')
    ```
    - shppe=[1] : 독립변수 개수
    - Dense(1) : 종속변수 개수
3. 데이터로 모델을 학습하기 (FIT)
    ```
    model.fit(독립, 종속, epoch=1000)
    ```
    - verbose=0 (로그 안찍히게 함)
4. 모델을 이용하기
    ```
    model.predict
    ```
    가중치 : model.get_weights()

## t03
- 퍼셉트론
- 가중치
- 편향

## t04
- 원핫인코딩 (onehot-encoding) : 범주형 변수를 변형하는 것.
- 활성화 함수 
    - 분류 : Softmax
    - 회귀 : Identity
- Sigmoid?
- loss
    - 분류 : crossentropy
    - 회귀 : mse

## t05
- 히든 레이어