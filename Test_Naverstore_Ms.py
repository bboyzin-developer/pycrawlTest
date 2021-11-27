import pyautogui

#마우스 포지션 위치
print(pyautogui.position())

#마우스 커서 이동(좌,표)
#pyautogui.moveTo(1949,69)

#마우크 좌표 클릭(좌,표)
#pyautogui.click(1949,69)

#해당 이미지 스크린샷을 통한 클릭 가능하게 구현
#pyautogui.screenshot('1.png', region=(좌,표,이미지 사이,즈))
# num1 = pyautogui.locateCenterOnScreen('1.png') 이미지 파일로 클릭할 값 저장
# pyautogui.click(num1) 클릭

# 스크롤 하기
# pyautogui.scroll(10)


## 네이버 스토어 주문 매크로 셋팅##
## !!필수!! 크롬 뷰어 75% 상태에서 실행

# 1. 실행창 클릭
pyautogui.click(1516,474)

#2. 키보드로 스크롤하기
pyautogui.press('down', presses=3)

#3. 구매하기 클릭
pyautogui.click(1178,1003)

#3. 딜레이주기 1초
pyautogui.PAUSE =0.6

#4. 스크롤하기 시간벌기
pyautogui.scroll(-17)

#5. 키보드로 스크롤하기
pyautogui.click(528,805)
#pyautogui.press('down', presses=43)

#5. 배송유의사항 클릭
#pyautogui.click(687,172)

#6. 대상 요청메세지 클릭
#pyautogui.click(648,296)

#7. 무통장입금 클릭
#pyautogui.click(497,455)

#8. 입금은행1 클릭
#pyautogui.click(645,560)

#9. 입금은행2 클릭
#pyautogui.click(636,655)

#10. 개인 소득 공제 클릭
#pyautogui.click(591,797)

#11. 폰 번호 클릭
#pyautogui.click(672,879)

#12. 폰 번호 클릭(010)
#pyautogui.click(667,941)

#13. text 입력(6628)
#pyautogui.click(748,877)
#pyautogui.write('6628')

#13-1. text 입력(6628)
#pyautogui.click(818,874)
#pyautogui.write('2518')


# 14. 동의 버튼 클릭
#pyautogui.click(1290,983)

# 15. 최종 주문하기 클릭
#pyautogui.click(1350,783)