# D1_1545 거꾸로 출력해 보아요

```python
num = int(input())
for i in range(num, -1, -1):
    print(i, end=' ')
```



# D1_2019 더블더블

```python
num = int(input())
cnt = 1
for i in range(1, num+1):
    print(cnt, end=' ')
    cnt *= 2
print(cnt)
```



# D1_1936 1대1 가위바위보

```python
rsp_num = input()
a_win = ['3 2', '2 1', '1 3']
b_win = ['2 3', '1 2', '3 1']
if rsp_num in  a_win:
    print('A')
elif rsp_num in b_win:
    print('B')
```



# D1_1933  간단한 N의 약수

```python
num = int(input())
for i in range(1, num+1):
    if not num % i:
        print(i, end=' ')
```



# D1_1938 아주 간단한 계산기

```python
two_num = input()
two_num = two_num.split(' ')
for i in range(len(two_num)):
    two_num[i] = int(two_num[i])
print(two_num[0] + two_num[1])
print(two_num[0] - two_num[1])
print(two_num[0] * two_num[1])
print(two_num[0] // two_num[1])
```



# D1_2025 N줄 덧셈

```python
num = int(input())
total = 0
for i in range(1, num+1):
    total += i
print(total)
```



# D1_2027 대각선 출력하기

```python
for i in range(5):
    for j in range(5):
        if i != j:
            print('+',end='')
        else:
            print('#',end='')
    print('')
```



# D1_2029 몫과 나머지 출력하기

```python
cnt_num = int(input())
num_list = []
for i in range(cnt_num):
    num_list += [input()]
for i in range(len(num_list)):
    num_list[i] = num_list[i].split(' ')
    for j in range(len(num_list[i])):
        num_list[i][j] = int(num_list[i][j])

for i in range(cnt_num):
    print(f'#{i+1}', num_list[i][0] // num_list[i][1], num_list[i][0] % num_list[i][1])
```



# D1_2043 서랍의 비밀번호

```python
check_num = input()
check_num = check_num.split(' ')
for i in range(len(check_num)):
    check_num[i] = int(check_num[i])
print(check_num[0] - check_num[1] + 1)
```



# D1_2046 스탬프 찍기

```python
num = int(input())
for i in range(num):
    print('#',end='')
```



# D1_2047 신문 헤드라인

```python
news_headline = input()

print(news_headline.upper())
```



# D1_2050 알파벳을 숫자로 변환

```python
alpha_str = input()
for word in alpha_str:
    print(ord(word)-64,end=' ')
```



# D1_2056 연월일 달력

```python

```



# D1_2058 자릿수 더하기

```python
num_str = input()
num = []
total = 0
for i in num_str:
    num += [int(i)]
    
for i in range(len(num)):
    total += num[i]

print(total)
```



# D1_2063 중간값 찾기

```python
cnt = int(input())
num = list(map(int, input().split()))
for i in range(len(num)):
    for j in range(1,len(num) - i):
        if num[j-1] > num[j]:
            num[j-1], num[j] = num[j], num[j-1]

print(num[cnt // 2])
```



# D1_2068 최대수 구하기

```python
cnt = int(input())
num = []
for i in range(cnt):
    num += [input()]
for i in range(len(num)):
    num[i] = num[i].split(' ')
    for j in range(len(num[i])):
        num[i][j] = int(num[i][j])
for i in range(len(num)):
    max_num = 0
    for j in range(1, len(num[i])):
        if num[i][j] > max_num:
            max_num = num[i][j]
    print(f'#{i+1}', max_num)
```



# D1_2070 큰 놈, 작은 놈

```python
cnt = int(input())
num_list = []
for i in range(cnt):
    num_list += [input()]
for i in range(len(num_list)):
    num_list[i] = num_list[i].split(' ')
    for j in range(len(num_list[i])):
        num_list[i][j] = int(num_list[i][j])
    if num_list[i][0] > num_list[i][1]:
        print(f'#{i+1} >')
    elif num_list[i][0] < num_list[i][1]:
        print(f'#{i+1} <')
    else:
        print(f'#{i+1} =')
```


# D1_2071 평균값 구하기

```python
cnt = int(input())
num_list = []
for i in range(cnt):
    total = 0
    num_list += [input()]
    num_list[i] = num_list[i].split(' ')
    for j in range(len(num_list[i])):
        num_list[i][j] = int(num_list[i][j])
        total += num_list[i][j]
    print(f'#{i+1} {round((total/len(num_list[i])))}')
```



# D1_2072 홀수만 더하기

```python
cnt = int(input())
num_list = []
for i in range(cnt):
    total = 0
    num_list += [input()]
    num_list[i] = num_list[i].split(' ')
    for j in range(len(num_list[i])):
        num_list[i][j] = int(num_list[i][j])
        if num_list[i][j] % 2:
            total += num_list[i][j]
    print(f'#{i+1} {total}')
```

