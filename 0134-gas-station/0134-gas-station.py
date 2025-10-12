class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if not gas or not cost:
            return -1
        
        totalGas = 0
        currentGas= 0
        start = 0

        for i in range(len(gas)):
            putGas = gas[i] - cost[i]
            totalGas += putGas
            currentGas += putGas

            if currentGas < 0:
                start = i + 1
                currentGas = 0

        if totalGas < 0:
            return -1
        else:
            return start