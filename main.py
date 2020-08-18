# -*- coding:utf-8 -*-
import urllib3
import json

# 언어 분석 기술(문어)
# openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"
# 언어 분석 기술(구어)
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU_spoken"

accessKey = "b59a9a69-4377-4363-a4d8-9fbbbe949af9"
analysisCode = "morp"
text = " "

# textFile = open("http://urbanunion.co.rk/8080/SRCtxt.txt", 'r')

textFile = open("./SRCtxt.txt", 'rt', encoding='UTF8')
SRCtext = textFile.read()
# text += str(SRCtext)
text += SRCtext
# print(text)
textFile.close()

# text += "허리 라인 핀턱으로 보다 더 여리한 실루엣을 연출해주는 블라우스에요. 잔잔한 세로 스트라이프 패턴으로 밋밋한 느낌을 덜어줘서 좋았구요 소매 단면이 넓어 팔뚝살을 커버해주기에 좋은 블라우스였답니다.  배색 컬러 대비로 더욱 스타일리쉬한 코디를 완성해주어 포인트 주기 딱 좋은 아이템이라 무난한 하의와도 쉽게 잘 어울릴 것 같아요 "

requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text,
        "analysis_code": analysisCode
    }
}

http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)

print("[responseCode] " + str(response.status))
print("[responBody]")
# print(str(response.data, "utf-8"))

f = open("./result.txt", mode='wb')
f.write(response.data)
f.close()