from rouge_score import rouge_scorer

# 기준 텍스트와 생성된 요약 텍스트
reference_text = """
기획재정부 해석에 따르면, 국제조세조정법 제25조의 부과제척기간 특례는 상호합의 대상 세목에 한정되지 않습니다. 따라서:\n\n1. 상호합의 결과로 인한 후속처분 시 법인세뿐만 아니라 관련된 부가가치세도 경정 가능\n2. 일반적인 5년 부과제척기간이 경과했더라도, 상호합의 절차 종료일로부터 1년 이내라면 처분 가능\n3. 단, 해당 세액 조정이 상호합의 결과와 직접적인 연관성이 있어야 함
"""
generated_summary = "국제조세조정법 제25조의 부과제척기간 특례는 상호합의 대상 세목에 한정되지 않습니다. 따라서:\n\n1. 상호합의 결과로 인한 후속처분 시 법인세뿐만 아니라 관련된 부가가치세도 경정 가능\n2. 일반적인 5년 부과제척기간이 경과했더라도, 상호합의 절차 종료일로부터 1년 이내라면 처분 가능\n3. 단, 해당 세액 조정이 상호합의 결과와 직접적인 연관성이 있어야 함"

# ROUGE 점수 계산
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
scores = scorer.score(reference_text, generated_summary)

# 각 지표별 점수 출력
print(f"ROUGE-1: {scores['rouge1'].fmeasure:.4f}") #단어 단위
print(f"ROUGE-2: {scores['rouge2'].fmeasure:.4f}") #문장 단위 일치도
print(f"ROUGE-L: {scores['rougeL'].fmeasure:.4f}") #요약 연속성