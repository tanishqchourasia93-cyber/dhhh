import pyautogui
import pyperclip
import time

print("⏳ Waiting 2 seconds so you can switch to the target window...")
time.sleep(2)

# Step 1: Click the icon
print("👉 Clicking icon at (1180, 1054)...")
pyautogui.click(1180, 1054)
time.sleep(2)  # give app some time to open

# Step 2: Drag to select text
print("👉 Dragging from (777, 178) to (870, 978)...")
pyautogui.moveTo(777, 178)
pyautogui.dragTo(870, 978, duration=1, button='left')
time.sleep(0.5)

# Step 3: Copy selected text
print("👉 Pressing Ctrl+C to copy...")
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)

# Step 4: Get clipboard content
copied_text = pyperclip.paste()
print("✅ Copied Text:", copied_text if copied_text else "[Nothing copied!]")
