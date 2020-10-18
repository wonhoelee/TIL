A

___

git banch feature/nav

git switch feature/nav

git add .

git commit -m  'nav-fix'

git push origin feature/nav

머지 리퀘스트 (마스터와 병합)

git switch master

git pull origin master (합쳐진 코드 가져오기)

git branch -d feature/nav (브랜치 삭제)



B

____

git branch feature/footer

git switch feature/footer

git add .

git commit -m 'footer-nav'

git push origin feature/footer

머지 리퀘스트

git switch master

git branch -d feature/footer





python manage.py loaddata  파일이름