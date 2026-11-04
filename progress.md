# LeetCode Progress

## Current position (2026-11-04)

Cycle focus: Arrays & Hashing → Two Pointers (done-ish), then Sliding Window.
Trapping Rain Water was next but felt hard; refreshed Arrays & Hashing and Two Pointers after a break.
Next: confirm Max Difference fix → review 3Sum and Container With Most Water → retry Trapping Rain Water → Sliding Window.

Note: this file was seeded on 2026-11-04 from coach notes plus a repo scan. Exact dates of earlier attempts are unknown ("pre-11/04"). Levels for pre-seed problems are estimates; independent explanation of correctness/complexity hasn't been verified for most.

## Due for review

- Maximum Difference Between Increasing Elements: return-condition fix never confirmed
- 3Sum: needed multiple rounds of guided debugging
- Container With Most Water: not reviewed this cycle
- Top K Frequent Elements, Product of Array Except Self, Longest Consecutive Sequence: reached optimal with guidance

## Arrays & Hashing

| Problem | Pattern | Last attempt | How solved | Final complexity | Key mistake or missing insight | Level | Next review |
|---|---|---|---|---|---|---|---|
| Contains Duplicate | Hash set | pre-11/04 | independent | O(n) / O(n) | — | L4 | — |
| Valid Anagram | Frequency count | pre-11/04 | independent | O(n) / O(1) | — | L4 | — |
| Two Sum | Hash map complement | pre-11/04 | independent | O(n) / O(n) | — | L4 | — |
| Group Anagrams | Frequency signature as key | pre-11/04 | independent | O(n·k) / O(n·k) | — | L4 | — |
| Top K Frequent Elements | Heap → bucket sort | 2026-11-04 | hint (guided questions) | O(n) / O(n) | Didn't see size-k heap or bucket-by-frequency unaided | L3 | 2026-11-07 |
| Encode and Decode Strings | Length-prefix encoding | pre-11/04 | independent (after debugging) | O(n) / O(1) extra | Needed debugging passes | L4 | — |
| Product of Array Except Self | Prefix/suffix products | pre-11/04 | hint (guided to O(1) space) | O(n) / O(1) extra | Reusing output array for one pass | L3 | 2026-11-05 |
| Valid Sudoku | Hash sets per row/col/box | pre-11/04 | independent (box index fixed after feedback) | O(1) (fixed 9×9) | Box indexing | L3 | 2026-11-07 |
| Longest Consecutive Sequence | Set + sequence starts | pre-11/04 | hint 1 | O(n) / O(n) | Only start counting at sequence starts | L3 | 2026-11-05 |

## Two Pointers

| Problem | Pattern | Last attempt | How solved | Final complexity | Key mistake or missing insight | Level | Next review |
|---|---|---|---|---|---|---|---|
| Valid Palindrome | Converging pointers | pre-11/04 | independent | O(n) / O(1) | — | L4 | — |
| Two Sum II | Converging pointers on sorted | pre-11/04 | independent | O(n) / O(1) | — | L4 | — |
| Container With Most Water | Converging pointers, move shorter side | pre-cycle | unknown (prior exposure) | — | Not reviewed this cycle | L2? | due now |
| 3Sum | Sort + two pointers, skip duplicates | pre-11/04 | multiple rounds of guided debugging | O(n²) / O(1) extra | Duplicate handling / debugging | L2–L3 | due now |

## Bridge problems

| Problem | Pattern | Last attempt | How solved | Final complexity | Key mistake or missing insight | Level | Next review |
|---|---|---|---|---|---|---|---|
| Maximum Difference Between Increasing Elements | Running information | pre-11/04 | linear approach | O(n) / O(1) | Return-condition bug; fix unconfirmed | L3 | due now |
| Find Pivot Index | Prefix sum | pre-11/04 | independent, optimized to O(1) space | O(n) / O(1) | — | L4 | — |

## Prior exposure (not reviewed this cycle — not mastery)

Repo scan 2026-11-04: 41 problem directories, 165 submission files (145 .py, 20 .cpp).

- Sliding Window: buy-and-sell-crypto, longest-substring-without-duplicates, minimum-window-with-characters
- Stack: validate-parentheses, minimum-stack, evaluate-reverse-polish-notation, daily-temperatures
- Binary Search: binary-search, find-target-in-rotated-sorted-array
- Linked Lists: reverse-a-linked-list, merge-two-sorted-linked-lists, linked-list-cycle-detection, reorder-linked-list, remove-node-from-end-of-linked-list
- Trees: depth-of-binary-tree, same-binary-tree, level-order-traversal-of-binary-tree, valid-binary-search-tree, binary-tree-from-preorder-and-inorder-traversal
- Heaps: kth-largest-integer-in-a-stream
- Graphs: count-number-of-islands, clone-graph, rotting-fruit, course-schedule
- Intervals: insert-new-interval, non-overlapping-intervals
- Other: remove-element
