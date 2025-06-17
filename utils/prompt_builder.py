def build_risk_prompt(text: str) -> str:
    return f"""
You are a regulatory compliance expert. Analyze the SOP below for:

1. Non-compliant sections
2. Missing documentation
3. High-risk or vague clauses
4. Suggested fixes

Respond ONLY in **valid JSON** like this (no explanation):

{{
  "non_compliant_sections": ["..."],
  "missing_elements": ["..."],
  "high_risk_clauses": ["..."],
  "suggested_fixes": ["..."]
}}

SOP:
{text}
"""