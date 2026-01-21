"""
샘플 ICLR 논문 4개 다운로드

demo.ipynb에서 사용하는 논문 ID: 39, 247, 289, 400
"""
import os
import json
import requests
import time
from pathlib import Path

# 샘플 논문 ID
SAMPLE_IDS = [39, 247, 289, 400]
CONFERENCE = "ICLR2024"
DATA_DIR = "data"

# 디렉토리 생성
paper_dir = Path(DATA_DIR) / CONFERENCE / "paper"
notes_dir = Path(DATA_DIR) / CONFERENCE / "notes"
accept_dir = notes_dir / "Accept"
reject_dir = notes_dir / "Reject"

for dir_path in [paper_dir, accept_dir, reject_dir]:
    dir_path.mkdir(parents=True, exist_ok=True)

print(f"📁 디렉토리 생성 완료")

# OpenReview API (인증 불필요)
def download_paper(paper_id, year=2024, retry=3, delay=10):
    """OpenReview에서 논문 다운로드"""

    # API로 메타데이터 가져오기
    api_url = f"https://api2.openreview.net/notes?invitation=ICLR.cc/{year}/Conference/-/Blind_Submission&number={paper_id}&details=all"

    for attempt in range(retry):
        try:
            print(f"  시도 {attempt + 1}/{retry}...", end=" ")
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            break  # 성공하면 루프 탈출
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:  # Rate limit
                if attempt < retry - 1:
                    wait_time = delay * (attempt + 1)  # 점진적 대기
                    print(f"Rate limit, {wait_time}초 대기...")
                    time.sleep(wait_time)
                else:
                    print(f"실패 (최대 재시도 초과)")
                    return None
            else:
                raise
        except Exception as e:
            print(f"❌ 오류 - {e}")
            return None

    try:

        if not data.get('notes'):
            print(f"⚠️  Paper {paper_id}: 메타데이터 없음")
            return None

        note = data['notes'][0]

        # PDF 다운로드
        pdf_url = f"https://openreview.net/pdf?id={note['id']}"
        pdf_path = paper_dir / f"{paper_id}.pdf"

        pdf_response = requests.get(pdf_url)
        if pdf_response.status_code == 200:
            with open(pdf_path, 'wb') as f:
                f.write(pdf_response.content)
            print(f"✅ Paper {paper_id}: PDF 다운로드 완료 ({len(pdf_response.content)} bytes)")
        else:
            print(f"⚠️  Paper {paper_id}: PDF 다운로드 실패 (status {pdf_response.status_code})")
            return None

        # 메타데이터 저장
        # decision 확인 (Accept/Reject)
        decision = note.get('content', {}).get('venueid', '')
        if 'poster' in decision.lower() or 'oral' in decision.lower():
            decision_folder = accept_dir
            decision_label = "Accept"
        else:
            decision_folder = reject_dir
            decision_label = "Reject"

        note_path = decision_folder / f"{paper_id}.json"
        with open(note_path, 'w', encoding='utf-8') as f:
            json.dump(note, f, indent=2, ensure_ascii=False)

        print(f"✅ Paper {paper_id}: 메타데이터 저장 완료 ({decision_label})")

        return decision_label

    except Exception as e:
        print(f"❌ Paper {paper_id}: 오류 - {e}")
        return None

# 논문 다운로드
print(f"\n📥 {len(SAMPLE_IDS)}개 논문 다운로드 시작...\n")

id2decision = {}
for i, paper_id in enumerate(SAMPLE_IDS):
    print(f"[{i+1}/{len(SAMPLE_IDS)}] Paper {paper_id}:")
    decision = download_paper(paper_id)
    if decision:
        id2decision[paper_id] = decision

    # 마지막 논문이 아니면 대기
    if i < len(SAMPLE_IDS) - 1:
        wait_time = 8
        print(f"  ⏳ {wait_time}초 대기 (rate limit 방지)...")
        time.sleep(wait_time)
    print()

# id2decision.json 생성
id2decision_path = Path(DATA_DIR) / CONFERENCE / "id2decision.json"
with open(id2decision_path, 'w') as f:
    json.dump(id2decision, f, indent=2)

# decision2ids.json 생성
decision2ids = {"Accept": [], "Reject": []}
for paper_id, decision in id2decision.items():
    decision2ids[decision].append(paper_id)

decision2ids_path = Path(DATA_DIR) / CONFERENCE / "decision2ids.json"
with open(decision2ids_path, 'w') as f:
    json.dump(decision2ids, f, indent=2)

print("="*60)
print("✅ 다운로드 완료!")
print(f"\n📊 결과:")
print(f"   - Accept: {len(decision2ids['Accept'])}개")
print(f"   - Reject: {len(decision2ids['Reject'])}개")
print(f"\n📁 저장 위치: {DATA_DIR}/{CONFERENCE}/")
