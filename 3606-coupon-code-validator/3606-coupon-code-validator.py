class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        
        e, g, p, r = [], [], [], []

        for i in range(len(code)):
            if not isActive[i]:
                continue

            Line = businessLine[i]
            if Line not in ("electronics", "grocery", "pharmacy", "restaurant"):
                continue

            if not code[i]:
                continue

            if not all(ch.isalnum() or ch == '_' for ch in code[i]):
                continue

            if Line.startswith("e"):
                e.append(code[i])
            if Line.startswith("g"):
                g.append(code[i])
            if Line.startswith("p"):
                p.append(code[i])
            if Line.startswith("r"):
                r.append(code[i])

        return sorted(e) + sorted(g) + sorted(p) + sorted(r)