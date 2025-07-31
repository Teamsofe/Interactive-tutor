from gtts import gTTS

text = "Understanding Bubble Sort (The Gentle Way), Have you ever arranged your books from the tallest to the shortest by comparing two at a time and swapping where needed? That’s basically how Bubble Sort works! In Bubble Sort, we compare pairs of elements in a list and swap them if they are out of order. This process is repeated multiple times — each time pushing the next largest element to its correct position, like a bubble rising to the top."
tts = gTTS(text)
tts.save("audio_1.mp3")

text = "Ever arranged playing cards in your hand? You pick a card and insert it into the right place among the already sorted ones. That’s exactly how Insertion Sort works! It builds the final sorted array one item at a time by comparing each new element with those before it and inserting it into the correct position."
tts = gTTS(text)
tts.save("audio_2.mp3")

text = "Imagine looking for your favorite book on a shelf, one by one. You check each book until you find it. This is exactly how Linear Search works! It checks each element in a list until the target is found or all elements have been searched. Line-by-Line Explanation: We start from the beginning of the list. Check each item to see if it matches the target. If a match is found, return the index. If no match is found after checking all items, return Not Found."
tts = gTTS(text)
tts.save("audio_3.mp3")

text = "Imagine you are searching for a word in a dictionary. Instead of starting from the beginning, you open the middle and decide to go left or right. That’s how Binary Search works! Binary Search is a highly efficient algorithm that finds the target value by repeatedly dividing the search interval in half. Line-by-Line Explanation: Start with the entire sorted list; Find the middle element; If it matches the target, return it; If it's smaller, search the right half; if larger, search the left half. More Insights: Why Binary? The search space is halved in each step, hence the name; Efficiency: Time complexity is O(log n); Best Use: Large sorted datasets."
tts = gTTS(text)
tts.save("audio_4.mp3")

text = "Recursion is a powerful concept in programming where a function calls itself to solve smaller parts of a bigger problem. Let's understand this using a simple mathematical example: calculating the factorial of a number (n!). For instance, 5! = 5 × 4 × 3 × 2 × 1. Line-by-Line Explanation: We define a function that takes an integer n; If n is 0 or 1, we return 1 (this is our base case); Otherwise, we return n * factorial(n - 1), which keeps calling itself with smaller values; This continues until it reaches the base case. More Insights: Why Recursion? It simplifies problems that can be broken into similar sub-problems; Efficiency: Can be less efficient without optimizations (like memoization); Best Use: Tree traversals, combinatorics, divide-and-conquer problems."
tts = gTTS(text)
tts.save("audio_5.mp3")