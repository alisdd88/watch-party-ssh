# 🎬 Terminal Watch Party

A fun and geeky way to **watch movies or shows with friends right from your terminal**. Instead of streaming video, this tool synchronizes **subtitles** across devices in real-time using **SSH or sockets**. Ideal for low-bandwidth setups or just terminal-loving friends who want to watch together from afar.

---

## 🔧 How It Works

- The **host loads a .srt subtitle file** and starts the session.
- A friend connects via **SSH** or the script syncs via **socket/TCP**.
- The subtitle text appears in both users' terminals, **synchronized**.
- Control playback using hotkeys: `play`, `pause`, `seek`, etc.
- Optional **chat overlay** lets you message during playback.
- (Optional) **System beep or sound effect** to mark subtitle cues.

- Host launches a tmux session and runs the script with a loaded **.srt** file.
- Remote user connects via **SSH** and attaches to the same **tmux session**.
- Both terminals share the same interface and controls.
- Subtitle playback is synced in real-time inside tmux.
- (Optional) chat window can be added using a split pane in tmux.

---

## 🧰 Tech Stack

| Component        | Tool/Library  |
|------------------|---------------|
| Language         | Python         |
| Subtitle Parsing | [`srt`](https://pypi.org/project/srt/) |
| Terminal UI      | `curses`       |
| Real-time Sync   | SSH + `tmux` shared session |
| Optional Audio   | `pyaudio`, `beep`, or `playsound` |

---

## 🗓️ Project Roadmap

- ✅ Planning & Setup
- 🔄 Subtitle Parsing & Timer System
- ⏯️ Playback & Sync Controls (Play, Pause, Seek)
- 🧪 Terminal UI Rendering
- 🌐 Real-time Synchronization Logic
- 💬 Optional Chat Overlay
- 🔔 Optional Audio Cues
- 📦 Packaging & CLI Options

---

## 🚀 Getting Started

```bash
git clone https://github.com/YOUR_USERNAME/terminal-watch-party.git
cd terminal-watch-party
python -m venv venv
source venv/bin/activate
pip install srt
