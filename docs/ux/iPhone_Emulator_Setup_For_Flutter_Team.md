# 📱 iPhone Emulator Setup Instructions for Flutter (macOS)

Use this guide to install and configure the iPhone Simulator for Flutter development.

---

## NO NEED TO BE IN VENV FOR THIS TO RUN

## 🧱 1. Install System Prerequisites

### ✅ Install Xcode
- Download from Mac App Store: https://apps.apple.com/us/app/xcode/id497799835
- Or use terminal:
```bash
xcode-select --install
```

### ✅ Accept License & Set Xcode Path
```bash
sudo xcodebuild -license
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

---

## 💎 2. Install Ruby & CocoaPods

### ✅ Install Homebrew (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### ✅ Install Ruby via Homebrew
```bash
brew install ruby
```

### ✅ Update Shell Path
```bash
echo 'export PATH="/opt/homebrew/opt/ruby/bin:$PATH"' >> ~/.zshrc
echo 'export PATH="/opt/homebrew/lib/ruby/gems/3.4.0/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### ✅ Install CocoaPods
```bash
gem install cocoapods
pod setup
```

---

## 🐦 3. Setup Flutter iOS Project

### ✅ Navigate to your Flutter project directory
```bash
cd wellness_hub/ux
```

### ✅ If `ios/` folder is missing, add it:
```bash
flutter create .
```

### ✅ Make sure `pubspec.yaml` contains:
```yaml
version: 1.0.0+1
```

---

## 📱 4. Boot and Use iPhone Simulator

### ✅ List available simulators
```bash
xcrun simctl list devices
```

### ✅ Boot a device (example: iPhone 16 Pro)
```bash
xcrun simctl boot <device-id>
xcrun simctl boot D757C10C-0AB1-47D7-9445-1C7B4FAE3494
open -a Simulator
```

---

## 🚀 5. Run the Flutter App

### ✅ Run on simulator
```bash
flutter run -d <device-id>
```

Or if only one device:
```bash
flutter run
```

---

## 🧪 6. Verify Environment

### ✅ Run Flutter Doctor
```bash
flutter doctor -v
```

Ensure CocoaPods and iOS devices show ✅.

---