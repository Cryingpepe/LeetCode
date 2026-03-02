class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer, Integer> hashmap = new HashMap<>();
        int result[] = new int[k];


        for (int i : nums){
            hashmap.put(i, hashmap.getOrDefault(i, 0) + 1);
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b) -> Integer.compare(hashmap.get(b), hashmap.get(a)));

        for(int key : hashmap.keySet()){
            maxHeap.add(key);
        }
        
        for(int i = 0; i < k; i++){
            result[i] = maxHeap.poll();
        }

        return result;
    }
}