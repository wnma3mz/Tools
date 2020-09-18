# coding: utf-8
import win32gui
hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(
            hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


def get_child_windows(parent):
    '''     
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),
                              hwndChildList)
    return hwndChildList


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if '查找/添加' in t:
        # print(h, t)
        clsname = win32gui.GetClassName(h)
        # 获取父句柄hwnd类名为clsname的子句柄
        left, top, right, bottom = win32gui.GetWindowRect(h)
        # hwnd1 = win32gui.FindWindowEx(h, None, clsname, None)
        print(left, top, right, bottom)
        break