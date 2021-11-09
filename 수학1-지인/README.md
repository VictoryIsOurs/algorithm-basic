# 수학1

1. 입력하는 법

   `inputs = list(map(int, input().split()))`

2. 시간 초과 방지하기 위해 사용하는 것

   ```python
   import sys
   input = sys.stdin.readline
   ```

3. 유클리드 호제법 : a를 b로 나논 나머지를 r이라고 했을 때, a와 b의 최대공약수는 b와 r의 최대공약수이다

   * 최대공약수

     ```python
     def gcd(a, b):
         return gcd(b, a % b) if b else a
     ```

   * 최소공배수

     ```python
     def lcm(a, b):
         return a * b // gcd(a, b)
     ```

     a = G * x, b = G * y -> x와 y는 서로소

     a * b = G * G * x * y

     최소공배수 = G * x * y = a * b // G

4. 에라토스테네스의 체 : 소수 구하는 방법

   ```python
   prime = [True] * 1001
   prime[0], prime[1] = False, False
   
   def find_prime():
       m = 1000 // 2
       for i in range(2, m+1):
           if prime[i] == True:
               for j in range(i+i, 1001, i):
                   prime[j] = False
   ```

5. 조합 사용하기

   ```python
   import itertools
   '''
   '''
   arr = 'ABCD'
   for a, b in itertools.combinations(arr, 2):
   	print(a, b) # 결과 : AB, AC, AD, BC, BD, CD
   ```

6. n진법으로 입력받기

   `int(input(), n)`

7. 10진수에서 2진수, 8진수, 16진수 변환

   ```python
   value = 50
   
   b = bin(value)
   o = oct(value)
   h = hex(value)
   ```

   

   

------

다시 풀어야 할 문제

- [ ] 2004

