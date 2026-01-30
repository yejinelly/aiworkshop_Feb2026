# 환경 설정 가이드

워크샵 실습은 **로컬 환경(권장)** 또는 **Google Colab(백업)**에서 진행할 수 있습니다.

---

## 옵션 A: 로컬 환경 (권장)

### 1. 필수 요구사항

- Python 3.10 이상
- VSCode 또는 Cursor (또는 다른 IDE)
- Git

### 2. 저장소 클론

```bash
git clone https://github.com/yejinelly/aiworkshop_Feb2026.git
cd aiworkshop_Feb2026
```

### 3. 가상환경 생성 및 활성화

#### macOS/Linux
```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 4. 패키지 설치

**방법 1: uv 사용 (권장, 빠름)**
```bash
# uv 설치 (없는 경우)
curl -LsSf https://astral.sh/uv/install.sh | sh  # macOS/Linux
# Windows: https://docs.astral.sh/uv/getting-started/installation/

# 패키지 설치 (1-2분)
uv pip install -e .
```

**방법 2: pip 사용 (일반)**
```bash
# 패키지 설치 (3-5분)
pip install -e .

# 또는 requirements.txt 사용
pip install -r requirements.txt
```

💡 **참고**: `uv`는 pip보다 10-100배 빠른 Python 패키지 매니저입니다

### 5. API Key 설정

#### Step 1: Gemini API Key 발급 (5분)

**Gemini API (필수, 무료)**
1. https://aistudio.google.com/apikey 접속
2. "Create API key" 클릭
3. Key 복사 (클립보드에 저장)

**OpenAI API (선택, 유료)**
- Notebook 3 (Paper Review Agent)에서 필요
- 없어도 Notebook 1, 2, 2.5, 4는 실습 가능

#### Step 2: .env 파일 생성

`.env.example`을 복사하여 `.env` 파일을 만듭니다:

```bash
# macOS/Linux
cp .env.example .env

# Windows (cmd)
copy .env.example .env

# Windows (PowerShell)
Copy-Item .env.example .env
```

#### Step 3: API Key 입력

`.env` 파일을 열고 `your_gemini_api_key_here`를 실제 API key로 교체하세요:

```bash
# .env 파일
GEMINI_API_KEY=your_gemini_api_key_here  # <- 실제 key로 교체
OPENAI_API_KEY=your_openai_api_key_here  # 선택사항
```

**⚠️ 중요:** `.env` 파일은 git에 업로드되지 않습니다 (.gitignore에 포함됨)

### 6. VSCode에서 노트북 실행

1. VSCode에서 `aiworkshop_Feb2026` 폴더 열기
2. `notebooks/1_overview.ipynb` 열기
3. 우측 상단에서 Kernel 선택: `.venv` 또는 `Python 3.x.x (.venv)`
4. Cell 실행: `Shift + Enter`

### 7. 확인

첫 번째 노트북의 Cell 1-3을 실행하여 환경 설정을 확인하세요:

```
Cell 1: ✅ 💻 로컬 환경에서 실행 중
Cell 2: ✅ 로컬 환경: requirements.txt로 설치된 패키지 사용
Cell 3: ✅ .env 파일에서 API Key 로딩 완료
```

---

## 옵션 B: Google Colab (백업)

로컬 설치가 어렵거나 실패한 경우 Colab을 사용하세요.

### 1. Colab에서 노트북 열기

README의 Colab 배지를 클릭하세요.

### 2. API Key 설정 (Colab Secrets)

1. 좌측 사이드바 🔑 아이콘 클릭
2. "Add new secret" 클릭
3. 아래 키들을 추가:
   - Name: `GEMINI_API_KEY`, Value: [Gemini API key]
   - Name: `OPENAI_API_KEY`, Value: [OpenAI API key] (Notebook 3용)
4. 저장

### 3. 노트북 실행

Cell을 위에서부터 순서대로 실행하세요:

```
Cell 1: 🌐 Colab 환경에서 실행 중 + Google Drive mount
Cell 2: 📦 패키지 설치 중...
Cell 3: ✅ Colab Secrets에서 API Key 로딩 완료
```

---

## 트러블슈팅

### Q1. "No module named 'xxx'" 에러
```bash
# 가상환경이 활성화되어 있는지 확인
which python  # macOS/Linux → .venv/bin/python 출력되어야 함
where python  # Windows → .venv\Scripts\python.exe 출력되어야 함

# 가상환경 재활성화
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# 패키지 재설치
uv pip install -e .
# 또는: pip install -e .
```

### Q2. VSCode에서 Kernel이 안 보여요
```bash
# venv 활성화 후
source .venv/bin/activate  # macOS/Linux

# ipykernel 설치 확인
pip install ipykernel

# Jupyter kernel 수동 등록
python -m ipykernel install --user --name=aiworkshop --display-name="Python (.venv)"

# VSCode 재시작 후 노트북에서 "Python (.venv)" 선택
```

### Q3. API Key가 로딩 안 돼요 (로컬)
- `.env` 파일이 프로젝트 루트에 있는지 확인
- 파일 이름이 정확히 `.env`인지 확인 (`.env.txt` 아님!)
- API key에 따옴표 없이 입력했는지 확인

### Q4. API Key가 로딩 안 돼요 (Colab)
- Colab Secrets의 Name이 정확히 `GEMINI_API_KEY`인지 확인
- Cell을 재실행해보세요

### Q5. 로컬 환경 설정이 너무 복잡해요
→ Colab을 사용하세요! 설치 없이 브라우저에서 바로 실행됩니다.

---

## 워크샵 당일 준비 체크리스트

- [ ] **로컬 환경 (권장)**
  - [ ] Python 3.10+ 설치 확인
  - [ ] 저장소 클론 완료
  - [ ] 가상환경 생성 및 패키지 설치
  - [ ] `.env` 파일에 API key 설정
  - [ ] VSCode에서 노트북 실행 테스트

- [ ] **Colab 환경 (백업)**
  - [ ] Google 계정 확인
  - [ ] Gemini API key 발급
  - [ ] Colab에서 노트북 열기 테스트

- [ ] **공통**
  - [ ] 본인 연구 주제 또는 논문 초안 준비 (실습용)

---

## 참고 자료

- Python 설치: https://www.python.org/downloads/
- VSCode 설치: https://code.visualstudio.com/
- Cursor 설치: https://cursor.sh/
- Gemini API 문서: https://ai.google.dev/
