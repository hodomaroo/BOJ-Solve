# [Gold IV] 무한 수열 2 - 1354 

[문제 링크](https://www.acmicpc.net/problem/1354) 

### 성능 요약

메모리: 629568 KB, 시간: 4568 ms

### 분류

자료 구조(data_structures), 다이나믹 프로그래밍(dp), 해시를 사용한 집합과 맵(hash_set), 트리를 사용한 집합과 맵(tree_set)

### 문제 설명

<p>무한 수열 A는 다음과 같다.</p>

<ul>
	<li>A<sub>i</sub> = 1 (i ≤ 0)</li>
	<li>A<sub>i</sub> = A<sub>⌊i/P⌋-X</sub> + A<sub>⌊i/Q⌋-Y</sub> (i ≥ 1)</li>
</ul>

<p>N, P, Q, X, Y가 주어질 때, A<sub>N</sub>을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 5개의 정수 N, P, Q, X, Y가 주어진다.</p>

### 출력 

 <p>첫째 줄에 A<sub>N</sub>을 출력한다.</p>

