
let bubbleArray = [64, 34, 25, 12, 22, 11, 90];

console.log("Original Array:", bubbleArray);
function bubbleSort(arr) {
    let n = arr.length;

        for (let i = 0; i < n - 1; i++) {

                for (let j = 0; j < n - i - 1; j++) {

                            if (arr[j] > arr[j + 1]) {
                                            let temp = arr[j];
     arr[j] = arr[j +1];              arr[j + 1] = temp;                                }
 }    
 console.log(`After Pass ${i + 1}:`, arr);        }

                                                                                                                return arr;
                                                                                                                }

                                                                                                                console.log("\nBubble Sort:");
                     bubbleSort([...bubbleArray]);

                                                                                                                // Insertion Sort
                                                                           let insertionArray = [64, 34, 25, 12, 22, 11, 90];

                                                                                                                function insertionSort(arr) {

                                                                                                                    for (let i = 1; i < arr.length; i++) {

                                                                                                                            let key = arr[i];
                                                                                                                                    let j = i - 1;

                                                                                                                                            while (j >= 0 && arr[j] > key) {
                                                                                                                                                        arr[j + 1] = arr[j];
                                                                                                                                                                    j--;
                                                                                                                                                                            }

                                                                                                                                                                                    arr[j + 1] = key;
                                                                                                                                                                                        }

                                                                                                                                                                                            return arr;
                                                                                                                                                                                            }

                                                                                                                                                                                            console.log("\nInsertion Sort:");
                                                                                                                                                                                            console.log("Sorted Array:", insertionSort(insertionArray));