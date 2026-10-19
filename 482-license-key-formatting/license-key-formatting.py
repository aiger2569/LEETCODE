class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        clean_s = s.replace("-", "").upper()
        reversed_s = clean_s[::-1]
        chunks = [reversed_s[i:i+k] for i in range(0, len(reversed_s), k)]
        return "-".join(chunks)[::-1]
     