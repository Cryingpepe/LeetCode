class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)

        # 결과 배열 미리 생성
        result = ['0'] * n
        carry = 0

        # 오른쪽부터 계산
        for i in range(n - 1, -1, -1):
            total = int(a[i]) + int(b[i]) + carry

            if total == 0:
                result[i] = '0'
                carry = 0
            elif total == 1:
                result[i] = '1'
                carry = 0
            elif total == 2:
                result[i] = '0'
                carry = 1
            else:  # total == 3
                result[i] = '1'
                carry = 1

        if carry == 1:
            result.insert(0, '1')

        return ''.join(result)