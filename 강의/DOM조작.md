# DOM조작

* HTML 을 Js로 조작
  * window
  * document
  * elements
* selector를 이용해서 조작
  * querySeletor / queerySelectorALL
  * dir(선택된 엘리먼트를 가진 변수)
    * 사용할수 있는 속성 정보를 볼 수 있ㄷ.
    * mdn 문서 (mdn +찾을려는 속성)

* DOM 조작 정리
  1. 선택한다.
  2. 수정 및 변경한다.

# 이벤트 리스너

* 이벤트는 브라우저에서 벌어지는 일

* 특정 이벤트가 벌어지며 특정 행동을 한다.

  이벤트 타겟.addEventListener (이벤트타입 ,할일)

* preventDefault()
  
  * 기본 동작을 동작하지 않게 막을수 있다

___

### 식별자

* 변수명은 식별자라고도 불림
* 규칙
  1. 반드시 문자, 달라($) 또는 밑줄로 시작해야 한다!! (숫자나, `-`로 시작할 수 없다.)
  2. 대소문자 구분
  3. 예약어는 사용할 수 없다.

* 스타일
  * 카멜케이스(lowerCamelCase)
    * 객체, 변수, 함수
  * 파스칼 케이스 (UpperCamelCase)
    * 클래스, 생성자
  * 대문자 스네이크 케이스(UPPER_CASE
    * 상수 : 변수나 변수의 속성이 변하지 않는 것.

___

### Hoisting

* var 로 선언된 변수는 선언 이전에 참조할 수 있는 현상.
  * 선언+ (undefined 초기화) 동시

```
console.log(name)
var name = '홍길동'

-var 일경우 선언하지않았는데 에러가 발생하지않는다

console.log(age)
let age = 10
```

___

### String

* js에서 문자열을 표현하는 방법

```javascript
const str1 = '홀 따옴표 사용'
const str2 = "쌍 따옴표 사용"

str1 + str // 2개의 문장을 한 문장으로 합침

const str3 = "줄 바 ㄲㅁ
은 허락되지 않는다."

//escape squence
const str4 = "줄바꿈은 \n 이렇게 해야합니다."

//template literal
const str5 = `안녕하세요.
출바꿈도 가능합니다.`

const num = 100
const str6 = `${num}- ${str1}`
```

* 리터럴
  - 리터럴이라는 단어는 값을 프로그램 안에서 직접 지정한다라는 의미
  - 리터럴은 값을 만드는 방법

___

### Switch

- break 꼭 있어야함 

```javascript
let name = 'admin'
switch(name)  {
    case 'admin': {
        console.log('관리자모드')
    	break
    }
    case 'manager': {
        console.log('매니저모드')
        break
    }
    default: {
        console.log(`${name}님 환영합니다.`)
    }
}
```

### for 문

```javascript
//1
for (let i = 0; i < 6; i++) {
    console.log(i)
}

//2
const numbers= [0, 1, 2, 3]
for (const number of numbers) {
    console.log(number)
}

//3
//에러발생
const obj = {a: 'apple', b:'banana'}
for (const o of obj) {
    console.log(o)
}
//VM169:2 Uncaught TypeError: obj is not iterable
    at <anonymous>:2:17


//4
const obj = {a: 'apple', b:'banana'}
for (const o in obj) {
    console.log(o)
    console.log(obj[o])
}

```

### 화살표 함수

```javascript
const arrow = function (nanme) {
    return `hello! ${name}!!`
}

// 1. function 키워드를 삭제하고 화살표를 추가한다
const arrow = (name) => {
	return `hello ${name}!!`
}

// 2. 매개변수가 하나일때는 괄호를 생략할 수 있다.
const arrow = name => {
	retrun `hello ${name}!!`
}

// 3. {} & return 생략 (body에 표현식이 1개인 경우)
const arrow = name => `hello, ${name}`
}


//연습코드
const exam = function () {
	return 'hello, world'
}

//1
const exam = () => (
    //console.log(name)
	return 'hell, world'
)
//2. skip

//2-1 그래도 적용하고싶다면 _를 사용
const exam = _ => {
    return 'hello, world'
}//언더바로 생략가능


//3.
const exam = () =>'hello, world'
or
const exam = _ =>'hello,world'



```





### funtion 키워드 호이스팅

```javascript
//선언식일때는 동작 -> 호이스팅 적용됨
add(2, 7)
function add (a, b){
    return a + b
}
//표현식 일때는? ->호이스팅 적용안됨(const)
sub(2, 7)
const sub = function (num1, num2) {
	return num1 - num2
}

// var는  함수일떄는 hoisting 적용안됨
sub(2, 7)
const sub = (num1, num2) {
	return num1 - num2
}
```



### 함수의 Object 축약형

```javascript
let obj = {
    name: 'ssafy',
    sayHi: function () {
        console.log('hello')
    } 
}
obj.sayHi() //'hello'

//ES6+
let obj2 = {
    name: 'ssafy',
    // 함수의 object 축약형.
    sayHi () {
        console.log('hello')
    } 
}
obj.sayHi() 'hi'
```



### JSON(JavaScript Object Notaion)

JavaScript Objecct 형태를 가지는 문자열

#### object -> JSON(string)

```javascript
const objData = {
    coffee: 'Americano',
    icecream: 'Bravo corn',
}
const jsonData = JSON.stringify(objData)
console.log(typeof(jsonData))
```

#### JSON -> object

```javascript
const objData2 = JSON.parse(jsonData)
console.log(typeof(objData2))

```

### forEach

- exercise

  ```javascript
  //배열 안에 있는 정보를 곱해서 그 넓이를 areas 배열에 저장
  const images = [
      {height:10, width:30},
      {height:20, width:90},
      {height:54, width:32},
  ]
  const areas=[]
  ```

  - 풀이코드

    ```javascript
    images.forEach(function (img) {
        areas.push(img.height * img.width) //{height: 10, widthL 30},
    })
    console.log('areas')
    ```


#### map

* exercise

  ```javascript
  //각 숫자들이 제곱근이 들어있는 새로운 배열을 만드세요
  
  const newNumber = [4, 9, 16]
  
  ```

  * 풀이

  ```javascript
  const newArray = newNumber.map(function (num){
      return num**(1/2)
  })
  
  // const newArray = newNumber.map(Math.sqrt) 
  ```

  ```javascript
  // forEach 문제 map으로 풀기
  const areas2 = images.map(function (image){
      return image.height*image.width
  })
  ```



#### filter

```javascript
const products = [
    { name : 'cucumber',type :'vegetable'},
    { name : 'banana',type :'fruit'},
    { name : 'carrot',type :'vegetable'},
    { name : 'apple',type :'fruit'},
]

const fruits = products.filter(function (product){
    //return product.type === 'fruit'
})

console.log(fruits)
```

* exercise

  ```javascript
  // number 배열중 50보다 큰 값들만 모은 배열  filteredNumbers을 만드세요
  const number = [ 15, 25, 35, 45, 55, 65, 75, 85, 95]
  ```

  ```javascript
  const filteredNumbers = number.filter(function(num){
      return num > 50
  })
  ```



#### find

```javascript
const products = [
    { name : 'cucumber',type :'vegetable'},
    { name : 'banana',type :'fruit'},
    { name : 'carrot',type :'vegetable'},
    { name : 'apple',type :'fruit'},
]
```

```javascript
const findNumbers = number.fine(function(num){
    return num = 50
})
```



#### some(1개만 통과)

```javascript
const products = [
    { name : 'cucumber',type :'vegetable'},
    { name : 'banana',type :'fruit'},
    { name : 'carrot',type :'vegetable'},
    { name : 'apple',type :'fruit'},
]

const someVegetable = products.some(function (product){
    return product.type === 'vegetable'
})
console.log(someVegetable)


const someWater = products.some(function (product){
    return product.type === 'Water'
})
console.log(someWater)


const zeroList = []
const someZero = zeroList.some(function (zero){
    return zero >50
})
console.log(zeroList)

```

```javascript
// requests 배열에서 status가 pending인 요청이 있는지 확인하세요
const requests = [
  { url: '/photos', status: 'complete' },
  { url: '/albums', status: 'pending' },
  { url: '/users', status: 'failed' },
]

const requestsList = requests.some(function(request)
    return request.status ==='pending'
})
console.log(requestList)
```

#### every (모든요소)

* exercise

```javascript
// users 배열에서 submited 인지 여부를 hasSubmitted에 저장
const users = [
    { id: 21, submmited: true },
    { id: 33, submmited: false },
    { id: 712, submmited: true},
]

const hasSubmitted = users.every(function(user){
    return user.submited ==='true'
})
console.log(hasSubmitted)
```



#### reduce

```javascript
// 주어진 basseUrl1 문자열 뒤에 필수 요청 변수인 api의 key-value 값을 key=value의 형태로 더하여 요청 url을 만드세요. url에서 요청 변수는 &문자로 구분됩니다.
const baseUrl = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?'
const api = {
  'key': 'API_KEY',
  'targetDt': '20200115'
}

const apiUrl = Object.entries(api).reduce(function(url,api) {
    return url + `${api[0]}=${api[1]}&`    
}, baseUrl)
console.log(apiUrl)
```



