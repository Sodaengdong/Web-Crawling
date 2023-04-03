import openpyxl   

#내가 작업할 Workbook 생성하기
wd = openpyxl.Workbook()

#작업할 Workbook 내 Sheet 활성화
sheet = wd.active

#Sheet내 Cell 선택(A1셀에 1이라는 값 할당)
sheet['A1'] = 1

#작업 마친 후 파일 저장(파일명 저장할 때 확장자 .xlsx으로 저장!)
wd.save("exceltest.xlsx")