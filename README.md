# AI 문헌 리뷰 에이전트 워크샵

**SNU AI Psychology - February 2026**

---

## 준비물

| 준비물 | 링크 | 필수 |
|--------|------|:----:|
| **Gemini API Key** | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | ✅ |
| **Semantic Scholar API Key** | [semanticscholar.org/product/api](https://www.semanticscholar.org/product/api) | ✅ |
| **OpenAI API Key** (Part 3용) | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) | 선택 |
| 본인 연구 주제 또는 논문 초안 | - | 권장 |

---

## 워크샵 개요

| Part | 내용 | 노트북 | Colab |
|------|------|--------|-------|
| **1** | 학술 API 개관 (Semantic Scholar, arXiv, PubMed) | `1_overview.ipynb` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yejinelly/aiworkshop_Feb2026/blob/master/notebooks/1_overview.ipynb) |
| **2** | Citation Crawler + SPECTER2 Selector | `2_crawlers_and_selector.ipynb` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yejinelly/aiworkshop_Feb2026/blob/master/notebooks/2_crawlers_and_selector.ipynb) |
| **2.5** | AI 리뷰용 샘플 논문 준비 | `2.5_manuscript_preparation.ipynb` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yejinelly/aiworkshop_Feb2026/blob/master/notebooks/2.5_manuscript_preparation.ipynb) |
| **3** | AI Paper Review Agent | `3_paper_review_agent.ipynb` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yejinelly/aiworkshop_Feb2026/blob/master/notebooks/3_paper_review_agent.ipynb) |
| **4** | Few-shot vs Agentic 리뷰 비교 | `4_review_comparison.ipynb` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yejinelly/aiworkshop_Feb2026/blob/master/notebooks/4_review_comparison.ipynb) |

```
1. Overview   → 학술 API로 논문 검색
       ↓
2. Crawlers   → Citation 네트워크 탐색 + SPECTER2 관련성 평가
       ↓
2.5 Manuscript → AI 리뷰용 샘플 논문 준비
       ↓
3. Review     → AI 논문 리뷰 받기 (agentic-paper-review)
       ↓
4. Comparison → Few-shot vs Agentic 비교 분석
```

---

## 발표 슬라이드

📊 [Canva 슬라이드 링크](https://www.canva.com/design/DAHAFFTL3Fk/Gfo_hFFn1J2Qh_SC_0Tr5Q/view?utm_content=DAHAFFTL3Fk&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h5d297b18ab)

---

## 파일 구조

```
aiworkshop_Feb2026/
├── notebooks/                          # 실습 노트북 (위 테이블 참조)
├── input/
│   ├── sample_method.md                # 샘플 Method (기후불안 연구)
│   └── human_reviews/                  # Transparent Peer Review 저장
└── outputs/                            # 실습 결과 저장
```

---

## Part 1: 학술 API 개관

| API | Key 필요 | 특징 |
|-----|----------|------|
| **Semantic Scholar** | 선택 (권장) | 인용 네트워크, 추천 기능 |
| **arXiv** | 불필요 | 프리프린트, CS/물리/수학 |
| **PubMed** | 불필요 | 의학/심리학 특화 |

---

## Part 2: Citation Crawler + Selector

| 도구 | 역할 |
|------|------|
| [paperscraper](https://github.com/jannisborn/paperscraper) | arXiv/PubMed 키워드 검색 |
| [Semantic Scholar API](https://api.semanticscholar.org/) | 인용/참조/추천 데이터 |
| [OpenAlex API](https://docs.openalex.org/) | 출판사 제한 없는 References |
| [SPECTER2](https://github.com/allenai/SPECTER2) | 논문 임베딩 → 관련성 점수 |

**Crawler 흐름**: paperscraper 검색 → 시드 선택 → References/Citations/Related 확장 → SPECTER2 필터링 → Top 10 추천

---

## Part 2.5: 논문 준비

| 옵션 | 현재 상태 | 생성 내용 |
|------|----------|----------|
| **A** | 완성된 초고 있음 | PDF/DOCX → MD 변환 |
| **B** | Method만 있음 | Intro + Results + Discussion 생성 |
| **C** | 논문 없음 | 전체 논문 생성 (영어) |

`input/sample_method.md`: 기후불안 청소년 종단연구 Method 예시 포함

---

## Part 3: AI Paper Review Agent

[agentic-paper-review](https://github.com/debashis1983/agentic-paper-review) - 9노드 LangGraph 워크플로우 (Spearman ρ = 0.74)

**평가 차원**: Soundness (1-4), Presentation (1-4), Contribution (1-4), Overall (1-10)

---

## Part 4: Few-shot vs Agentic 비교

| 항목 | Few-shot Reviewer | agentic-paper-review |
|------|-------------------|---------------------|
| 기반 | Transparent Peer Review 예시 | 9노드 워크플로우 |
| 모델 | gemini-2.5-flash | OpenAI API |
| 웹검색 | ❌ | ✅ |
| Few-shot 예시 | ✅ | ❌ |

**Transparent Peer Review 소스**: [Communications Psychology](https://www.nature.com/commspsychol/), [Nature Communications](https://www.nature.com/ncomms/), [OpenReview](https://openreview.net/)

---

## 결과 제출 & 공유

| Part | 제출 폼 | 결과 시트 |
|------|---------|----------|
| **2** | [Google Form](https://forms.gle/dYNbvMeeBMqxSmLa7) | [결과 보기](https://docs.google.com/spreadsheets/d/15jyTrqGY7Po5iLcXFrv_kwyUNkCC9YMX6kypPMs-bAc/edit?usp=sharing) |
| **3** | [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSfciPtMCZTSNyGvutdFGSdcUjKSdu98Vm7gVPe6TvVcGQKK2g/viewform) | [결과 보기](https://docs.google.com/spreadsheets/d/1wPGTOPGF5yvWQTimikr-rg2VExXiHCE0Xn2EVkffWfo/edit?usp=sharing) |
| **4** | [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSeYrzmXSEmoddzInY5j5xagy4cfa-MwolZYZYvm6_B7gXvnNQ/viewform) | [결과 보기](https://docs.google.com/spreadsheets/d/1v9ch3qRiGINOdf-bZkmrxxdt-QZKVQrDejvJ-1mxSbI/edit?gid=1333882645#gid=1333882645) |

---

## 참고 논문

- [PaSa: An LLM Agent for Comprehensive Academic Paper Search](https://arxiv.org/abs/2501.10120)
- [SPECTER2: SciRepEval: A Multi-Format Benchmark](https://arxiv.org/abs/2211.13308)
- [AgentReview: Exploring Peer Review Dynamics with LLM Agents](https://arxiv.org/abs/2406.12708)

---

*Last updated: 2026-01-29*
