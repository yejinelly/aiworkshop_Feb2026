# AI 문헌 리뷰 에이전트 워크샵

**SNU AI Psychology - February 2026**

---

## 워크샵 개요

| Part | 내용 | 시간 |
|------|------|------|
| **Part 1** | 오픈소스 Literature Agent 개관 | 10분 |
| **Part 2** | Deep Dive: 문헌 검색 (Agent Laboratory / PaSa) | 25분 |
| **Part 3** | Deep Dive: Related Work 생성 (LitLLM) | 25분 |
| **Part 4** | Deep Dive: Peer Review 시뮬레이션 (AgentReview) | 20분 |
| **Part 5** | 토론: 우리 연구실에 맞게 커스텀하기 | 10분 |

### 각 Deep Dive 구성
1. **파악하기** - 코드 구조, 핵심 모듈, 데이터 흐름
2. **써보기** - 실제 논문으로 실행
3. **바꿔보기** - 프롬프트/설정 수정해서 결과 비교

---

## 파일 구조

```
aiworkshop_Feb2026/
├── README.md                        # 워크샵 가이드
├── notebooks/
│   ├── 1_overview.ipynb             # Part 1: 에이전트 개관
│   ├── 2_literature_search.ipynb    # Part 2: 문헌 검색
│   ├── 3_related_work.ipynb         # Part 3: Related Work
│   └── 4_peer_review.ipynb          # Part 4: Peer Review
└── examples/
    ├── sample_abstract.txt          # 테스트용 초록
    └── sample_paper.pdf             # 테스트용 논문
```

**실습에서 clone할 저장소**
- `github.com/SamuelSchmidgall/AgentLaboratory` - 문헌 검색
- `github.com/bytedance/pasa` - 논문 검색
- `github.com/ServiceNow/litllm` - Related Work
- `github.com/ahren09/agentreview` - Peer Review

---

## Part 1: 오픈소스 Literature Agent 개관 (15분)

> 코드가 공개된 에이전트만 다룸. 웹 서비스(Elicit, Consensus 등)는 제외.

