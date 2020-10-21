# Javascript 과목평가

> 브라우저를 동적으로 사용하기 위해 고안된 언어이다.

 

### 파편화&표준화 역사

* 파편화된 요소가 하나의 표준으로 정립되는 과정을 이해하면 접근



### javascript로 할수 있는 것

1. DOM(document object Model)
2. BOM(Browser object Model)
   * navigator, screen, location....
3. ECMAscript
   * 변수, 타입, 조건문, 반복문, 함수



#### DOM

> HTML, XML등과 같은 문서를 다루기 위한 독립적인 문서 모델 인터페이스

* DOM tree  구조
* window, document 와 같은 객체들이 존재,  window 는 최상위 객체로 생략 가능

##### DOM maniulation

> 문서 모델을 객체를 통해 조작

1. 선택

   * `querySelector/querseletorAll`

   * class를 선택할때 `'.class' ` , `document.getElementByClassName('class')`
   * id 선택 : `'#id'`, `document.getElementById('Id')`

   * 태그 선택 : `'h1'`, `docment.getElementByTagName('li')`

     ```text
     getElementByTagName(ClassName,Id, ...) : 아래에 데이터값을 추가해도 자동으로 업데이트 되어서 다시 호출할필요가 없다.
     ```

   * 같은 요소가 여려개 이면 첫번째로 일치하는거 선택

   * 복합 선택자

     * `const selectDescendant = document.querySelector('body li')`
       * body 태그 아래 li 첫번째 데이터
     * `const selectDescendant = document.querySelectorAll('body li')`
       * body 태그 아래 li 모든 데이터

     * `const selectChild = document.querySelector('body > li')`
       * body 태그 바로 아래의 li 선택

   * 단일 요쇼

     `document.getElementById(id)` : id만  활용 가능

     **`document.querySelector(selector)`** : 모든 선택자 가능

   * 여러개 요소

     `document.getElementsByTagName(tagName)`

     `document.getElementsByClassName(class)`

     **`document.querySelectorAll(selector)`**

2. 변경, 조작

   * `document.createElement(tagName)` : 생성해서 DOM에 부착

     * `document.createElement(tagName)`

       `appendChild` & `append`

       `removeChild` & `remove`

   * 속성변경

     * `innerText` & `innerHTML`

       `element.style.color` & `element.style.textDecoration`

       `setAttribute(attribute, value)`  : 속셩 변경(`'id' `or `'class' `, `'king'`) 

        `getAttribute(attribute) ` : 속성 보기( `'id' `or `'class' `)



```javascript
const myName = 'ssafy 4th'

if (myName === 'ssafy 4th') {
      console.log('ssafy 4th님 환영합니다.')
    } else if (myName === 'ssafy 3th') {
      console.log('ssafy 3th님 환영합니다.')
    } else {
      console.log('환영합니다.')
    }
```

```javascript
 for (let i = 0; i < 6; i++) {
      console.log(i)
    }
```

```javascript
//1. 함수 선언
    // 함수 선언식
    function add (num1, num2) {
      // console.log(num1 + num2)
      return num1 + num2
    }

    // 함수 표현식
    const sub = function (num1, num2) {
      // console.log(num1 - num2)
      return num1 - num2
    }

    // arrow function
    const multi = (num1, num2) => {
      return num1 * num2
        
    }
//2. 함수 호출
    const result1 = add(2, 7)
    const result2 = sub(7, 2)
    const result3 = multi(7, 2)
```



## Event Listener

**addEventListener**

*"특정 이벤트가 발생하면, 할 일을 등록하자"*

`EventTarget.addEventListener(type, listener)`

1. EventTarget 
   - 이벤트 감지를 위한 요소

2. addEventListener 
   - EventTarget에 이벤트를 등록할 때 사용하는 이벤트 핸들러
3. type
   - 이벤트의 종류

4. listener
   - (콜백) 함수
   - 이벤트가 발생하면 실행되는 함수

### `event.preventDefault()`

> "각 태그의 고유한(== 기본으로 설정된) 이벤트가 브라우저에서 동작하지 않도록 막는 행위"

1. 해당 이벤트의 기본 동작을 확인하고
2. 기본 동작을 막아보자
   * 막을수 있는지 log찍어보자!!



## todo CRUD

```javascript
const input = document.querySelector('input')
    const button = document.querySelector('button')
    
    function crud () {
        const content = input.value

        if (content) {
            const li = document.createElement('li')
            li.innerText = content

            const ul = document.querySelector('ul')
            ul.append(li)
            input.value = ''


            li.addEventListener('click', function(event) {
                // console.log(event.target.classList)
                // if (event.target.classList.contains('done')){
                //     event.target.classList.remove('done')

                // } else {
                //     event.target.classList.add('done')
                // }
                event.target.classList.toggle('done')
            })

            const delbutton = document.createElement('button')
            delbutton.innerText = '삭제'
            delbutton.style.marginLeft = '10px'
            console.log(delbutton.style)
            li.append(delbutton)

            delbutton.addEventListener('click', function(){
                li.remove()
            })
        } else {
            alert('빈값 안됨!!')
        }
    }
    button.addEventListener('click', crud)
    input.addEventListener('keypress', function(event) {
        if (event.code == 'Enter')
        crud()
    })
```



