## 파일 시그니처 Header signature(Hex) 
#### 파일의 처음에 존재하는 시그니처는 헤더(Header)시그니처, 파일의 마지막에 존재하는 시그니처는 푸터(Footer or Tailer)시그니처라고 한다. 


<u>JPEG</u> : <br >FF D8 FF E0 
      <br> FF D8 FF E8
 <br>JPEG의 경우 디지털 카메라로 캡쳐한 파일과 구분하기 위해 FF D8 FF E1의 시그니처를 갖는다.

<mark>GIF<mark/> : <br>47 49 46 38 37 61
      <br>47 49 46 38 39 61 

<mark>PNG<mark/> : <br>89 50 4E 47 0D 0A 1A 0A 

<mark>PDF<mark/> : <br>25 50 44 46 2D 31 2E 

<mark>ZIP<mark/> : <br>50 4B 03 04 

<mark>ALZ<mark/> : <br>41 4C 5A 01

<mark>RAR<mark/> : <br>52 61 72 21 1A 07


---
LFI(Local File Inclusion) 취약점 <br>
서버 내에있는 파일을 불러와 읽을수 있는 취약점<br>
/robots.txt는 로봇 배제표준이라고하며, 검색 엔진의 접근을제어하기 위한 일종의 규약 <br>

/flag.php<br>
/index.php<br>

SQLi : DB언어를 이용해 데이터를 불러오고, 또 저장하는데<br>
서버에서 DB로 전달하는 SQL문을 비인가자가 조작이 가능할 경우 취약점이 발생<br>

SQLI 취약점이 존재하는지 알아볼수있는지 가장 쉬운방법은<br>
입력창에 작은따옴표(')를 하나 적는다 <br>

SQL 구문 오류가 나는데 SELECT * FROM members WHERE username = '사용자 입력값'<br>
SQL 쿼리가 위처럼 최초 작성이 되었다. <br>
만약 NAME 칸에 HELLO라고 입력했다면<br>
SELECT * FROM members WHERE username = 'HELLO'<br>
이런식으로 DB로 전달이 된다 <br>
SELECT * FROM members WHERE username = '''<br>
이렇게 입력이 들어가게 되는데 문제가 발생한다<br>
작은 따옴표는 하나를 열었으면, 하나를 닫아줘야한다<br>
즉 작은 따옴표가 총개수가 홀수가 되면 안된다.<br>
위처럼 작은따옴표 개수가 홀수일경우 아직 닫히지 않은 작은따옴표가 생기기 떄문에<br>
에러 발생<br>

작은따옴표를 하나 입력했을때 저렇게 에러가 발생한다면<br>
SQLi 취약점이 있다 . <br>

' or 1=1-- - 라고 입력하게 되면<br>
SELECT * FROM members WHERE username= '' ore 1=1-- -' <br>
이런식으로 쿼리가 전달되는데 <br>
여기서 1=1 TRUE, TURE와 or 하면 그결과 역시 참이기 때문에<br>
WHERE(조건절)이 항상 참인 결과가 성립<br>
그리고 닫히지 않은 맨끝의 작은따옴표는 주석(-- -)을 입력해 줌으로써 없애버릴수있다.<br>

---
## SQL Injection 구문 <br>
<br>
# 1) WHERE 구문 우회<br>
 회원 ID를 입력하여 회원정보를 조회하는 웹 페이지 <br>
 1) 사용자가 ID가 1인 사용자 정보를 요청 <br>
 <br>2) 웹 애플리케이션이 내부의 데이터베이스로 SQL쿼리문 전송 </br> 
 > SELECT name, email FROM users WHERE ID= '1' <br>
   => WHERE 조건문이 있는 쿼리문 <br>
 3) 데이터베이스가 users라는 사용자 테이블에서 ID가 1인 사용자 정보를 반환 <br>
 4) 웹 어플리케이션을 통해 클라이언트까지 전달<br>
 <br>
 
 => SQL 쿼리문을 구성하는 소스코드는 다음과 같을 때 <br>
 $id=$_REQUEST['id'];<br>
 $qurey="SELECT name,emeail FROM users WHERE id = '$id';"; <br>
 




## 
