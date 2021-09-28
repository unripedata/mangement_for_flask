# 통합 관리 웹 사이트 (1) - 개요

1. 프로젝트 명

   - management_for_flask

2. 개발 사유

   - 혼서 프론트, 백엔드, 서버, 관리를 편하게 하기 위해 개발
   
3. 구조도

   - 전체 구조도

     ![](https://images.velog.io/images/unripedata/post/121be2ee-5bf6-408f-bb7d-5eaf1b36cab6/image.png)

4. 서버 환경 정보 

   - 서버
     - vultr 클라우드 (AWS를 사용하려 했으나 월급쟁이이므로 저렴한 클라우드 이용)
   - 도메인
     - imw.unripedata.com (웹)
     - api.imw.unripedata.com (RestApi - 내부 및 지정 아이피만 접근)
     - cmd.imw.unripedata.com (TcpServer Api)

5. Docker 정보

   - 내부 아이피

     - gateway: 172.19.0.1
     - subnet: 172.19.0.0/21

   - 기능별 아이피/포트

     - MariaDB
       - 아이피: 172.19.0.10
       - 포트: 3306

     - Redis
       - 아이피: 172.19.0.102
       - 포트: 9001

     - Nginx
       - 아이피: 172.19.0.150 
       - 포트: 80(WEB), 16000(DB API), 17000(TCP API), 20000(TCP Port) 

     - web 
       - 아이피: 172.19.0.121-129
       - 포트: 80(WEB)
     - 공용 API
       - 아이피: 172.19.0.131-139
       - 포트: 80(WEB)
     - TCPServer
       - 아이피: 172.19.0.141-149
       - 포트: 80(WEB), 20000(TCP Port)

6. 프로그램 연동

   - 나이키 자동 Draw 기능 (소스 공개 불가능)
   - 쿠팡 파트너스 자동 포스팅 기능 (소스 공개 불가능)
   
7. 이슈

   - 소스 리펙토링 중
   - docker -volum및 SSL 미반영
   - uwsgi 미반영
   - 소스 리펙토링 후 반영 예정
   - 하위 도메인 기준 도메인 용도 분리 방법에 대해 변경 필요
     - 기존 api.unripedata.com -> 변경 www.unripdata.com/api/~
     - dockerfile 내용 변경 필요
