# ===================================================================================
#  ملف: README.md (تم التحديث)
# ===================================================================================
# منصة بصيرة - Bassera Platform

## نظرة عامة
منصة بصيرة هي مساعد ذكي مبني على تقنية OVOS (Open Voice Operating System) يوفر واجهة صوتية تفاعلية باللغة العربية.

## المتطلبات
- Python 3.8 أو أحدث
- نظام تشغيل Linux/macOS/Windows
- ميكروفون ومكبرات صوت
- اتصال بالإنترنت (للتحديثات والخدمات السحابية)

## التثبيت والإعداد

### 1. إنشاء البيئة الافتراضية
```bash
python3 -m venv venv
source venv/bin/activate  # على Linux/macOS
# أو
venv\Scripts\activate     # على Windows
```

### 2. تثبيت المتطلبات
```bash
pip install -r requirements.txt
```

### 3. الإعداد الأولي
```bash
# تشغيل سكربت الإعداد التلقائي
bash first_boot_setup.sh
```

### 4. تشغيل التطبيق
```bash
python start_basseera.py
```

## الاستخدام

### تشغيل المساعد
1. تأكد من تفعيل البيئة الافتراضية
2. شغل الأمر: `python start_basseera.py`
3. انتظر حتى تظهر رسالة "يمكنك الآن التحدث إلى المساعد"
4. ابدأ بقول "مرحبا بصيرة" أو "Hey Bassera"

### إيقاف المساعد
- اضغط `Ctrl+C` لإيقاف جميع الخدمات بأمان

## الخدمات المتضمنة

- **ovos-messagebus**: نظام الرسائل الداخلي
- **ovos-audio**: معالجة الصوت والتشغيل
- **ovos-skills**: إدارة المهارات والقدرات
- **ovos-listener**: الاستماع والتعرف على الصوت

## المهارات المتاحة

- **الوقت والتاريخ**: "كم الساعة؟" - "ما هو التاريخ اليوم؟"
- **الطقس**: "كيف الطقس اليوم؟" - "ما هي درجة الحرارة؟"
- **الحسابات**: "احسب 15 زائد 25" - "ما هو جذر 64؟"
- **المعلومات العامة**: "من هو...؟" - "ما هي عاصمة...؟"
- **التحكم في النظام**: "أغلق الحاسوب" - "افتح متصفح الويب"

## استكشاف الأخطاء

### مشاكل شائعة

1. **خطأ: لم يتم العثور على الأمر**
   - تأكد من تثبيت جميع المتطلبات: `pip install -r requirements.txt`
   - تحقق من تفعيل البيئة الافتراضية

2. **مشاكل الصوت**
   - تحقق من اتصال الميكروفون ومكبرات الصوت
   - تأكد من صلاحيات الوصول للصوت

3. **بطء في الاستجابة**
   - تحقق من اتصال الإنترنت
   - أعد تشغيل الخدمات

### ملفات السجل
يمكن العثور على ملفات السجل في:
- `~/.local/share/ovos/logs/`
- `/tmp/ovos/logs/`

## التطوير والمساهمة

### إضافة مهارات جديدة
1. أنشئ مجلد جديد في `skills/`
2. اتبع هيكل المهارات المعياري لـ OVOS
3. اختبر المهارة محلياً
4. أرسل طلب دمج (Pull Request)

### هيكل المشروع
```
Bassera.App/
├── start_basseera.py     # الملف الرئيسي
├── requirements.txt      # المتطلبات
├── first_boot_setup.sh   # سكربت الإعداد
├── README.md             # هذا الملف
├── config/               # ملفات التكوين
├── skills/               # المهارات المخصصة
└── logs/                 # ملفات السجل
```

## الترخيص
هذا المشروع مرخص تحت رخصة MIT - راجع ملف LICENSE للتفاصيل.

## الدعم
للحصول على الدعم أو الإبلاغ عن مشاكل:
- افتح issue جديد في GitHub
- راسلنا على: support@bassera.ai
- انضم إلى مجتمعنا على Discord

## شكر وتقدير
- فريق OVOS لتطوير النظام الأساسي
- مجتمع المطورين العرب
- جميع المساهمين في المشروع

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
# اسم المستخدم الافتراضي في Raspberry Pi OS الحديث هو 'pi' أو الذي يتم إنشاؤه
# بواسطة Imager. سنفترض هنا أن اسم المستخدم هو 'gentle' كما في حالتك.
# إذا كنت تستخدم صورة نظام مختلفة، قم بتغيير هذا المتغير.
USERNAME="gentle"
APP_SOURCE_DIR="/boot/firmware/Basseera_App"
APP_DEST_DIR="/home/$USERNAME/Basseera_App"
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
    # check_venv() # لا نحتاج لهذا التحقق عند التشغيل كخدمة
    
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
            print(f"\032[92mSUCCESS:\033[0m جاري تشغيل خدمة: {service}")
            command_path = os.path.join(sys.prefix, 'bin', service)
            proc = subprocess.Popen([command_path])
            processes.append(proc)
            time.sleep(5)

        print("\n\033[92mSUCCESS:\033[0m كل خدمات منصة بصيرة تعمل الآن في الخلفية.")
        print("\033[93mINFO:\033[0m يمكنك الآن التحدث إلى المساعد.")
        print("\033[93mINFO:\033[0m اضغط Ctrl+C لإيقاف كل الخدمات بأمان.")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\033[91mINFO:\033[0m تم استلام أمر الإيقاف. جاري إغلاق كل الخدمات...")
        for proc in reversed(processes):
            proc.terminate()
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
