from flask import Flask, render_template, request, jsonify
from google import genai 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 화면에서 버튼 누르면 실행되는 통로
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    selected_function = data.get('function') # 화면에서 선택한 기능 (explain, quiz 등)
    user_input = data.get('input')           # 사용자가 입력한 질문 내용

    # 채워야 할 구역(선택한 기능에 따라 프롬프트 다르게 주기)
    if selected_function == "explain":
        # [기능 1: 문제 해설] - 바로 답 안 주고 되묻기 기획 반영
        prompt = f"학생의 생각 과정을 고정해주는 과외 선생님처럼 말해줘. 질문: {user_input}"
        ai_reply = f"이 문제 풀 때 무슨 생각부터 했어? 이 문제에서 막힌 이유를 설명해봐 "
        # 여기에 gpt api 코드 넣어서 프롬프트 입력받고 출력하기
        client = genai.Client()
        response = client.modesl.generate_content(
            model="gemini_2.5-flash",
            contents=prompt
        ) 
        #print (response.text)


    elif selected_function == "quiz":
        # [기능 2: 퀴즈 생성]
        prompt = f"다음 내용을 바탕으로 중고등학생용 퀴즈를 만들어줘: {user_input}"
        

    elif selected_function == "method":
        # [기능 3: 공부법 추천]
        prompt = f"다음 과목이나 상황에 맞는 효과적인 공부법을 추천해줘: {user_input}"
        

    elif selected_function == "hint":
        # [기능 4: 개념접근 및 힌트]
        prompt = f"정답을 주지 말고 문제를 풀 수 있는 핵심 개념과 힌트만 줘: {user_input}"
        

    else:
        prompt = user_input
        ai_reply = "기능을 올바르게 선택해주세요."

    # 
    # ai_reply = 실제_AI_API_호출함수(prompt)

    return jsonify({"reply": ai_reply})

if __name__ == '__main__':
    app.run(debug=True)