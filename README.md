# 🖌️ AI Virtual Painter

An interactive computer vision project that allows users to draw on the screen using **hand gestures** — no mouse or stylus required!

---

## 🧠 How It Works

1. **Hand Detection**: Uses MediaPipe to detect 21 hand landmarks from the webcam feed.
2. **Gesture Control**:
   - **Two fingers up** → Color selection mode.
   - **One finger up** → Drawing mode.
   - **All fingers up** → Clear the canvas.
3. **Drawing Logic**: Tracks the index finger position and draws lines based on movement.
4. **Canvas Merging**: Uses masking and bitwise operations to combine canvas and live video.
5. **Header Control**: Displays a top banner to choose colors/tools based on finger position.

---

## 🛠️ Tech Stack

- **Language**: Python
- **Libraries**:
  - `OpenCV` – for image processing & camera access
  - `MediaPipe` – for hand tracking and landmarks
  - `NumPy` – for image operations


