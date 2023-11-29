from fastapi import FastAPI
import requests
import json
from openai import OpenAI

app = FastAPI()

@app.get("/get_recipe_recommendation")
def get_recipe_recommendation():
    # OpenWeatherMap API로 현재 날씨 정보 가져오기
    weather_response = requests.get('https://api.weatherapi.com/v1/current.json?key=a887bb71919a421a966152403232411&q=Seoul&lang=ko&api=yes')
    weather_json = json.loads(weather_response.text)

    # OpenAI API 설정
    openai_key =
    client = OpenAI(api_key=openai_key)

    # 현재 날씨 정보 출력
    current_time = weather_json['location']['localtime']  # 현재 시간
    current_temp = weather_json['current']['temp_c']  # 현재 온도
    current_condition = weather_json['current']['condition']['text']  # 현재 날씨

    # OpenAI API를 사용하여 자취에서 해먹을 수 있는 요리 추천
    #prompt
    prompt = f"현재 시간은 {current_time}이고, 온도는 {current_temp}도, 날씨는 {current_condition}입니다. 상황에 맞게 해먹을 음식을 추천해주세요. (중요도 : 온도 > 날씨 > 시간 ) 출력예시 : 'recommend' : '된장찌개', 'comment' : 오늘은 ~하니까 '된장찌개'는 어때요?"

    
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=300,  # 요리 추천 텍스트의 최대 길이 조절
        temperature=0.7  # 다양성 조절
    )

    recipe_recommendation = completion.choices[0].text.strip()

    return {recipe_recommendation}
