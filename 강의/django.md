### django

#### 프로젝트 만들기

`django-admin startproject first_projeect(프로젝트이름)`

사용하면 안되는 프로젝트 이름 

* 하이픈 
* python, djngo 에서 쓰는 기본적인 이름
* 가장 밖에 있는 프로젝트 폴더명은 수정 가능하나 ,setting 파일이 들어있는 폴더명은 걸드리지 말자

#### 서버 켜기

`python manage.py runserver`

#### 서버 끄기

ctrl + c

#### app 만들고 app을 등록하기

`python manage.py startapp articles(앱이름)`

**바로 setting app을 등록해주기!!! **

install_apps 제일 위에 등록

* 앱이름은 복수형으로 만들어 줄 것

* 장고 프로젝트는 app의 집합체로 동작
  * 하나의 프로제게트는 여러 개의 어플리 케이션을 가질 수 있음
    * 어플리케이션 : 하나의 역할 및 기능 단위로 쪼개진 형태
    * 회원관리/ 글작성,  수정, 글 삭제 / 데이터를 수집분석 /...
    * 작은 프로젝트라면 어플리케이션을 따로 나누지 않아도 된다.

* settings 에서의 app 순서

  1. local apps

  2. 3rd party apps

  3. django apps



#### 한글버전 

`LANGUAGE_CODE = 'ko-kr'` 소문사로사용

time_zone = 'Asia/seoul' 앞에만 대문자



####  3 대장 : 가장많이 건드려야할 파일

1. urls.py

2. views.py

3. template (.html)

   error가 나온상황이면 오타를 확인할것!!! (폴더오타)

* urls.py  에서 해야할 일

  **path('url패턴/', 실행이 되어야 하는 views에 있는함수,해당 path의 별명)**

  * 많이 놓치는 부분 : url 패던 뒤에 슬러쉬!!!

  * url의 변수화 :  value rounting

* views.py 에서 해야할일
  * 함수를 정의(첫번째 인자로 request 필수!! )
  * **return**은 꼭 필요
    * render : 주로 template과 함께 response 할 때 사용되는 함수

* template 에서 해야할일
  
  * 폴더 명은 반드시 templates 인것을 확인

#### MTV(MVC 패턴)

model : 장고에서는 model

view : template

controller : view



#### Django template language (DTL)

* django temlpate system 에서 사용하는 bullit-in template system
* 조건, 반복, 치환, 필터, 변수 등의 기능을 제공.
* 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것
* 파이썬 처럼 if,for을 사용할 수 있지만 이거는 단순히 python code 실행되는 것이 아님.



##### syntax

* variable : {{}}
* filter : {{ variable | filter}}
* tags : {% tag %} 



----------------------



## 템플릿 시스템 설계 철학

* 장고는 템플릿 시스템이 표현을 제어하는 도구이자 표현에 관련된 로직일뿐이라고 생각한다.
* 템플릿 시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안된다.



______________________________



### 여기서 부터는 본격 장고 동작 정의 방법

* Template Variable

  * html과 같은 template에서 views.py에서 준비한 변수를 가져다가 쓰는 방법

  * render() 세번째 인자로 `{'key': value}`와 같이 딕셔너리 형태로 넘겨주면 Template에서 key를 이용하여 value를 가져 올 수 있다.

    ```python
    context = {'key' : value}
    return render(request,'index.html',context)
    ```

    ```python
    {{ key }} 이렇게 value를 보여줄 수 있다.
    ```

* Variable Routing(동적 라우팅)

  * url 주소 일부를 변수처럼 사용해서 동적인 주소를 만드는 것.

  * 주소 요청 : `http://127.0.0.1:8000/hello/문자열`

    urls.py

    ```
    path('hello/str(타입):name(저장되는 변수명)/', views.hello)
    ```

    views.py

    ````python
    def hello(request, name(저장되는 변수명)):
        print(name)
        context = {
            'name' = name,
        }
        return render(request,'hello.html', context)
    
    ````

    template(hello.html)

    ```html
    <body>
        이름은 : {{ name }} # context의 key 값을 사용하면 value를 출력한다.
    </body>
    ```

* DTL (tag와 filter)

  * 로직을 표현 할때는 : {% for %}

  * 값을 표현 할 때는 : {{ }}

  * 주석으로 나타내고 싶을 때는 : {# #} or {% comment %} 주석할내용 {% comment %} 

    ```
    <!-- <h1>{#{i * 2}#}</h1> -->
    {% comment %} <h1>{i * 2}</h1> {% comment %
    ```

  * for 태그 

    * 반복을 위한 태그

      ```
      {% for 임시변수 in interable 한 객체 %}
      {% endfor %}
      ```

    * for empty

      ```
      {% for 임시변수 in interable 한 객체 %}
      	값이 하나라도 있으면 여기가 실행
      {% empty %}
      	출력할 값이 없으면 출력.
      {% endfor %}
      ```

  * if 태그

    * 조건을 구분하기 위한 태그

      ```
      {% if 조건문 %}
      {% elif 조건문 %}
      {% else %}
      {% endif %}
      ```

  * 나머지 기타 유용안 dtl 문서를 참고,