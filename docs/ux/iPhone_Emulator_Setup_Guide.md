# 📱 iPhone Simulator Setup Guide for Flutter Teams (macOS)

This guide walks you through setting up an iPhone emulator for Flutter development on macOS.

---

## NO NEED TO BE IN VENV FOR THIS TO RUN

## ✅ Prerequisites

1. **Install Flutter SDK**  
   Follow: https://docs.flutter.dev/get-started/install/macos  
   Ensure `flutter` is available in terminal:
   ```bash
   flutter doctor
   ```

2. **Install Xcode from Mac App Store**  
   Link: https://apps.apple.com/us/app/xcode/id497799835  
   Once installed:
   ```bash
   sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
   sudo xcodebuild -license
   ```

---

## 🧰 Install Ruby & CocoaPods (iOS Dependency Manager)

1. **Install Ruby (if not already)**  
   ```bash
   brew install ruby
   ```

2. **Add Ruby to PATH**
   ```bash
   echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
   echo 'export PATH="/opt/homebrew/lib/ruby/gems/3.4.0/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

3. **Install CocoaPods**
   ```bash
   gem install cocoapods
   pod setup
   ```

---

## 📱 Launch iPhone Simulator

1. **List Available Devices**
   ```bash
   xcrun simctl list devices
   ```

2. **Boot a Simulator (e.g., iPhone 16 Pro)**
   ```bash
   xcrun simctl boot <device-UDID>
   open -a Simulator
   ```

3. **Verify Device is Detected**
   ```bash
   flutter devices
   ```

---

## 🚀 Run Flutter App on Simulator

1. **Navigate to Your Flutter Project**
   ```bash
   cd your_flutter_project
   ```

2. **Ensure iOS support exists (optional)**
   ```bash
   flutter create .
   ```

3. **Run on Simulator**
   ```bash
   flutter run
   ```

---

## 🛠 Fix Warnings

To fix App Store build warnings, update your `pubspec.yaml`:
```yaml
version: 1.0.0+1
```

---

## ✅ Final Check

Run:
```bash
flutter doctor -v
```
Ensure all checks are ✅, especially for:
- Xcode
- CocoaPods
- Connected Devices

---

Team members can now build, test, and debug iOS apps using the simulator.