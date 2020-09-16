유저 생성

유저 로그인



______________



CRUD의 연장선

* 장고에서 만들어둔 USER 모델을 사용
* 장고에서 만들어둔 FORM을 사용
* 그래서 외울게 좀 있다 (import)
  * 기억이 나지 않으면 dj doc 찾아보자



______________



오늘 라이브에서 가장 처음 했던것

* account 라는 앱을 생성.

  * 동일하게 urls 분리
  * models.py 는  장고에서 제공하는 USER를 사용하기 떄문에 따로 정의는 하지 않음
  * form 도 장고에서 제공하는 form을 사용하기 때문에 따로 정의 하지는 않음
    * but, 곧 custom을 해야함.

* 회원가입

  * Athentication(인증) : 신원 확인, 유저가 나는 이러한 사람이다 라고 신원을 확인. 

  * Authoriztion(권한,허가) : 권한을 부여

    

  * 회원 가입 -> 새로운 유저를 받겠다 => 유저 정보를 받아서 DB에 생성(create)

    * UserCreationForm : 장고 제공 폼.

      * 입력 받은 USER정보를 최종적으로 DB에 저장.
      * ModelForm

      ```python
      from django.contrib.auth.forms import UserCreationFrom
      
      def signup(request):
          if request.method == "POST":
              form = UserCreationForm()
              if form.is_valid():
                  form.save()
                  return redirect('account:index')
          else:
         		form = UserCreationForm()
          context ={
              'form' : form
          }
          return render(request,'account/signup.html',context)
      ```

* 로그인

  * **쿠키**

    * 브라우저에 저장이 되는 내용
    * 키 = 밸류의 작은 데이터 파일
    * 만료날짜, 경로정보 (자주 접속한다면 만료날짜가 계속 갱신)
    * 쿠키가 세션보다 속도가 빠름
    * 보안은 세션이 더 좋음 , 쿠키는 브라우저 저장이 되기 때문에 타인이 볼 수 있음
    * 종류
      * 세션쿠키
        * 쇼핑몰 장바구니
        * 브라우저를 닫으면 삭제됨.
      * 지속 쿠키
        * 24시간 동안 닫기, 로그인 이름 유지
        * 로컬에 저장이 되서 컴퓨터를 재시작해도 남아 있음.

  * **세션**

    * 서버의 DB. 메모리
    * 특정 사용자의 중요한 정보
    * 사용자가 많아지면 서버메모리를 많이 쓰게되서 정말 중요한 정보만 저장

  * 세션에 담긴 유저 정보가 특정 브라우저를 사용하는 유저가 맞는지 확인하기 위해서

    세션 키(id)를 쿠키에 전달을 해줌.

  * 브라우저에서 쿠키를 삭제 한다면?

    * 서버는 해당 브라우저의 유저가 누구인지 확인 할 수 없게됨.
    * 새롭게 로그인을 해서 새로운 세션키를 발급받아야 함, 쿠키 새롭게 생성됨

    

    

    

  * AuthenticationForm

    * 장고에서 제공해주는 폼
    * 로그인에 필요한 정보를 받아서 유효성 검사 폼
    * 따로 ED에 저장하는 것이아니여서 Form
    * 첫번쨰 인자로 request 확인

  * 실직적으로 로그인을 하는 함수는 장고에서 제공해주는 login함수

    * 회원임을 확인 되면 세션을 생성.

    ```python
    #view.py
    from django.contrib.auth.forms import AuthenticationForm
    from django.contrib.auth import as auth_login
    
    def login(request):
        if request.method =="POST":
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
                login(request,form.get_user()) #장고에서 제공해주는 함수
                return redirect('articles:index')
        else:
            form = AuthenticationForm()
        context = {
    		'form' : form,
        }
        return render(request, 'accounts/login.html', context)
    ```


____



* 접근 제한

  * request에 로그인 정보가 들어있음.

  * request.user

    * is_authenitcated : 로그인 여부
    * is_superuser : 관리자 인지 아닌지 여부
    * is_anonymous : 로그아웃 여부

  * 데코레이터

    * login_required (함수위에 선언)

      ```python
      from django.contrib.auth.decorators import login_required
      
      @login_requitred
      def update(request):
         ..... 
      ```

      * 로그아웃 상태에서 update로 접근을 했다.
        * /accounts/login/?next=/accounts/update/ 로 주소가 나타나는 것을 확인 가능
        * 이 주소로 형식은 전혁적인 GET타입의 querystring
        * request.GET.get('next')하면 /accounts/update/를 획득할수 있음
        * redirect(request.GET.get('next') or 'articles:index')로 이동할 수 있음.



___

* 회원 탈퇴
  * urls.py 를 정의 한다. 회원 탈퇴 요청이 들어오면 views.에서 함수를 실행하게 정의
  * views.py에서 삭제하는 함수를 정의
    * 회원가입 => DB에 유저 정보를 생성
    * 회원탈퇴 => DB에서 유저정보를 삭제
    * 유저정보를 delete()실행하면 삭제 됨
      * 유저 정보는 어디에?
        * request.user에 있음
        * request.user.delete() 하면 DB에서 삭제됨
    * 여기에서 생각해보면 로그인 하지 않은 유저가 요청을 하면 되지 않음
      * 로그인 되었을 때 만 회원 탙퇴 하겠끔 is_authenticated로 접급 제한.



____

* 회원 정보 수정

  * UserChangeForm 사용

    * User DB를 수정.

    * ModelForm

    * 사용 했더니?

    * 일반 유저는 대박.

      * 내가 나를 최고 관리자로 만들 수 있다.

        => UserChangeForm  을 그대로 사용하면 서비스 망

  * custom 해서 사용해야함

    * forms.py 에서 CustomUserChangeForm을 정의

      * UserChangeForm을 상속 바드아서 정의

        ```python
        from django.contrib.auth.forms import UserChangeForm
        from django.contrib.auth import get_user_model
        
        class CustomChangeForm(UserChangeForm):
            class Meta:
                models = get_user_model()
                fields = ('email', 'first_name', 'last_name')
        
        ```

____

