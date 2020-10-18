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

