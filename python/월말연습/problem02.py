def my_number(n, m):
    a= f'010 - {n} - {m} 입니다.'
    return a

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    x, y = map( int,input().split())
    print(my_number(x, y))
    # => '010-1234-5678'
    print(my_number(1000, 9999))
    # => '010-1000-9999'