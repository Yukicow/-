







Expression Language


EL이란 표현식이나 액션 태그를 대신해서 값을 표현해 주는 언어이다.


EL은 ${}을 말한다. <%= %>과 같다.

JSP 스크립트의 표현식을 대신하여 속성 값을 쉽게 출력하도록 고안된 언어라고 할 수 있다.

속성값을 표현하는 것에서는 표현식 보다 간략하고

EL이 제공하는 내장객체가 존재하기 때문에 인자나 특정 속성 값들을 바로 불러와 출력할 수 있다.

EL은 java언어가 아니고 jsp문법이기 때문에 그냥 출력 방법만 조금 편해지는 것 뿐이다.

그리고 EL태그는 <%= %>와 비슷하기 때문에 함수를 호출해서 사용할 수도 있는데 이 때는 정적(static) 메소드만 사용 가능하다.

ex) Math.ceil() Integer.parsInt() 등

 
EL -> ${}의 내부에는 연산자 사용이 가능한데

일반적인 언어의 연산과 똑같다. 하지만 조금 차이점이 있다면 연산자를 알파벳을 이용하기도 한다.

<(크다) 는 gt로 대체 가능하고 >는 lt <=는 ge >=는 le로 사용할 수 있다.

이 알파벳은 영어 단어의 약자이다. gt = greater than, lt = less than, ge = greater or equal (이건 맞는 지 모르겠음)

위의 것들 말고도 and,or,eq,ng,empty,div,mod 가 있다.

empty는 그 값이 null이거나 빈 문자열이면 true를 반환하는 연산이다.


이렇게 연산자 말고 알파벳 연산을 가능하게 한 이유는 특정 연산자를 사용할 수 없는 엄격한 환경이 있을 수 있는데

그럴 때 사용할 수 있는 연산자를 둔 것이다. 연산자를 보면 '<' 이런 식으로 태그와 겹치는 문자같은 걸 사용해서

문제가 될 수 있는 환경도 존재하기 때문에 연산자를 사용하지 못 하게 하는 환경이 있다는 것이다.


조건 연산은 a? b:c 로 사용한다.

또 EL에는 empty 연산자도 있다. 객체에 value가 있는 지를 판단한다.

test = " empty 객체" 하면 객체가 null일 경우 true를 반환한다. 



EL은 액션 태그로도 사용된다.

예를 들어 <jsp:getProperty name = "member" property = "name"/>태그를 EL로 간략화 하면

${member.name}이 된다. # '.'이 아닌 []으로 표현이 가능하다 -> ${member[name]} 

액션 태그로 표현하면 길게 표현해야 하지만 EL을 이용하면 더 간략화가 가능하다.



EL의 내장객체

EL은 내장객체를 갖고 있기 때문에 

우리가 태그를 이용하거나 java언어를 통해 특정 값을 출력할 때 

힘들게 하나하나 값을 불러오고 저장하여 출력할 필요 없이 바로 출력이 가능하다.



밑은 각 내장객체의 이름과 사용법에 대한 내용이다.

객체 = name 속성 값이라고 생각하고 보면 편하다.


pageContext

JSP내장 객체 pageContext와 같다.


pageScope

pageContext에 등록된 데이터의 이름과 값을 저장하고 있는 map객체

${pageScope.객체명}


requestScope

httpServletrequest에 등록된 데이터의 이름과 값을 저장하고 있는 map객체

${requestScope.객체명}


applicationScope

ServletContext에 등록된 데이터의 이름과 값을 저장하고 있는 map객체

${applicationScope.객체명}


sessionScope

session 보관소의 값 조회

${sessionScope.객체명}


위의 스코프들은 EL 태그를 사용할 때 중요하다.

page,request,application,session은 우선순위라는 게 있어서

만약 Controller에 의해 생성된 모델 데이터를 EL로 가져올 때

일반적으로 내장객체에 저장된 데이터를 불러오는 형태 ( 예시 :  ${result} )로 사용하면 

서로 다른 내장객체에 같은 이름의 attribute가 있을 경우 우선 순위에 의해 출력된다는 것이다.

이 우선순위는 page -> request -> session -> application 순이다.


예를 들어

page객체에 Controller에서 setAttribute("result", 10)을 저장하고 

request객체에 setAttribute("result", 5) 을 저장했다고 해 보자.

여기서 jsp의 EL태그로 ${result}를 사용하면 page객체에 저장된 10이 출력된다.

이런 것을 막기 위해서 위처럼 스코프를 통해 사용할 수 있다.

EL 내장객체는 각 스코프 영역에 있는 데이터만을 갖기 때문에 출력하기 때문에 겹치지 않고 사용이 가능하다.

그냥 내장객체의 getAttribute를 사용한다고 생각하면 편한데 사용은 훨씬 간편하다.



param

HTTP 의 파라미터들로 요청 파라미터 를 읽어올 때 사용

${param.매개변수명}


paramValues

같은 이름으로 전달된 질의 문자열의 이름과 값들을 저장하고 있는 map 객체

${paramValues.매개변수명}


header

요청정보 헤더의 정보를 이르과 값으로 저장하고 있는 map 객체

${header.헤더명}


headerValues

요청정보 헤더의 정보들을 이름과 값들을 저장하고 있는 map객체

${headerValues.헤더명}


cookie

<쿠키이름, cookie> 매핑을 저장한 map 객체

${cookie.쿠키명}


initParam

컨텍스트 초기화 매개변수의 값 조회

${initParam.매개변수명}