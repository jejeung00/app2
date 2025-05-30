import streamlit as st

st.title("창호 디자인 추천 시스템 (Prototype)")

# 사용자 입력 받기
width = st.number_input("창호 가로 길이 (mm)", min_value=100, max_value=3000, value=1200)
height = st.number_input("창호 세로 길이 (mm)", min_value=100, max_value=3000, value=1500)

# 파라미터 추천 함수
def recommend_params(width, height):
    ratio = round(width / height, 2)
    area = width * height

    if ratio > 1.5:
        frame_color = "진회색"
        glass_color = "청색"
        divides = 3
        open_type = "슬라이딩"
    elif ratio < 0.8:
        frame_color = "흰색"
        glass_color = "클리어"
        divides = 1
        open_type = "여닫이"
    else:
        frame_color = "우드톤"
        glass_color = "브론즈"
        divides = 2
        open_type = "고정창"

    return {
        "프레임 색상": frame_color,
        "유리 컬러": glass_color,
        "디바이드 수": divides,
        "개폐 방식": open_type,
        "프레임 두께": "30mm",
        "핸들 타입": "인셋",
        "차음 성능": "중간",
        "채광 등급": "높음" if area > 1500000 else "중간"
    }

if st.button("창호 디자인 생성"):
    result = recommend_params(width, height)
    st.subheader("🎨 추천된 창호 디자인 파라미터")
    for key, value in result.items():
        st.write(f"✅ {key}: {value}")