from random import randint, random

inputMoney = 1260

fHund = int(inputMoney/500)
oHund = int((inputMoney - 500*fHund)/100)
fifty = int((inputMoney- 500*fHund - 100*oHund)/50)
ten = int((inputMoney - 500*fHund - 100*oHund - 50*fifty)/10)
print(" 500원개수 : ",fHund,"\n","100개수 : ",oHund,"\n","50개수 : ",fifty,"\n","10개수 : ",ten)
print("거슬러줄 동전의 최소값 : ",fHund+oHund+fifty+ten)