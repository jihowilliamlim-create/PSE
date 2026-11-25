import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="나의 철학 가치관 검색기",
    page_icon="🔍",
    layout="centered"
)

# 철학자 데이터베이스
PHILOSOPHERS = [
    {
        "name": "소크라테스 (Socrates)",
        "keywords": ["성찰", "질문", "무지", "덕", "진리", "자아"],
        "summary": "검토되지 않은 삶은 살 가치가 없다.",
        "details": "자신의 무지를 자각하고 끊임없는 질문과 대화를 통해 참된 지식과 덕을 찾아가야 한다고 주장했습니다."
    },
    {
        "name": "에피쿠로스 (Epicurus)",
        "keywords": ["쾌락", "마음의 평정", "아타락시아", "행복", "고통 없음", "소박함"],
        "summary": "쾌락은 행복한 삶의 시작이자 끝이다.",
        "details": "육체적 고통이 없고 마음의 불안이 없는 상태(아타락시아)를 참된 쾌락이자 행복으로 보았습니다."
    },
    {
        "name": "프리드리히 니체 (Friedrich Nietzsche)",
        "keywords": ["주체", "초인", "극복", "운명애", "자유", "의지", "창조"],
        "summary": "나를 죽이지 못하는 것은 나를 더 강하게 만든다.",
        "details": "기존의 주어진 가치를 수동적으로 따르기보다, 자신의 운명을 사랑(아모르 파티)하고 끊임없이 스스로를 극복하는 주체적인 삶을 강조했습니다."
    },
    {
        "name": "임마누엘 칸트 (Immanuel Kant)",
        "keywords": ["의무", "도덕", "이성", "자율", "원칙", "선한 의지"],
        "summary": "네 의지의 한계가 언제나 보편적 입법의 원리가 될 수 있도록 행동하라.",
        "details": "결과나 감정에 휘둘리지 않고, 이성이 제시하는 보편적인 도덕 법칙과 의무에 따라 자율적으로 행동할 것을 주장했습니다."
    },
    {
        "name": "장폴 사르트르 (Jean-Paul Sartre)",
        "keywords": ["실존", "자유", "선택", "책임", "주체성"],
        "summary": "실존은 본질에 앞선다.",
        "details": "인간은 정해진 목적 없이 태어나며, 자신의 자유로운 선택과 행동을 통해 스스로의 존재 이유를 만들어간다고 보았습니다."
    }
]

# 헤더 영역
st.title("🔍 나의 철학 가치관 검색")
st.write("당신이 중요하게 생각하는 가치나 삶의 태도를 입력해보세요.")
st.caption("예시 단어: 자유, 마음의 평정, 도덕적 의무, 자기 극복, 성찰")

st.divider()

# 검색 입력 창
user_input = st.text_input("가치관 또는 삶의 태도 입력", placeholder="예: 자유와 선택을 중요하게 생각해요")

if st.button("철학자 찾기", use_container_width=True) or user_input:
    if not user_input.strip():
        st.warning("가치관을 입력해 주세요!")
    else:
        results = []
        for p in PHILOSOPHERS:
            # 입력 문장에 포함된 키워드 수 계산
            score = sum(1 for kw in p["keywords"] if kw in user_input)
            if score > 0:
                results.append({
                    "name": p["name"],
                    "summary": p["summary"],
                    "details": p["details"],
                    "score": score
                })

        # 점수 높은 순으로 정렬
        results.sort(key=lambda x: x["score"], reverse=True)

        st.subheader("💡 매칭 결과")

        if results:
            for item in results:
                with st.container():
                    st.markdown(f"### {item['name']}")
                    st.info(f'"{item["summary"]}"')
                    st.write(item["details"])
                    st.write("---")
        else:
            st.write("입력하신 단어와 일치하는 키워드가 없어 추천 철학자를 보여드립니다.")
            for p in PHILOSOPHERS[:2]:
                with st.container():
                    st.markdown(f"### {p['name']}")
                    st.info(f'"{p["summary"]}"')
                    st.write(p["details"])
                    st.write("---")
                    import streamlit as st
                    from google import genai

                    # 페이지 기본 설정
                    st.set_page_config(
                        page_title="AI 철학 가치관 검색기",
                        page_icon="🧠",
                        layout="centered"
                    )

                    # 사이드바 설정 (API 키 입력)
                    with st.sidebar:
                        st.header("⚙️ 설정")
                        api_key = st.text_input(
                            "Gemini API Key",
                            type="password",
                            help="Google AI Studio에서 발급받은 API 키를 입력하세요."
                        )
                        st.markdown("[🔑 API 키 발급받으러 가기](https://aistudio.google.com/)")
                        st.divider()
                        st.markdown("### 💡 팁")
                        st.info("짧은 단어뿐만 아니라, 요즘 하고 있는 고민이나 삶의 태도에 대한 긴 문장을 적어보세요.")

                    # 메인 헤더
                    st.title("🧠 AI 철학 가치관 분석 검색기")
                    st.write("당신의 생각, 고민, 삶의 태도를 자유롭게 적어보세요. AI가 가장 잘 어울리는 철학자와 그들의 사상을 찾아드립니다.")

                    st.divider()

                    # 사용자 입력 영역 (긴 문장 지원을 위해 text_area 사용)
                    user_input = st.text_area(
                        "당신의 가치관이나 고민을 적어주세요:",
                        placeholder="예: 매일 똑같이 반복되는 일상 속에서 내가 진정으로 원하는 게 뭔지 모르겠어요. 모든 걸 내 선택으로 책임져야 한다는 게 때로는 너무 무겁게 느껴집니다...",
                        height=120
                    )

                    # 분석 버튼
                    if st.button("철학적 분석 시작하기", use_container_width=True):
                        if not api_key:
                            st.warning("⚠️ 왼쪽 사이드바에 Gemini API Key를 입력해 주세요!")
                        elif not user_input.strip():
                            st.warning("⚠️ 분석할 내용을 입력해 주세요!")
                        else:
                            with st.spinner("🧠 철학자들의 사상을 뒤져 당신의 마음을 분석하는 중..."):
                                try:
                                    # Gemini 클라이언트 초기화 (최신 google-genai SDK 기준)
                                    client = genai.Client(api_key=api_key)

                                    # 프롬프트 구성
                                    prompt = f"""
                                    사용자가 자신의 철학적 가치관이나 고민을 다음과 같이 입력했습니다:
                                    "{user_input}"

                                    이 입력 내용을 바탕으로 가장 잘 어울리는 역사 속 철학자 2~3명을 선정해주세요.
                                    각 철학자에 대해 다음 형식으로 마크다운을 사용하여 답변해주세요:

                                    ### [철학자 이름]
                                    > "[대표 명언 또는 핵심 요약]"

                                    **매칭 이유 및 사상 설명:**
                                    (사용자의 입력 내용과 이 철학자의 사상을 연결하여 통찰력 있고 친절하게 3~4문장으로 설명)

                                    ---
                                    """

                                    # 모델 호출 (Gemini 2.5 Flash 또는 2.0 Flash 활용)
                                    response = client.models.generate_content(
                                        model='gemini-2.5-flash',
                                        contents=prompt
                                    )

                                    # 결과 출력
                                    st.success("분석이 완료되었습니다!")
                                    st.subheader("💡 AI 철학 분석 결과")
                                    st.markdown(response.text)

                                except Exception as e:
                                    st.error(f"오류가 발생했습니다: {e}")