#!/bin/bash
# ===================================================================================
#  ملف: first_boot_setup.sh (سكربت الإعداد التلقائي)
# ===================================================================================

# ألوان للنصوص
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}====================================================================================${NC}"
echo -e "${BLUE}                    مرحباً بك في منصة بصيرة - Bassera Platform${NC}"
echo -e "${BLUE}                           سكربت الإعداد التلقائي${NC}"
echo -e "${BLUE}====================================================================================${NC}"
echo

# التحقق من وجود Python
echo -e "${YELLOW}[1/8]${NC} التحقق من وجود Python..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo -e "${GREEN}✓${NC} تم العثور على Python ${PYTHON_VERSION}"
else
    echo -e "${RED}✗${NC} Python غير مثبت. الرجاء تثبيت Python 3.8 أو أحدث."
    exit 1
fi
echo

# التحقق من وجود pip
echo -e "${YELLOW}[2/8]${NC} التحقق من وجود pip..."
if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}✓${NC} تم العثور على pip"
else
    echo -e "${RED}✗${NC} pip غير مثبت. الرجاء تثبيت pip."
    exit 1
fi
echo

# إنشاء البيئة الافتراضية
echo -e "${YELLOW}[3/8]${NC} إنشاء البيئة الافتراضية..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✓${NC} تم إنشاء البيئة الافتراضية"
else
    echo -e "${GREEN}✓${NC} البيئة الافتراضية موجودة بالفعل"
fi
echo

# تفعيل البيئة الافتراضية
echo -e "${YELLOW}[4/8]${NC} تفعيل البيئة الافتراضية..."
source venv/bin/activate
echo -e "${GREEN}✓${NC} تم تفعيل البيئة الافتراضية"
echo

# تحديث pip
echo -e "${YELLOW}[5/8]${NC} تحديث pip..."
pip install --upgrade pip
echo -e "${GREEN}✓${NC} تم تحديث pip"
echo

# تثبيت المتطلبات
echo -e "${YELLOW}[6/8]${NC} تثبيت المتطلبات من requirements.txt..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo -e "${GREEN}✓${NC} تم تثبيت جميع المتطلبات"
else
    echo -e "${RED}✗${NC} ملف requirements.txt غير موجود"
    exit 1
fi
echo

# إنشاء مجلدات المشروع
echo -e "${YELLOW}[7/8]${NC} إنشاء هيكل المجلدات..."
mkdir -p config
mkdir -p skills
mkdir -p logs
mkdir -p data
echo -e "${GREEN}✓${NC} تم إنشاء مجلدات المشروع"
echo

# إنشاء ملف التكوين الأساسي
echo -e "${YELLOW}[8/8]${NC} إنشاء ملف التكوين الأساسي..."
cat > config/bassera_config.yaml << EOF
# ملف التكوين الأساسي لمنصة بصيرة
general:
  name: "بصيرة"
  language: "ar"
  timezone: "Asia/Riyadh"
  
audio:
  microphone:
    device: "default"
    sample_rate: 16000
  speaker:
    device: "default"
    volume: 0.8
    
speech:
  recognition:
    engine: "vosk"  # أو "google" أو "sphinx"
    language: "ar-SA"
  synthesis:
    engine: "espeak"  # أو "gtts"
    language: "ar"
    voice: "ar+m3"
    
skills:
  auto_load: true
  skills_dir: "./skills"
  
logging:
  level: "INFO"
  file: "./logs/bassera.log"
EOF
echo -e "${GREEN}✓${NC} تم إنشاء ملف التكوين"
echo

echo -e "${GREEN}====================================================================================${NC}"
echo -e "${GREEN}                              تم الإعداد بنجاح!${NC}"
echo -e "${GREEN}====================================================================================${NC}"
echo
echo -e "${BLUE}الخطوات التالية:${NC}"
echo -e "1. تفعيل البيئة الافتراضية: ${YELLOW}source venv/bin/activate${NC}"
echo -e "2. تشغيل التطبيق: ${YELLOW}python start_basseera.py${NC}"
echo
echo -e "${BLUE}للحصول على مساعدة إضافية، راجع ملف README.md${NC}"
echo