import gradio as gr
import csv

#load the playlist 

def load_playlist_from_file(file):
    playlist = []

    try:
        with open(file.name, newline='') as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    if not row["title"] or not row["artist"] or not row["energy"] or not row["duration"]: #confirms all 4 sections are there
                        continue

                    energy = int(row["energy"]) #turning any values into numbers
                    duration = int(row["duration"])

                    if energy <= 0 or duration <= 0:
                        continue

                    playlist.append({
                        "title": row["title"],
                        "artist": row["artist"],
                        "energy": energy,
                        "duration": duration
                    })

                except:
                    continue

    except:
        return []

    return playlist


# Merge sort 

def merge_sort(arr, key, steps):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, steps)
    right = merge_sort(arr[mid:], key, steps)

    return merge(left, right, key, steps)


def merge(left, right, key, steps):
    merged = []
    i = j = 0
    #showing the steps 
    while i < len(left) and j < len(right):
        steps.append(f"Comparing {left[i]['title']} ({left[i][key]}) vs {right[j]['title']} ({right[j][key]})")

        if left[i][key] >= right[j][key]:
            merged.append(left[i])
            steps.append(f"Added {left[i]['title']}")
            i += 1
        else:
            merged.append(right[j])
            steps.append(f"Added {right[j]['title']}")
            j += 1

        steps.append(f"Current order: {[song['title'] for song in merged]}")

    while i < len(left):
        merged.append(left[i])
        steps.append(f"Added {left[i]['title']} (remaining)")
        i += 1

    while j < len(right):
        merged.append(right[j])
        steps.append(f"Added {right[j]['title']} (remaining)")
        j += 1

    return merged




def sort_playlist(file, key):
    key = key.lower().strip()     #makes sure the key is in the right format 
    if file is None:
        return "Please upload a CSV file."

    if key not in ["energy", "duration"]:
        return "Invalid selection."

    playlist = load_playlist_from_file(file)

    if not playlist:
        return "No valid songs found."

    steps = []
    sorted_playlist = merge_sort(playlist, key, steps)

    output = "---- SORTING STEPS ----\n\n"
    for step in steps:
        output += step + "\n"

    output += "\n---- FINAL PLAYLIST ----\n\n"
    for song in sorted_playlist:
        output += f"{song['title']} - {song['artist']} | Energy: {song['energy']} | Duration: {song['duration']}\n"

    return output
#Gradio UI
interface = gr.Interface(
    fn=sort_playlist,
    inputs=[
        gr.File(label="Upload CSV File"),
        gr.Textbox(label="Sort By (type 'energy' or 'duration')"),],
    outputs="text",
    title="Playlist Vibe Builder",
    description="Upload a CSV file and watch merge sort step-by-step.")

interface.launch()