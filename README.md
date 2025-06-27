# EduScan Somalia – Offline & Online Learning‑Risk App  



## 1  📘 Project Overview
**EduScan Somalia** is a smart offline-first desktop application built using **PyQt5**. It helps detect learning difficulties among Somali students by using a trained ML model.  

Designed for **teachers and parents**, it runs **offline** (as a `.exe` or `.py`) but also supports optional online sync. It includes risk prediction, educational resources, a parent tracker, and reporting tools — all tailored for the Somali education system.


## 2  🖥 How to Install & Run (Windows)

```bash
# 1. Clone or unzip the repository
git clone https://github.com/YourUser/eduscan-somalia.git
cd eduscan-somalia

# 2. Create a virtual environment and install dependencies
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 3. Run the app
python main.py
✅ Or run the packaged version (no setup required):
bash
Copy
Edit
dist\EduScan_Somalia.exe
⚠️ Keep the following files/folders in the same directory as the .exe or main.py:

app_images/

learning_difficulty_detector.pkl

3  🎯 Features Demo (Add These to Your Video)
#	Feature	Sample Data	Expected Output
1	Login as Teacher/Parent	teacher01 / 1234	Opens correct dashboard
2	Learning Risk Prediction	Math:94, Read:94, Write:91, Attendance:85, Behavior:2, Literacy:8	High Risk shown
3	Teacher Resources	Click PDF/Activity	Opens material
4	Parent Tracker	Add daily report	Saved offline
5	Risk History Report	Data points (30)	Table shown, Export to CSV works

📂 Put screenshots of each feature in /screenshots/ before submission.

4  🧪 Testing Strategies
✅ Basic Functionality: Normal user paths were tested.

✅ Edge Cases: Extreme inputs (0/100) for all scores.

✅ Offline Mode: Wi-Fi off → app still works.

✅ Multiple Systems: Tested on both low-end and high-end Windows machines.

✅ Speed: Prediction responses are always under 1 second.

See TEST_RESULTS.md for screenshots + details.

5  📊 Results Summary
🎯 ML Model worked with over 85% confidence.

💡 UI redesigned for accessibility and clarity.

🧩 Optional features (Google Forms, PDF resources, etc.) tested in beta.

❗ Online sync backend not yet deployed — saved for future work.

6  📅 Supervisor Checkpoints
✅ Offline version submitted early and approved.

✅ UI improvements accepted — changes merged.

⚠️ Syncing and mobile access marked as future work.

7  📌 Recommendations & Future Work
🔐 Add encryption for local student records.

🌍 Connect with Somali education NGOs for field use.

🔄 Improve model by gathering more local school data.

📱 Build Android version for easier teacher access.

8  🎥 Demo Video Outline (5 mins max)
Timestamp	What to Show
00:00 – 00:45	Launch App + Login
00:45 – 02:30	Run a prediction
02:30 – 03:15	Open resources section
03:15 – 04:00	Use parent tracker
04:00 – 05:00	Show history table + switch roles

🎞 Upload your video to Google Drive or YouTube and paste the link here.

9  📦 Submission Links
🔗 GitHub Repo: https://github.com/YourUser/eduscan-somalia

💾 Download App (.zip): https://github.com/YourUser/eduscan-somalia/releases

🔧 (Optional) Flask backend repo: [add if applicable]

© 2025 Guled Hassan – Final Year Project
