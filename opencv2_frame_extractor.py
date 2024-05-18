import cv2
import os

# Function to extract frames
def extract_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return

    # Get the total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    frame_number = 0
    while True:
        # Read the next frame
        ret, frame = cap.read()

        # If the frame was not read successfully, break the loop
        if not ret:
            break

        # Save the frame as an image file
        frame_filename = os.path.join(output_folder, f"frame_{frame_number:04d}.png")
        cv2.imwrite(frame_filename, frame)

        frame_number += 1
        print(f"Extracted frame {frame_number}/{total_frames}")

    # Release the video capture object
    cap.release()
    print("Finished extracting frames.")

# Example usage
video_path = 'path_to_your_video.mp4'
output_folder = 'extracted_frames'
extract_frames(video_path, output_folder)
