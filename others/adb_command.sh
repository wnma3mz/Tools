# 启动app
adb shell monkey -p package -c android.intent.category.LAUNCHER 1

# 强行关闭app
adb shell am force-stop package

# 查看当前运行的app
adb shell dumpsys window | grep mCurrentFocus

# 列出所有app
adb shell pm list package

# 手机屏幕状态
adb shell dumpsys window policy

# 拍照
adb shell input keyevent 27
# 电源键
adb shell input keyevent 26
# 返回健
adb shell input keyevent 4
# 传输手机文件到本地
adb pull /sdcard//DICM1.png .
# 截图
adb shell screencap -p /sdcard/xx.png
# 截图并发送至windows端
adb shell screencap -p /sdcard/screenshot.png; adb pull /sdcard/screenshot.png .
# 获取页面布局（比截图高效）
adb shell uiautomator dump /sdcard/1.xml; adb pull /sdcard/1.xml .
# 长按
adb shell input touchscreen swipe {} {} {} {} 2000
"""
# 使用多线程加快点击某点的速度
def run_adb_shell(num, index):
    for _ in range(num):
        os.system("adb shell tap 1016, 444")

def tap_screen():
    import threading
    for i in range(10):
        threading.Thread(target=run_adb_shell, args=(20000, i)).start()
        time.sleep(1)

"""
