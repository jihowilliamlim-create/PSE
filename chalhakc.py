
import time
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

                # 503 오류(일시적 과부하)에 대비한 재시도 로직 함수
                def generate_with_retry(max_retries=3, wait_seconds=2):
                    for attempt in range(max_retries):
                        try:
                            return client.models.generate_content(
                                model='gemini-3.8-flash',
                                contents=prompt
                            )
                        except Exception as err:
                            if attempt < max_retries - 1:
                                time.sleep(wait_seconds)
                            else:
                                raise err

                # 모델 호출 (재시도 로직 포함)
                response = generate_with_retry()

                # 결과 출력
                st.success("분석이 완료되었습니다!")
                st.subheader("💡 AI 철학 분석 결과")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