| 프로젝트 | Stars | 용도 | 검색 DB |
|----------|------:|------|---------|
| [GPT-Researcher](https://github.com/assafelovic/gpt-researcher) | 24.9k | 웹검색 → 보고서 | 웹 (Tavily) |
| [AI-Scientist](https://github.com/SakanaAI/AI-Scientist) | 12k | 아이디어→논문 자동화 | Semantic Scholar |
| [PaperQA2](https://github.com/Future-House/paper-qa) | 8k | PDF RAG Q&A | Semantic Scholar |
| [**Agent Laboratory**](https://github.com/SamuelSchmidgall/AgentLaboratory) | 5.2k | **문헌→실험→보고서** | **arXiv ⭐** |
| [**PaSa**](https://github.com/bytedance/pasa) | 1.5k | **논문 검색 특화** | **arXiv + Scholar ⭐** |
| [**AgentReview**](https://github.com/ahren09/agentreview) | - | **Peer Review 시뮬레이션** | 없음 (EMNLP 2024) |
| [**LitLLM**](https://github.com/ServiceNow/litllm) | - | **Related Work 생성** | Semantic Scholar (TMLR 2024) |

→ 오늘 집중:
- **문헌 검색**: Agent Laboratory, PaSa (arXiv 직접 검색)
- **논문 작성**: LitLLM (Related Work), AgentReview (Peer Review)

---

## Part 2: Deep Dive - 문헌 검색 (25분)

> **목표**: arXiv/Scholar에서 관련 논문 자동 검색

### Agent Laboratory

```
AgentLaboratory/
├── agents/
│   ├── literature_agent.py   # 문헌 검색 에이전트
│   ├── experiment_agent.py   # 실험 에이전트
│   └── report_agent.py       # 보고서 에이전트
├── tools/
│   └── arxiv_search.py       # arXiv API 래퍼
└── run.py
```

**핵심 흐름:**
1. 연구 주제 입력
2. arXiv API로 관련 논문 검색
3. 논문 요약 + 실험 제안
4. 보고서 생성

```bash
git clone https://github.com/SamuelSchmidgall/AgentLaboratory
cd AgentLaboratory && pip install -r requirements.txt
python run.py --topic "your research topic"
```

### PaSa (Paper Search Agent)

```
pasa/
├── agents/
│   ├── crawler.py     # 논문 크롤링 에이전트
│   └── selector.py    # 관련성 평가 에이전트
├── search/
│   ├── arxiv.py       # arXiv 검색
│   └── scholar.py     # Google Scholar 검색
└── run_search.py
```

**핵심 흐름:**
1. 연구 질문 입력
2. Crawler가 arXiv/Scholar 검색
3. Selector가 관련성 평가 (PPO 학습됨)
4. 순위화된 논문 리스트 반환

```bash
git clone https://github.com/bytedance/pasa
cd pasa && pip install -r requirements.txt
python run_search.py --query "your research question"
```

### 바꿔보기: 커스텀

| 수정 포인트 | 파일 | 아이디어 |
|-------------|------|----------|
| 검색 DB | `arxiv_search.py` | PubMed API 추가 |
| 검색 쿼리 | `literature_agent.py` | 심리학 키워드 템플릿 |
| 필터링 | `selector.py` | 연도/저널 필터 추가 |

---

## Part 3: Deep Dive - LitLLM (25분)

> **목표**: Related Work 섹션 초안 자동 생성

### 3-1. 파악하기: 코드 구조

```
litllm/
├── litllm/
│   ├── retriever.py      # 관련 논문 검색
│   ├── summarizer.py     # 논문 요약
│   ├── writer.py         # Related Work 생성
│   └── prompts/          # 프롬프트 템플릿
├── data/
│   └── arxiv_cache/      # 논문 캐시
└── generate_related_work.py
```

**핵심 흐름:**
1. 논문 초안 입력 → 키워드 추출
2. Semantic Scholar API로 관련 논문 검색
3. 각 논문 요약
4. Related Work 문단 생성 (인용 포함)

### 3-2. 써보기: 실행

```bash
# 설치
git clone https://github.com/ServiceNow/litllm
cd litllm
pip install -r requirements.txt

# 실행
python generate_related_work.py \
  --input your_draft.txt \
  --output related_work.md \
  --num_papers 10
```

### 3-3. 바꿔보기: 커스텀

| 수정 포인트 | 파일 | 아이디어 |
|-------------|------|----------|
| 검색 DB | `retriever.py` | PubMed 추가 (심리학용) |
| 요약 스타일 | `prompts/summary.txt` | "방법론 중심으로" |
| 작성 스타일 | `prompts/writer.txt` | "APA 스타일로", "비판적 톤으로" |
| 언어 | `writer.py` | 한글 Related Work |

---

## Part 4: Deep Dive - AgentReview (20분)

> **목표**: 논문 제출 전 AI 피드백 받기

### 4-1. 파악하기: 코드 구조

```
agentreview/
├── agentreview/
│   ├── arena.py          # 메인 시뮬레이션 루프
│   ├── paper.py          # 논문 파싱
│   ├── reviewer.py       # 리뷰어 에이전트
│   └── prompts/          # 리뷰어 페르소나
├── data/
│   └── iclr_reviews/     # 실제 ICLR 리뷰 데이터
└── run_review.py         # 실행 스크립트
```

**핵심 흐름:**
1. 논문 PDF → 섹션별 파싱
2. 리뷰어 에이전트 생성 (다양한 페르소나)
3. 각 리뷰어가 독립적으로 평가
4. 점수 + 코멘트 집계

### 4-2. 써보기: 실행

```bash
git clone https://github.com/ahren09/agentreview
cd agentreview && pip install -r requirements.txt
python run_review.py --paper your_paper.pdf --num_reviewers 3
```

### 4-3. 바꿔보기: 커스텀

| 수정 포인트 | 파일 | 아이디어 |
|-------------|------|----------|
| 리뷰어 페르소나 | `prompts/reviewer.txt` | "심리학 저널 리뷰어처럼" |
| 평가 기준 | `reviewer.py` | novelty, methodology, clarity 가중치 |
| 출력 형식 | `arena.py` | 한글 리뷰, 체크리스트 형식 |

---

## Part 5: 토론 - 커스텀 아이디어 (10분)

### 우리 연구실에 맞게 바꾼다면?

| 도구 | 커스텀 아이디어 |
|------|----------------|
| **Agent Laboratory** | PubMed API 모듈 추가 |
| **PaSa** | 심리학 저널 필터링 |
| **LitLLM** | 메타분석용 "효과크기 요약" 모드 |
| **AgentReview** | 지도교수님 피드백 스타일 학습 |
| **파이프라인** | 검색→Related Work→Review 연결

---

## Google Colab 실습 노트북

### 노트북 구성

| 노트북 | 내용 | Colab 링크 |
|--------|------|------------|
| `1_overview.ipynb` | Part 1: 에이전트 개관 + API 테스트 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]() |
| `2_literature_search.ipynb` | Part 2: Agent Laboratory / PaSa 실습 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]() |
| `3_related_work.ipynb` | Part 3: LitLLM 실습 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]() |
| `4_peer_review.ipynb` | Part 4: AgentReview 실습 | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]() |

### 각 노트북 상세 구조

```
📓 X_tool_name.ipynb

[Cell 1-3] 🔧 SETUP
├── Cell 1: Google Drive Mount + 작업 폴더 설정
├── Cell 2: 패키지 설치 (!pip install ...)
└── Cell 3: API Key 로딩 (dotenv 또는 Colab Secrets)

[Cell 4-8] 📖 1. 파악하기 - 코드 구조 이해
├── Cell 4: [Markdown] 프로젝트 구조 다이어그램
├── Cell 5: [Markdown] 핵심 흐름 설명
├── Cell 6: 핵심 모듈 임포트 + 클래스 확인
├── Cell 7: 주요 함수 시그니처 출력
└── Cell 8: [Markdown] 💡 질문: "이 구조에서 어떤 부분을 바꾸면 좋을까?"

[Cell 9-14] ▶️ 2. 써보기 - 실행 실습
├── Cell 9: [Markdown] 샘플 데이터 설명
├── Cell 10: 샘플 데이터로 실행 (발표자 데모)
├── Cell 11: 결과 출력 + 시각화
├── Cell 12: [Markdown] "DIY: 본인 데이터로 실행해보세요"
├── Cell 13: # DIY - 빈 셀 (참가자 실습)
└── Cell 14: # DIY - 결과 확인 셀

[Cell 15-20] 🔨 3. 바꿔보기 - 커스텀 실습
├── Cell 15: [Markdown] 수정 포인트 표
├── Cell 16: 프롬프트 수정 예시 (Before/After)
├── Cell 17: # DIY - 프롬프트 수정 실습
├── Cell 18: 설정 파라미터 변경 예시
├── Cell 19: # DIY - 설정 변경 실습
└── Cell 20: 결과 비교 (원본 vs 수정본)

[Cell 21-22] 💡 4. 토론
├── Cell 21: [Markdown] 토론 질문 3개
└── Cell 22: [Markdown] 다음 단계 제안
```

### 노트북 작성 패턴 (이전 워크샵 참고)

```python
# === Cell: Setup ===
from google.colab import drive
drive.mount('/content/drive/')

import os
os.chdir("/content/drive/MyDrive/aiworkshop_Feb2026/")

# API Key 로딩 (dotenv 방식)
!pip install python-dotenv -q
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# === Cell: DIY 템플릿 ===
# DIY: 본인 연구 주제로 실행해보세요
# 힌트: query 변수만 바꾸면 됩니다

query = "your research topic here"  # <- 이 부분 수정

# 아래 코드는 그대로 실행
result = search_papers(query)
display(result)
```

### 실습 환경 옵션

| 옵션 | 장점 | 단점 |
|------|------|------|
| **Google Colab** | 설치 불필요, GPU 무료 | API key 입력 필요 |
| **로컬 venv** | 환경 커스텀 자유 | 설치 필요 |
| **GitHub Codespaces** | 브라우저에서 VSCode | 월 60시간 무료 |

### Colab 사용 시 주의사항

```python
# 1. API Key는 Colab Secrets 사용 (노출 방지)
from google.colab import userdata
OPENAI_API_KEY = userdata.get('OPENAI_API_KEY')

# 2. 대용량 모델은 GPU 런타임 필요
# Runtime > Change runtime type > GPU

# 3. 세션 종료 시 설치된 패키지 초기화됨
# 매번 !pip install 필요
```

---

## 준비물

### 발표자
- [ ] 4개 도구 로컬 실행 테스트 완료
- [ ] 데모용 논문 PDF + 초록 txt
- [ ] OpenAI API key
- [ ] Colab 노트북 배포 확인

### 참가자
- [ ] Google 계정 (Colab 접속용)
- [ ] 본인 연구 주제 또는 논문 초안
- [ ] (선택) OpenAI API key - 없으면 발표자 key 공유

---

## API Key 신청 링크

| API | 링크 | 비용 | 비고 |
|-----|------|------|------|
| **Gemini** | [aistudio.google.com](https://aistudio.google.com/apikey) | 무료 | LLM용 |
| **Semantic Scholar** | [semanticscholar.org/product/api](https://www.semanticscholar.org/product/api) | 무료 | rate limit 완화 |
| **GitHub** | [github.com/settings/tokens](https://github.com/settings/tokens) | 무료 | 60→5000 req/hr |
| **OpenAlex** | 불필요 | 무료 | polite pool: 이메일만 |
| **PubMed** | 불필요 | 무료 | 무제한 |
| **arXiv** | 불필요 | 무료 | 무제한 |
| **OSF** | 불필요 | 무료 | 무제한 |

---

## 참고 자료

### 오늘 다루는 프로젝트
- [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) - arXiv 검색, 5.2k stars
- [PaSa](https://github.com/bytedance/pasa) - arXiv + Scholar, ByteDance
- [LitLLM](https://github.com/ServiceNow/litllm) - Related Work 생성, TMLR 2024
- [AgentReview](https://github.com/ahren09/agentreview) - Peer Review, EMNLP 2024

### 기타 오픈소스
- [GPT-Researcher](https://github.com/assafelovic/gpt-researcher) - 24.9k stars
- [AI-Scientist](https://github.com/SakanaAI/AI-Scientist) - 12k stars
- [PaperQA2](https://github.com/Future-House/paper-qa) - 8k stars

### API 문서
- [Semantic Scholar API](https://api.semanticscholar.org/)
- [OpenAI API](https://platform.openai.com/docs)

---

*Last updated: 2026-01-19*
