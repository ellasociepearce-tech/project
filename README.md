# CISC 121 Final Project Ella Pearce: Playlist Vibe Builder  
## Playlist vibe builder is used to organize a list of songs by sorting them based on the user's input. This helps create a playlist based on a specific characteristic, making it more efficient for the user's vibe.  
## The algorithm I used is merge sort. Merge sort has a time complexity of O(nlog⁡n), making it great for organizing playlists large in size. It is also stable, so songs with the same value will keep their original order. 
## Demo (video/gif/screenshot of at least one run) 
## - Decomp: Take in a list of songs, user chooses a sorting key, divide the playlist into smaller sublists, recursively sort each sublist, merge the sorted sublists back together, output the final sorted playlist and display the steps.
## - Pattern recognition: Repeatedly split the list into halves until single elements remain, compare values when merging, the same process is used at every level of the recursion. 
## - Abstraction: Only the selected characteristic is used for sorting ignoring the other details, key steps like splitting and merging are shown while ignoring the rest of the details not involved in the process.
## - Algorithmic Thinking: Input: User provides a playlist and chooses a sorting key. Processing: Merge sort recursively splits and merges the playlist based on the chosen characteristic. Output: A sorted playlist is given to the user. GUI: Show the list is split into smaller parts and comparisons during merging, animate how elements move into their sorted positions, display the final ordered playlist. 
## flowchart: <img width="430" height="790" alt="image" src="https://github.com/user-attachments/assets/f53c1852-de95-4078-86ea-946eb1a77e72" />
## Steps to Run (local) + requirements.txt 
## Hugging Face Link 
## Testing (what you tried + edge cases) 
## Author & Acknowledgment (sources + AI use, if any) 
