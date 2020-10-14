# Event Loop 동작 방법

```javascript
function func1 () {
    console.log('Hello')
    func2()
}

function func2 () {
    setTimeout(function () {
	    console.log('Ssafy!')        
    }, 0)
	func3()
}

function func3 () {
    console.log('Bye')
}


func1()
```

![996F87445BC7D90209](C:\Users\Edwin\Desktop\996F87445BC7D90209.gif)

