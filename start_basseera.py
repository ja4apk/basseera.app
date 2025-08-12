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