### Account 간단요약

* 앱을 새롭게 생성
* Article이 이미 존재하지만 계시글을 관리하는 역할을 하는 앱
* 회원관리 역할을 하는 기능이 필요한데 Account



### 회원 가입 기능 추가

* 회원 가능 == DB 유저 정보를 새롭게 추가 범위(create)
* UserCreateForm: django에서 기본적으로 제공해주는 폼
  * 유저 정보를 DB에  저장을 해야함 >>>  Modelform
  * `form django.contrib.auth.form import UserCreateForm`
  * 나머지 로직은 이전 crud의 create 동일
* 회원 가입을 하면 따로 로그인을 해야한다
  * 근데 우리는 이미 로그인 하는 방법을 알고 있다.
  * 회원 가입을 한다라는 것은 우리 사이트의 회원임이 인증 된 것이다.



### 로그인

* 로그인 ==> 세선을 새롭게 생성(create)

* 쿠키

  * 브라우저에 저장
  * 키-밸류 작은 데이터 파일
  * 만료일자가 존재
  * 쿠키종류
    * 세션 쿠키
      * 사용자가 사이트를 탐색할때 , 설정과 선호 사람을 저장하는 임시 쿠키
      * 브라우저를 닫으면 삭제
    * 지속 쿠키
      * 사용자가 주기적으로 방문하는 사이트에 대한 설정 정보나 로그인 이름을 유지하기 위해 주로 사용
      * 브라우저를 닫거나 재시작해도 남아있음

* 세션

  * 서버 DB 혹은 메모리
  * 정말 중요한 정보를 저장
  * 사용자가 많아지면 서버가 느려질 수 있음

* 로그인 -- 세션을 새롭게 생성(create)

* AuthenticationForm : django 에서 기본적으로 제공해주는 form

  * 로그인을 위해서 입력창을 제공
  * 로그인 유효성 검사
  * DB유저 정보와 비교해서 접속 인증해주는 친구
  * DB를 직접 수정하는 용이 아니기 떄문에 form
    * 첫번쨰 인자로 request 정보를 보내야 함.

* login 함수 : Django에서 기본적으로 제공해 주는 함수

  * 세션에 인증 정보를 생성해주는 함수

    

### 로그아웃

* 로그아웃 == 세션을 삭제(delete)
* logout 함수 : Django에서 기본적으로 제공해주는 함수
  * 현재 request에서 session에 관한 data를 삭제.

### 접근제한

* is_authenticated
  * User 클래스와 AnonymousUser의 속성값
    * User  해당 값이 항상 True, AnonymousUser는 항상 False
  * 유저가 인증된 유저인지 아닌지를 확인
* is_anonymous : 유저가 인증되지 않은 사용자인지 확인
* is_superuser: 유저가 최고 관리자인지 확인
* is_staff : 유저가 관리자 계정에 접긍 가능한지 확인 



* login__required 데코레이터

  * 로그인 된 유저만 해당 함수를 실행가능하게 하는 데코레이터
  * 만약 로그인이 되지 않은 유저라면
    * /account/login/ 으로 리다이렉트해줌
    * next라는 쿼리 문자열에 이전에 접근하려 했던  주소를  keep해줌
      * 킵된 주소를 사용하려면 request.GET.get('next')해서 리다이렉트
    * @login_required(login_url='/accounts/test/')
    * settings.py 에서 LOGIN_URL을 설정을 해주면 해당주소로 갈수 있

* login_required와 required_POST를 같이 사용할수 없는 이유

  ```python
  @require_POST
  @login_required
  def  글쓰기(request):
      #if ~~~~~
  ```

  * 비록인 상태로 POST로 글쓰기를 시도 했을때
    1. login_required에서 로그인 페이지로 리다이렉트 (POST 데이터 손실)
       * 리다이렉트는 GET
    2. 로그인을 완료 후에 NEXT를  이용해서  다시 글쓰기에 접근
       * 리다이렉트로 logout을 접근하게 됨
    3. 결국 403 http method 에러 발생



### 회원 탈퇴

* 회원 탈퇴 == >DB에서 유저 정보를 삭제

* 이전에 데이터 베이스로 정보를 삭제하는 방법

  ```python
  def delete(request,id):
      date = Article.objects.get(pk=id)
      data.delete()
      ....
  ```



* 유저 정보는 request.user 에 담겨져 있다.

  * request.user.delete()를 하면 유저정보가 삭제

  *  DB 정보를 삭제하는 것이기 때문에 POST요청

    

### 회원정보 수정

* 회원 정보를 Update
* `UsweChangeForm` : Django에서 기본적으로 제공해주는 폼
  * 
  * 문제점 
    * 일반 유거자 권한 설정을 할 수  있게 됨.
    * 그대로 사용하면 절대 안됨
* `CustomUserChangForm` : `UserChangeForm`을 상속받아서 커스텀함 폼.
  * 원하는 필드만 수정할 수 있게  해야함
  * 유저의 정보를 채워서 입력 창을 보여줘야 하므로 `instace` 설정을 해야함



* 디버깅 순서 
  * 개발 순서 (요청 -> url -> view -> template -> 응답)
  * 개발 순서의 역순으로  샹각하면서 오류 트래킹
    * 응답(오류메세지) -> template -> views -> url -> 요청(주소줄 확인 or 장고 log에 찍힌 요청을 확인. )



### 비밀번호 변경

* DB를 수정을 하는데 그런데 .. 말입니다..
  * 비밀번호는 텍스트 그래도 저장되면 안됨.
  * Django는 비밀번호를 그냥 저장하지 않고 암호화.
* PasswordChangeForm
  * Form을 상속 받아서 정의 되어 있음.
  * 첫번째 인자로 `request.user` 가 반드시 필요
* 비밀번호를 변경을 성공하게된다면 로그인이 풀려버린다.
  * 로그인 되면 유저 정보를 세션에 저장하는데
  * 비밀번호가 변경이 되면 유저 정보가 업데이트 되어서 세션에 저장된 유저정보와 데이터가 일치하지 않음
  * `update_session_auth_hash`  함수를 사용해서 세션의 유저 정보를 업데이트 시켜줘야함