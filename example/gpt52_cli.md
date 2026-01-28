# GPT-5.2 CLI 예제 (Python)

이 문서는 `gpt52_cli.py` 스크립트를 설명합니다. 이 스크립트는 CLI에서 프롬프트를 입력받아 OpenAI Responses API에 `gpt-5.2` 모델로 요청하고, 응답을 출력합니다.

## 파일 구성

- `gpt52_cli.py`: 실행 가능한 CLI 예제.

## 동작 방식

1. **API 키 로딩**
   - `os.getenv`로 `OPENAI_API_KEY` 환경 변수를 읽습니다.
   - 환경 변수가 없으면 명확한 오류 메시지와 함께 종료합니다.

2. **프롬프트 입력**
   - `input("Enter your prompt: ")`로 사용자 입력을 받고 공백을 제거합니다.
   - 비어 있으면 요청을 보내지 않도록 종료합니다.

3. **추가 입력(추론 강도, 이미지 경로)**
   - `reasoning_effort` 값( `low` / `medium` / `high` )을 입력받습니다. 엔터를 누르면 생략합니다.
   - 이미지 입력을 위해 쉼표(`,`)로 구분된 이미지 파일 경로를 입력받습니다. 엔터를 누르면 생략합니다.
   - 이미지가 있을 때는 각 파일을 Base64로 인코딩해 `data:` URL로 변환합니다.

4. **OpenAI 클라이언트 생성**
   - 로드한 API 키로 `OpenAI` 클라이언트를 생성합니다.

5. **Responses API 요청**
   - `client.responses.create(...)`를 호출하며 다음 값을 전달합니다:
     - `model="gpt-5.2"`
     - `input`에 텍스트와 이미지(선택)를 함께 전달
     - `reasoning_effort`는 입력했을 때만 포함
   - 최신 OpenAI **Responses API** 패턴을 사용합니다.

6. **출력**
   - 모델 출력에서 합쳐진 텍스트인 `response.output_text`를 출력합니다.

## 사용 방법

```bash
# OpenAI SDK 설치
pip install openai

# API 키 환경 변수 설정
export OPENAI_API_KEY="your_key_here"

# 스크립트 실행
python gpt52_cli.py
```

프롬프트를 입력하면 모델의 응답이 표준 출력으로 표시됩니다.

### 입력 예시

```
Enter your prompt: 이 이미지들에 공통으로 보이는 물체가 뭐야?
Reasoning effort (low/medium/high). Press Enter to skip: medium
Image paths (comma-separated). Press Enter to skip: /path/to/a.png, /path/to/b.jpg
```

## 참고 사항

- 예제는 이해를 위해 최소한의 입력만 사용합니다. 필요에 따라 시스템 프롬프트, 멀티턴 입력, 도구 호출 등으로 확장할 수 있습니다.
- 환경 변수를 사용하기 싫다면 `OpenAI(api_key=...)`로 직접 키를 전달할 수도 있지만, 보안을 위해 환경 변수 사용을 권장합니다.
- 이미지 경로는 로컬 파일 경로이며, 파일을 읽어 `data:` URL로 전송합니다. 파일 경로가 잘못되면 오류가 발생합니다.
