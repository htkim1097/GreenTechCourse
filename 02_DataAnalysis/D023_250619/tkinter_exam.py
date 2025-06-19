# 중간 점검 문제
import tkinter as tk

window = tk.Tk()

window.geometry("600x800")
window.title("Window Title")

RadioVariety_1 = tk.IntVar()
RadioVariety_2 = tk.IntVar()
RadioVariety_3 = tk.IntVar()
RadioVariety_4 = tk.IntVar()
CheckVarlst = [tk.IntVar(), tk.IntVar(), tk.IntVar(), tk.IntVar()]

# 테스트 서두
label_desc = tk.Label(window, text='여러분의 고양이 지식 정도를 파악해보겠습니다:)\n')
label_desc.pack()

# 문제 1
label_question1 = tk.Label(window, text='\n[1번] 고양이가 좌우로 꼬리를 세차게 흔듭니다. 고양이는 어떤 상태일까요?')
label_question1.pack()

rbtn_q1_1 = tk.Radiobutton(window, text='1) 따분하다', value=1, variable=RadioVariety_1)
rbtn_q1_1.pack()

rbtn_q1_2 = tk.Radiobutton(window, text='2) 배가 고프다', value=2, variable=RadioVariety_1)
rbtn_q1_2.pack()

rbtn_q1_3 = tk.Radiobutton(window, text='3) 놀고 싶다', value=3, variable=RadioVariety_1)
rbtn_q1_3.pack()

rbtn_q1_4 = tk.Radiobutton(window, text='4) 기분이 안 좋다', value=4, variable=RadioVariety_1)
rbtn_q1_4.pack()

# 문제 2
label_question2 = tk.Label(window, text='\n[2번] 다음 중 세상에서 가장 큰 고양이의 종은 무엇일까요?')
label_question2.pack()

rbtn_q2_1 = tk.Radiobutton(window, text='1) 아메리칸 숏헤어', value=1, variable=RadioVariety_2)
rbtn_q2_1.pack()

rbtn_q2_2 = tk.Radiobutton(window, text='2) 메인쿤', value=2, variable=RadioVariety_2)
rbtn_q2_2.pack()

rbtn_q2_3 = tk.Radiobutton(window, text='3) 뱅갈', value=3, variable=RadioVariety_2)
rbtn_q2_3.pack()

rbtn_q2_4 = tk.Radiobutton(window, text='4) 터키쉬 앙골라', value=4, variable=RadioVariety_2)
rbtn_q2_4.pack()

# 문제 3
label_question3 = tk.Label(window, text='\n[3번] 다음 고양이의 행동 중 잘못된 것을 고르세요')
label_question3.pack()

radio1 = tk.Radiobutton(window, text='1) 엉덩이에 붙은 *을 떼어내기 위해 엉덩이로 기어다닌다', value=1, variable=RadioVariety_3)
radio1.pack()

radio2 = tk.Radiobutton(window, text='2) 음식에 발로 덮는 시늉을 하는 것은 아껴먹기 위해서 이다', value=2, variable=RadioVariety_3)
radio2.pack()

radio3 = tk.Radiobutton(window, text='3) 노트북 위에 올라가는 이유는 코딩하고 싶어서 이다', value=3, variable=RadioVariety_3)
radio3.pack()

radio4 = tk.Radiobutton(window, text='4) 수염을 만지면 입이 올라간다', value=4, variable=RadioVariety_3)
radio4.pack()

# 문제 4
label_question4 = tk.Label(window, text='\n[4번] 다음 중 고양이 빈혈에 관한 설명으로 옳지 않은 것을 고르세요')
label_question4.pack()

radio1 = tk.Radiobutton(window, text='1) 빈혈은 적혈구의 감소, 산소를 전달하는 헤모글로빈의 감소를 말한다', value=1, variable=RadioVariety_4)
radio1.pack()

radio2 = tk.Radiobutton(window, text='2) 빈혈의 원인으로는 출혈/백혈병 등의 감염/독성 물질 섭식/면역 매개성 질활 등이 있다', value=2, variable=RadioVariety_4)
radio2.pack()

radio3 = tk.Radiobutton(window, text='3) 빈혈이 발생하면 귓바퀴와 잇몸이 창백해지고 발바닥 패드도 창백해진다', value=3, variable=RadioVariety_4)
radio3.pack()

radio4 = tk.Radiobutton(window, text='4) 그 외에도 심한 기력 저하, 눈으로 확인하기 힘든 정도의 얕고 느린 호흡을 보인다', value=4, variable=RadioVariety_4)
radio4.pack()

# 문제 5
label_question5 = tk.Label(window, text='\n[5번] 다음 중 \'고양이과\' 동물들을 모두 선택하세요')
label_question5.pack()

chk_1 = tk.Checkbutton(window, text='1) 스라소니', variable=CheckVarlst[0])
chk_1.pack()

chk_2 = tk.Checkbutton(window, text='2) 재규어', variable=CheckVarlst[1])
chk_2.pack()

chk_3 = tk.Checkbutton(window, text='3) 사자', variable=CheckVarlst[2])
chk_3.pack()

chk_4 = tk.Checkbutton(window, text='4) 치타', variable=CheckVarlst[3])
chk_4.pack()

def calc_score():
    score = 0
    if RadioVariety_1.get() == 4:
        score += 20

    if RadioVariety_2.get() == 2:
        score += 20

    if RadioVariety_3.get() == 3:
        score += 20

    if RadioVariety_4.get() == 4:
        score += 20

    for i in CheckVarlst:
        if i.get():
            score += 5

    score_label.config(text='점수: ' + str(score))

# 완료 버튼
apply_btn = tk.Button(window, text='완료', command=calc_score)
apply_btn.pack()

# 점수 라벨
score_label = tk.Label(window, text="점수: ")
score_label.pack()

window.mainloop()