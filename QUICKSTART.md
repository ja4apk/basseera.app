# دليل البدء السريع - Quick Start Guide

## التثبيت السريع

### 1. استنساخ المشروع
```bash
git clone https://github.com/bassera-platform/bassera-app.git
cd bassera-app
```

### 2. الإعداد التلقائي
```bash
# على Linux/macOS
bash first_boot_setup.sh

# على Windows
# قم بتشغيل الأوامر يدوياً:
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. التشغيل
```bash
# تفعيل البيئة الافتراضية
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# تشغيل المساعد
python start_basseera.py
```

## الأوامر الصوتية الأساسية

### تفعيل المساعد
- "مرحبا بصيرة"
- "Hey Bassera"
- "بصيرة"

### الوقت والتاريخ
- "كم الساعة؟"
- "ما هو التاريخ اليوم؟"
- "أخبرني الوقت"

### الحسابات
- "احسب خمسة زائد ثلاثة"
- "كم يساوي عشرة ضرب اثنين؟"
- "ما هو جذر ستة عشر؟"

### المعلومات العامة
- "من هو الملك سلمان؟"
- "ما هي عاصمة فرنسا؟"
- "أخبرني عن الذكاء الاصطناعي"

### التحكم في النظام
- "أغلق الحاسوب"
- "افتح متصفح الويب"
- "ما هو إصدار النظام؟"

## إعداد سريع للتطوير

### إضافة مهارة جديدة
1. أنشئ ملف في مجلد `skills/`:
```python
# skills/my_skill.py
from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler

class MySkill(OVOSSkill):
    @intent_handler('my.custom.intent')
    def handle_my_intent(self, message):
        self.speak("مرحبا من مهارتي الجديدة!")

def create_skill():
    return MySkill()
```

2. أعد تشغيل المساعد

### تخصيص الإعدادات
عدّل ملف `config/bassera_config.yaml`:
```yaml
general:
  name: "اسم مساعدك"
  language: "ar"
  
audio:
  speaker:
    volume: 0.9  # مستوى الصوت
```

## استكشاف الأخطاء السريع

### المساعد لا يستجيب
```bash
# تحقق من الخدمات
ps aux | grep ovos

# أعد تشغيل المساعد
python start_basseera.py
```

### مشاكل الصوت
```bash
# تحقق من الأجهزة الصوتية
python -c "import sounddevice; print(sounddevice.query_devices())"

# اختبار الميكروفون
python -c "import speech_recognition as sr; r = sr.Recognizer(); print('يعمل!' if r else 'لا يعمل')"
```

### مشاكل التثبيت
```bash
# تحديث pip
pip install --upgrade pip

# إعادة تثبيت المتطلبات
pip install -r requirements.txt --force-reinstall
```

## الملفات المهمة

- `start_basseera.py` - الملف الرئيسي
- `config/bassera_config.yaml` - الإعدادات
- `skills/` - المهارات المخصصة
- `logs/` - ملفات السجل
- `requirements.txt` - المتطلبات

## روابط مفيدة

- [التوثيق الكامل](README.md)
- [سجل التغييرات](CHANGELOG.md)
- [مجتمع OVOS](https://openvoiceos.com/)
- [الدعم الفني](https://github.com/bassera-platform/bassera-app/issues)

## نصائح سريعة

1. **استخدم البيئة الافتراضية دائماً**
2. **تحقق من ملفات السجل عند حدوث مشاكل**
3. **اختبر الميكروفون قبل التشغيل**
4. **حافظ على تحديث المتطلبات**
5. **اقرأ رسائل الخطأ بعناية**

---

**مرحباً بك في منصة بصيرة! 🎉**

للمساعدة: [support@bassera.ai](mailto:support@bassera.ai)