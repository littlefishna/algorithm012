学习笔记
本周学习了二叉树的前，中， 后序遍历， 前序就是根节点先遍历，中序是根节点在左节点之后
遍历， 后序是根节点最后遍历。 运用递归写法，遍历的时间复杂度是O(n).
Binary seach tree: the value on the left child node is smaller than that on parent node and the ones on the right child node is larger than that on parent node. The time complexity of seaching, inserting, deleting of the binary seach tree should be O(logN)
Heap: Heap could be implemented by priority queue. 
Binary heap: Max heap or min heap. In python the package called "heapq" is the heap realization of the min heap. The implementation could be in an array. The left node is 2*i + 1 and the right node is 2*i +2 and the parent node is floor((i-1)/2).  
The time complexity to construct a heap should be O(nlogn). As for loop for each element is O(n) and the heapify costs O(logN). Then get the min/max should be O(1). Inserting should be O(1), Delete should be O(logN)