**AJAX(Asynchronous Javascript And XML)**

1. 다음과 같은 특징을 지닌다.

   - reload하지 않고 요청 작업을 비동기적으로 수행할 수 있다. (사용자 경험 향상)
   - 페이지의 전체가 아닌 일부만을 업데이트 할 수 있다. 

   - HTML, JSON, XML, 그리고 일반 텍스트 등을 교환할 수 있다.

**XHR(XMLHttpRequest)**

*브라우저 내장 객체*

1. 서버와 상호작용하기 위해서 사용한다. 전체 페이지의 새로 고침없이 데이터를 받아올 수 있다. 
2. 사용자가 하는 것을 방해하지 않고(== 새로고침이 발생하지 않는다.) 페이지의 일부를 업데이트 할 수 있다.
3. 주로 AJAX 프로그래밍에 사용한다. 

**How JavaScript works?**

1. <u>Asynchronous</u>

   > "기다려주지 않는다. ㅂㅣㄷㅗㅇㄱㅣ"

왜 기다려주지 않을까?

2. <u>Single Thread</u>

> "혼자 일하기 때문에 기다릴 수가 없다."

외부 서버로 요청을 보내는 상황을 가정해보자

1. 기다리는 상황
   - 요청을 보내고 응답을 기다린다. 
   - 응답이 오면 후에 남은 일을 처리한다.
   - 만약 응답이 1시간 뒤에 온다면 뒤에 해야하는 일을 그 시간 동안 할 수 없다.
2. 기다리지 않는 상황
   - 요청을 보내고 응답을 기다리지 않고 다른 일을 한다.
   - 응답이 오면 그때 그 일을 처리한다.
   - 응답이 1시간 뒤에 오더라도 상관없다.

3. <u>Event Loop</u>

> "JavaScript가 혼자서 일하는 방법"

- Call Stack

  - 함수의 호출을 기록하는 Stack 자료 구조

  - 한 번에 하나의 작업만 처리할 수 있으며 함수의 처리는 Stack이 다시 비워질 때까지 계속 이어진다.

- Web API(Browser API)

  - 브라우저에서 제공하는 API

  - `setTimeout`, `setInerval`, `XHR`

- Task Queue

  - Callback Function이 대기하는 Queue 자료 구조
  - 전송 순서대로 작업을 처리하기 위해 Queue 자료 구조를 사용함

- Event Loop

  - Call Stack이 비어있으면 Task Queue의 함수를 Call Stack으로 보낸다.

wI > taskQ > Event > callback

**Callback Function**

*"다른 함수의 인자로 전달되는 함수"*

1급 객체(First-Class Citizen)

> "다른 객체들에 일반적으로 적용 가능한 연산을 모두 지원하는 객체"



아래와 같은 특징을 지니면 1급 객체라고 부른다.

1. return 값으로 사용 가능
2. **<u>함수의 인자로 사용 가능</u>**
3. 변수에 할당 가능

JavaScript(+Python)의 함수는 위와 같은 특징 3가지를 모두 만족하므로 1급 객체의 특성을 가진다. 



Callback은 이러한 특징 중 "인자로 넘어간다."라는 특징에 해당한다. 우리는 지금까지 이러한 특징을 알게 모르게 활용했다. 

 일의 결과가 다른 일의 trigger가 되는 과정이 연속적으로 발생하면 콜백 함수의 콜백 함수를 넣는 과정이 반복되고 이는 콜백 지옥(Callback Hell)로 이어진다.

**Promise**

*"비동기 작업이 맞이 할 미래의 결과(성공/실패)를 약속하는 객체"*

1. 콜백 지옥을 해결하기 위해 ES6부터 등장한 개념
2. 2가지의 약속이 이행되는 상황을 가정한다.
   - 성공
     - `.then(callback function)`
     - 성공하고 나면 무엇을 할 지 
   - 실패
     - `.catch(callback function)`
     - 실패하면 에러를 어떻게 처리(잡을지) 할 지

**Axios**

*"**Promise based** HTTP client for the browser and node.js"*

1. Promise 기반의 비동기 요청을 할 수 있는 JavaScript 라이브러리

2. 사용법

   ```javascript
   axios.get('https://jsonplaceholder.typicode.com/todos/asdf')
   	// Promise의 성공/실패에 대한 약속 이후의 처리를 할 수 있다.
     .then(function (res) {
       console.log(res)
       return res.data
     })
   	// 이전 .then 내부 CB의 return 값은 다음 .then 내부 CB의 인자로 넘어온다.
     .then(function (data) {
       console.log(data)
       return data.title
     })
     .then(function (title) {
       console.log(title)
     })
   	// Error는 요청를 1이 아닌 asdf로 변경해서 확인해보자
     .catch(function (err) {
       console.log(err)
     })
   ```

3. 참고 사항

   - Axios도 결국 내부적으로 `xhr`을 사용한다. 
   - 결국, 이를 편하고 직관적으로 사용할 수 있도록 만들어 놓은 라이브러리다.

