
// 7_tree.js
// Time Complexity:
// Insertion: O(log n) average, O(n) worst case
// BFS: O(n)
// DFS (In-order): O(n)

class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    constructor() {
        this.root = null;
    }

    insert(value) {
        const newNode = new Node(value);

        if (this.root === null) {
            this.root = newNode;
            return;
        }

        let current = this.root;

        while (true) {

            if (value < current.value) {

                if (current.left === null) {
                    current.left = newNode;
                    return;
                }

                current = current.left;

            } else {

                if (current.right === null) {
                    current.right = newNode;
                    return;
                }

                current = current.right;

            }
        }
    }

    // Breadth-First Traversal
    bfs() {

        let queue = [];
        queue.push(this.root);

        console.log("Breadth-First Traversal:");

        while (queue.length > 0) {

            let current = queue.shift();
            process.stdout.write(current.value + " ");

            if (current.left) queue.push(current.left);
            if (current.right) queue.push(current.right);
        }

        console.log();
    }

    // Depth-First Traversal (In-order)
    inorder(node) {

        if (node !== null) {
            this.inorder(node.left);
            process.stdout.write(node.value + " ");
            this.inorder(node.right);
        }

    }
}

const tree = new BinaryTree();

// Insert at least 7 nodes
tree.insert(50);
tree.insert(30);
tree.insert(70);
tree.insert(20);
tree.insert(40);
tree.insert(60);
tree.insert(80);

tree.bfs();

console.log("Depth-First Traversal (In-order):");
tree.inorder(tree.root);
console.log();