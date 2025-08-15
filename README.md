# ===================================================================================
#  ملف: README.md (تم التحديث والتحسين)
# ===================================================================================
# منصة بصيرة - Basseera Platform

##  نظرة عامة
منصة بصيرة هي مساعد ذكي قابل للتخصيص مبني على تقنية OVOS (Open Voice Operating System). تم تصميم هذا النموذج الأولي لعرض القدرات الأساسية للمنصة، مع التركيز على المهارات المتقدمة مثل التعرف على الوجوه.

## المتطلبات
- Raspberry Pi 5 أو كمبيوتر يعمل بنظام Linux.
- Python 3.9 أو أحدث.
- ميكروفون ومكبرات صوت (كاميرا ويب USB مع مايكروفون مدمج هي الخيار الأسهل).
- اتصال بالإنترنت.

---

## طريقة الإعداد (اختر طريقة واحدة فقط)

### الطريقة الأولى: الإعداد اليدوي (موصى به للمطورين)

اتبع هذه الخطوات لتثبيت التطبيق على نظام تشغيل موجود.

**1. استنساخ المشروع:**
```bash
git clone [https://github.com/ja4apk/basseera.app.git](https://github.com/ja4apk/basseera.app.git)
cd basseera.app
```

**2. إنشاء وتفعيل البيئة الافتراضية:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. تثبيت المتطلبات الأساسية للنظام:**
```bash
sudo apt-get update
sudo apt-get install -y build-essential cmake libopenblas-dev liblapack-dev libjpeg-dev
```

**4. تثبيت مكتبات البايثون:**
```bash
pip install -r requirements.txt
```

**5. تشغيل التطبيق:**
```bash
python start_basseera.py
```

---

### الطريقة الثانية: الإعداد التلقائي (للأجهزة الجديدة)

استخدم هذه الطريقة لتجهيز جهاز راسبيري باي جديد بالكامل تلقائياً عند أول تشغيل.

**1. تجهيز بطاقة الذاكرة:**
   - استخدم أداة Raspberry Pi Imager لحرق نسخة حديثة من `Raspberry Pi OS Lite (64-bit)`.
   - **لا تخرج البطاقة من الكمبيوتر.** افتح وحدة التخزين `bootfs`.

**2. نسخ الملفات:**
   - انسخ كل ملفات هذا المشروع إلى داخل `bootfs`.
   - أنشئ ملفاً فارغاً باسم `ssh` لتفعيل التحكم عن بعد.

**3. تفعيل سكربت التشغيل الأول:**
   - افتح ملف `cmdline.txt` الموجود داخل `bootfs`.
   - اذهب إلى نهاية السطر وأضف مسافة ثم الصق النص التالي:
     `systemd.run=/boot/firmware/first_boot_setup.sh systemd.run_success_action=reboot`

**4. التشغيل:**
   - أخرج البطاقة، ضعها في الراسبيري باي وشغّله. ستبدأ عملية التثبيت التلقائي (تستغرق 15-30 دقيقة) ثم سيعيد الجهاز التشغيل.

---

## الاستخدام

### تشغيل المساعد
1. تأكد من أنك داخل مجلد المشروع وأن البيئة الافتراضية مفعلة.
2. شغل الأمر: `python start_basseera.py`
3. انتظر حتى تظهر رسالة "يمكنك الآن التحدث إلى المساعد".
4. ابدأ بقول كلمة الاستيقاظ (Wake Word) الافتراضية "Hey Mycroft".

### إيقاف المساعد
- في نافذة الأوامر، اضغط `Ctrl+C` لإيقاف جميع الخدمات بأمان.

## المهارات المخصصة

- **التعرف على الوجوه**: "identify this person" - "run face recognition"

## استكشاف الأخطاء وإصلاحها

### مشاكل شائعة
- **خطأ: لم يتم العثور على الأمر:** تأكد من تفعيل البيئة الافتراضية (`source venv/bin/activate`).
- **مشاكل الصوت:** تحقق من أن النظام يتعرف على المايكروفون والسماعة باستخدام الأوامر `arecord -l` و `aplay -l`.

### ملفات السجل
يمكن العثور على ملفات السجل الرئيسية في: `~/.local/state/ovos/`

## هيكل المشروع
```
basseera.app/
├── start_basseera.py     # الملف الرئيسي للتشغيل
├── requirements.txt      # متطلبات البايثون
├── first_boot_setup.sh   # سكربت الإعداد التلقائي
├── README.md             # هذا الملف
└── skills/               # المهارات المخصصة
```

## الترخيص
هذا المشروع مرخص تحت رخصة MIT.

# ===================================================================================

# ===================================================================================
#  ملف: requirements.txt
# ===================================================================================
#
# ovos-core
# opencv-python
# face-recognition
# padatious
#
# ===================================================================================

# ===================================================================================
#  ملف: first_boot_setup.sh (سكربت الإعداد التلقائي)
# ===================================================================================
#!/bin/bash