___

## JavaScript 문법 정리

```
var : 재할당, 재선언, 함수 스코프
let : 재할당, 블록스코프
const : 블록 스코프
```



### 타입

* Number
* Boolean : True, False
* Empty Value
  * null  : 개발자가 의도적으로 없음 표현 typeof(object)
  * undefined :값이 없을 경우 JavaScript가 할당 하는 값 typeof(undefined)

___



### 연산자

* python 대부분 동일

  * c +=  a  // c에서 10을 더한다.
  * c -= a 
  * c *= a
  * c++  // c 에서 1을 더한다
  * c--   // c에서 1을 뺀다.

* 비교연산자

  * < , > 

* 동등연산자

  * ==

* 일치연산자

  * ===

* 논리연산자

  * and or not
  * &&(and), `\\(or)` , ! (not)

* 삼항 연산자 

  *  조건식이 참이면 : 앞의 값이 반환되며 그 반대일 경우 : 뒤의 값이 반환되는 연산자다. 

  *  삼항 연산자의 중첩 사용은 지양하며, 일반적으로 한 줄에 표현한다.

    ```js
    true ? 1 : 2 //1
    false ? 1 : 2 // 2
    
    const result = Math.PI > 4 ? 'yep' : 'Nope'
    console.log(result) // Nope
    ```

    

___

#### string

* js에서 문자열 표현

* 줄바꿈 x

* 줄바꿈은 \n 사용

  ```javascript
  const str1 ='abc'
  const str2 ='def'
  
  str3 = str1 + str2 //'abcdef'
  ```

___



### if

```javascript
if (조건식) {결과창}

if (name === 'admin') {
    console.log('관리자님 환영합니다.')
} elif (name == 'manage'){
    console.log('매니저님 환영합니다.')
} else {
     console.log(`${name}님 환영합니다.`)
}
```



####  switch

* 모든 case를 돌아가기때문에 break 필수

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

// break가 없으면
// console.log('관리자모드')
// console.log('매니저모드')
// console.log('`${name}님 환영합니다.`') << admin으로 다실행된다.
```



####  for 문

```javascript
//1 
for (let i = 0; i < 6; i++) {
    console.log(i)
}

//2 for of 매 요소는 블럭 내에서 새롭게 선언되기 때문에 반드시 변수 선언 키워드를 작성한다
const numbers= [0, 1, 2, 3]
for (const number of numbers) {
    console.log(number)
}

//3 for in Object의 key를 순회하는 반복하는 반복문이다. Array의 경우 index를 순회한다

const fruits = {a:'apple', b:'banana'}

for (const key in fruits) {
    console.log(key)
    console.log(fruits[key])
}
```



### while

```javascript
let i = 0
while (i < 6) {
    console.log(i)
    i++
}
```



## 함수연산자

* 한수 선언식

  ```javascript
  function add (num1, num2) {
      return num1 + num2 
  }
  
  add(2,7)
  ```

* 함수 표현식

  ```javascript
  const sub = function(num1, num2) {
      return num1 - num2
  }
  ```

  ```javascript
  const mysub = function sub (num1, num2) {
      return num1 - num2
  }
  ```

* 화살표 함수 

  * 함수 선언 시 function 키워드와 중괄호를 생략하기 위해 고안된 단축 문법이다

    ```javascript
    const arrow = fnnction(name) {
        return `hello ${name}`
    }
    
    
    const arrow = (name) => {return `hello ${name}`}
    
    const arrow = name =>{ return `hello ${name}`}
    
    const arrow = name => return `hello ${name}`
    
    // ㅍ
    const arrow = name => ({message:return `hello ${name}`})
    ```

    



##  자료구조

### 배열(Array)

### index

```javascript
const number = [1, 2, 3, 4]
number[0] 		// 1
number[-1] 	// undefined 
number.length	//4
```

### reverse

```javascript
number.reverse()
number 			// [4,3,2,1]
```

### push & pop

```javascript
number.posh('a') // [1,2,3,4,'a']
number.pop()	 // [1,2,3,4] pop(3) 이여도 가장 뒤의 요소 제거
```



### unshift & shift

```javascript
number.unshift('a') // ['a',1,2,3,4]
number.shift('a')	// [1,2,3,4] 가장 처음요소 제거
```



### includes

```javascript
number.includes(1) // number안에 1이라는 요소가 존재하는가
```



###  indexof

```javascript
number.indexof('b') // number안에 'b'의 문자열에대한 인덱스 번호 없으면 -1 출력
```



### join

```javascript
number.join('-') // '1-2-3-4'
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

const newArry = products.map(function (num){
    return num.name
})

console.log(newArry)

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
const findNumbers = number.find(function(num){
    return num = 50
})
//값이 없다면
undefined를 반환한다
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



const scores = [90, 90, 80, 77]

const totalscore = scores.reduce (function (sum, score) {
    return sum _ score
    
}, 0) //0 생략가능 => 첫번째 아이템이 누적값

console.log(totalscore) // 337
```









