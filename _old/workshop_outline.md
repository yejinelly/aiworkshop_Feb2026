# AI 문헌 리뷰 에이전트 워크샵

**SNU AI Psychology - February 2026**

---

## 워크샵 구조 (총 90분 기준)

```
┌─────────────────────────────────────────────────────────────┐
│  Part 1: 시장 조사 (50분)                                    │
│  → 기존 Review Agent 도구 비교 분석                          │
├─────────────────────────────────────────────────────────────┤
│  Part 2: 실습 (30분)                                         │
│  → 모듈형 Literature Finder 데모                             │
├─────────────────────────────────────────────────────────────┤
│  Part 3: 토론 (10분)                                         │
│  → 새로운 모듈 아이디어 브레인스토밍                          │
└─────────────────────────────────────────────────────────────┘
```

---

## Part 1: 시장의 Review Agent 도구들 (50분)

### 1.1 상용 도구 비교

| 도구 | 주요 기능 | 가격 | 장점 | 단점 |
|------|----------|------|------|------|
| **Elicit** | 논문 요약, 데이터 추출 | Freemium ($10/mo) | 질문 기반 검색 | 논문 수 제한 |
| **Consensus** | 과학적 합의 분석 | Free/$9.99 | Yes/No 답변 | 의학/과학 편중 |
| **Semantic Scholar** | 논문 검색, 인용 분석 | Free API | 대규모 DB, TLDR | 전문 분야 약함 |
| **ResearchRabbit** | 논문 네트워크 시각화 | Free | 관련 논문 발견 | 분석 기능 없음 |
| **Connected Papers** | 인용 그래프 | Free/Pro | 시각적 탐색 | 검색 기능 제한 |
| **Scite.ai** | 인용 맥락 분석 | $20/mo | Supporting/Contrasting | 비쌈 |
| **Litmaps** | 문헌 맵핑 | Freemium | Seed 기반 확장 | 느림 |
| **SciSpace (Typeset)** | PDF 읽기, 설명 | Freemium | Chat with PDF | 정확도 이슈 |
| **Perplexity** | 웹 + 학술 검색 | Free/$20 | 실시간 검색 | 인용 불완전 |

### 1.2 오픈소스 프로젝트

| 프로젝트 | GitHub Stars | 특징 |
|----------|--------------|------|
| **gpt-researcher** | 13k+ | 자율 리서치 에이전트 |
| **paper-qa** | 4k+ | PDF 기반 Q&A |
| **scholarcy** | - | 논문 요약 |
| **paperswithcode** | - | 코드 연결 논문 |
| **OpenScholar** | Allen AI | 오픈 학술 LLM |

### 1.3 데모 시연 (각 도구 3-5분)

1. **Elicit**: "What interventions reduce depression in adolescents?"
2. **Consensus**: "Does meditation improve anxiety?"
3. **ResearchRabbit**: 시드 논문에서 확장
4. **Connected Papers**: 인용 그래프 탐색

---

## Part 2: 모듈형 Literature Finder 실습 (30분)

### 2.1 데이터베이스 모듈

```
┌─────────────────────────────────────────────────────────────┐
│                    Literature Finder                         │
│                                                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │  PubMed  │ │  arXiv   │ │   OSF    │ │  GitHub  │        │
│  │  (Free)  │ │  (Free)  │ │  (Free)  │ │  (Free)  │        │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘        │
│       │            │            │            │               │
│       └────────────┴────────────┴────────────┘               │
│                         │                                    │
│                    ┌────▼────┐                               │
│                    │ Merger  │                               │
│                    │& Ranker │                               │
│                    └────┬────┘                               │
│                         │                                    │
│                    ┌────▼────┐                               │
│                    │ Output  │                               │
│                    └─────────┘                               │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 API Key 없이도 동작하는 구조

| 데이터베이스 | API Key 필요? | 무료 대안 |
|-------------|--------------|----------|
| **PubMed** | ❌ 불필요 | E-utilities (무제한) |
| **arXiv** | ❌ 불필요 | arXiv API (무제한) |
| **OSF** | ❌ 불필요 | OSF API (무제한) |
| **GitHub** | ⚠️ 권장 | 비인증 60req/hr |
| **Semantic Scholar** | ⚠️ 권장 | 비인증 100req/5min |
| **SciVal** | ✅ 필요 | 기관 구독 필요 |

### 2.3 Fallback 전략

```python
# API Key 우선순위 시스템
def get_search_results(query):
    results = []

    # Tier 1: 항상 무료 (API key 불필요)
    results += search_pubmed(query)      # 항상 동작
    results += search_arxiv(query)       # 항상 동작
    results += search_osf(query)         # 항상 동작

    # Tier 2: API key 있으면 사용
    if SEMANTIC_SCHOLAR_KEY:
        results += search_semantic_scholar(query)
    else:
        results += search_semantic_scholar_free(query)  # rate limited

    # Tier 3: 기관 접근 필요
    if SCIVAL_TOKEN:
        results += search_scival(query)
    # else: skip silently

    return deduplicate_and_rank(results)
```

### 2.4 모듈 교체 가능한 구조

```python
# 사용자가 원하는 모듈만 선택
pipeline = LiteraturePipeline([
    PubMedModule(),           # 의학/생명과학
    ArXivModule(),            # CS/물리/수학
    # OSFModule(),            # 사회과학 (선택)
    # GitHubModule(),         # 코드 검색 (선택)
    SemanticScholarModule(),  # 통합 검색
])

# 순서도 변경 가능
pipeline.reorder(['semantic_scholar', 'pubmed', 'arxiv'])

# 새 모듈 추가
pipeline.add(CustomModule())
```

---

## Part 3: 새로운 모듈 아이디어 (10분)

### 브레인스토밍 주제

1. **Citation Context Analyzer**
   - 인용이 supporting인지 contrasting인지 분석

2. **Method Extractor**
   - 논문에서 방법론만 추출/비교

3. **Gap Finder**
   - 문헌 간 연구 공백 자동 탐지

4. **Replication Checker**
   - 재현 연구 여부 확인

5. **Author Network**
   - 주요 연구자 네트워크 분석

6. **Trend Analyzer**
   - 키워드 시계열 트렌드

### 참가자 활동

- 3-4명씩 그룹
- 새로운 모듈 아이디어 1개 제안
- 구현 방법 간단히 스케치

---

## 기술 스택

### 필수 (설치됨)
```
google-generativeai  # LLM (Gemini)
requests            # API 호출
```

### 선택 (모듈별)
```
biopython           # PubMed
arxiv               # arXiv
osfclient           # OSF
PyGithub            # GitHub
semanticscholar     # Semantic Scholar
```

---

## 실습 노트북 구성

```
1_existing_tools_demo.ipynb     # Part 1: 기존 도구 실습
2_literature_finder.ipynb       # Part 2: 모듈형 검색기
3_module_template.ipynb         # Part 3: 새 모듈 만들기 템플릿
```

---

## 준비물 체크리스트

### 발표자
- [ ] Elicit 계정 (무료)
- [ ] Consensus 계정 (무료)
- [ ] ResearchRabbit 계정 (무료)
- [ ] Gemini API key
- [ ] 데모용 연구 질문 3개

### 참가자
- [ ] Google Colab 접속 가능
- [ ] (선택) Gemini API key
- [ ] (선택) 관심 연구 주제

---

*Last updated: 2026-01-17*