# --- Configuration ---
USERNAME="ovos" # اسم المستخدم الافتراضي في صور OVOS Lite
APP_SOURCE_DIR="/boot/firmware/basseera.app"
APP_DEST_DIR="/home/$USERNAME/basseera.app"
VENV_DIR="$APP_DEST_DIR/venv"

echo "--- Starting Basseera First Boot Setup ---"

# انتظر حتى يتصل الجهاز بالإنترنت
echo "Waiting for network connection..."
while ! ping -c 1 -W 1 google.com &> /dev/null; do
    sleep 1
done
echo "Network is up."

# تحديث النظام وتثبيت الأدوات الأساسية
echo "Updating system and installing dependencies..."
apt-get update
apt-get upgrade -y
apt-get install -y build-essential cmake libopenblas-dev liblapack-dev libjpeg-dev python3-venv git

# نسخ مجلد التطبيق من قسم الإقلاع إلى المجلد الرئيسي للمستخدم
echo "Copying application files to home directory..."
cp -r "$APP_SOURCE_DIR" "$APP_DEST_DIR"
chown -R $USERNAME:$USERNAME "$APP_DEST_DIR"

# تنفيذ الأوامر الخاصة بالمستخدم (مثل إنشاء البيئة وتثبيت المكتبات)
echo "Setting up Python environment as user: $USERNAME"
su - $USERNAME -c "
    cd '$APP_DEST_DIR'

    echo 'Creating Python virtual environment...'
    python3 -m venv venv

    echo 'Activating environment and installing requirements...'
    source '$VENV_DIR/bin/activate'
    pip install --upgrade pip
    pip install -r requirements.txt
    deactivate
"

# إنشاء خدمة systemd لتشغيل التطبيق تلقائياً عند كل إقلاع
echo "Creating systemd service to run Basseera on boot..."
cat > /etc/systemd/system/basseera.service << EOL
[Unit]
Description=Basseera Smart Assistant Service
After=network-online.target

[Service]
Type=simple
User=$USERNAME
WorkingDirectory=$APP_DEST_DIR
ExecStart=$VENV_DIR/bin/python start_basseera.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
EOL

# تفعيل وبدء الخدمة
echo "Enabling and starting Basseera service..."
systemctl enable basseera.service
systemctl start basseera.service

echo "--- Basseera Setup Complete! The system will reboot shortly. ---"
# إعادة التشغيل تتم تلقائياً بواسطة الأمر الذي أضفناه في cmdline.txt

# ===================================================================================


# ===================================================================================
#  ملف: start_basseera.py (الكود الرئيسي لتشغيل التطبيق)
# ===================================================================================

import subprocess
import time
import sys
import os

def check_venv():
    """Checks if the script is running in a virtual environment."""
    if sys.prefix == sys.base_prefix:
        print("\033[91mخطأ: يجب تشغيل هذا السكربت داخل بيئة افتراضية.\033[0m")
        print("الرجاء تفعيل البيئة أولاً باستخدام الأمر:")
        print("\033[93msource venv/bin/activate\033[0m")
        sys.exit(1)

def main():
    """
    Main function to start and manage all OVOS services.
    """
    check_venv()
    
    print("\033[94mINFO:\033[0m بدء تشغيل خدمات منصة بصيرة...")
    
    # قائمة الخدمات التي يجب تشغيلها بالترتيب
    services = [
        "ovos-messagebus",
        "ovos-audio",
        "ovos-skills",
        "ovos-listener"
    ]
    
    processes = []

    try:
        # تشغيل كل خدمة كعملية منفصلة
        for service in services:
            print(f"\033[92mSUCCESS:\033[0m جاري تشغيل خدمة: {service}")
            command_path = os.path.join(sys.prefix, 'bin', service)
            proc = subprocess.Popen([command_path])
            processes.append(proc)
            time.sleep(5)  # انتظر 5 ثوانٍ بين كل خدمة لضمان استقرارها

        print("\n\033[92mSUCCESS:\033[0m كل خدمات منصة بصيرة تعمل الآن في الخلفية.")
        print("\033[93mINFO:\033[0m يمكنك الآن التحدث إلى المساعد.")
        print("\033[93mINFO:\033[0m اضغط Ctrl+C لإيقاف كل الخدمات بأمان.")

        # إبقاء السكربت يعمل لمراقبة العمليات
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\033[91mINFO:\033[0m تم استلام أمر الإيقاف. جاري إغلاق كل الخدمات...")
        for proc in reversed(processes):
            proc.terminate()
        # Wait for processes to terminate
        for proc in reversed(processes):
            proc.wait()
        print("\033[92mSUCCESS:\033[0m تم إيقاف كل الخدمات بنجاح.")
    except FileNotFoundError as e:
        print(f"\033[91mERROR:\033[0m لم يتم العثور على الأمر: {e.filename}. هل قمت بتثبيت المتطلبات من ملف requirements.txt؟")
    except Exception as e:
        print(f"\033[91mERROR:\033[0m حدث خطأ غير متوقع: {e}")
        for proc in processes:
            proc.terminate()

if __name__ == "__main__":
    main()
