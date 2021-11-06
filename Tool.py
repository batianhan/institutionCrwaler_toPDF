import os, shutil
import time
from selenium import webdriver
from urllib.parse import quote

chrome_version = "v-77"
chrome_path = os.getcwd() + "/Application/" + chrome_version + "/chrome.exe"
chrome_driver_path = os.getcwd() + "/Application/" + chrome_version + "/chromedriver.exe"

# chrome_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
# chrome_driver_path =

# 打印信息时加上时间
def log_console(str):
    print('{} {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), str))

def chromeInit(savePath=os.getcwd(), flag=False):
    options=webdriver.ChromeOptions()
    options._binary_location= chrome_path
    options.add_argument("--disable-gpu")
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-extensions')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    if flag:
        options.add_argument('--headless')

    if savePath != '':
        prefs = {
            "profile.default_content_settings.popups": 0,
            "download.default_directory": savePath,
            "profile.default_content_settings": {'images': 2}}
        options.add_experimental_option("prefs", prefs)
    chrome=webdriver.Chrome(options=options, executable_path=chrome_driver_path)
    chrome.minimize_window()
    chrome.implicitly_wait(20)
    return chrome

# 将数组逐行写入txt
def write_arr(arr, file):
    f = open(file, 'w')
    f.write('\n'.join(arr))
    f.close()

# 逐行读取txt生成返回数组
def load_arr(file):
    arr = []
    f = open(file, 'r')
    text = f.read()
    arr = text.split('\n')
    return arr
    f.close()

# 获取最新文件（时间排序取最后）
def sort_fold(path):
    """排序文件"""
    dir_lists = os.listdir(path)
    dir_lists.sort(key=lambda fn: os.path.getmtime(path + '\\' + fn))
    if len(dir_lists) == 0:
        return '文件夹为空'
    else:
        return (dir_lists[-1])

# 移动文件，顺便改名
def movefile(src_file, dst_file):
    if not os.path.isfile(src_file):
        log_console("{} not exist!".format(src_file))
    else:
        dst_path,dst_fname=os.path.split(dst_file)     #分离文件名和路径
        if not os.path.exists(dst_path):   os.makedirs(dst_path)  #创建路径

        for fname in os.listdir(dst_path):  # 同名删除
            if fname == dst_fname: os.remove(dst_path + '\\' + fname)

        shutil.move(src_file, dst_file)         #移动文件
        # log_console("move {0} -> {1}".format(src_file, dst_file))

# 删除文件夹中的所有文件
def clean_fold(path):
    for i in os.listdir(path):              # os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file = path + "\\" + i              # 当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file) == True:    # os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file)
        else:
            clean_fold(file)

# 用js点击
def js_click(driver, element):
    driver.execute_script("arguments[0].click();", element)

# 循环点击，直到下载完成
def loop_click(temp_fold, element):
    element.click()
    time.sleep(0.1)     # 等待下载完成
    if len(os.listdir(temp_fold)) == 0:
        log_console('再点一次')
        loop_click(element)

def loop_js_click(driver, temp_fold, element):
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)       # 等待下载完成
    if len(os.listdir(temp_fold)) == 0:
        log_console('再点一次')
        loop_js_click(driver, element)
'''https://www.webofscience.com/wos/woscc/full-record/WOS:000347715900024?SID=8BpveVXfUipGJ9goxbD'''
'''https://www.webofscience.com/wos/woscc/full-record/WOS:000309621400001?SID=8BpveVXfUipGJ9goxbD'''
'''https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=15&SID=8BpveVXfUipGJ9goxbD&page=1&doc=2'''
'''https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=20&SID=8BpveVXfUipGJ9goxbD&page=1&doc=1&cacheurlFromRightClick=no'''
'''https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=20&SID=8BpveVXfUipGJ9goxbD&page=1&doc=2'''
'''https://access.clarivate.com/login?app=wos&detectSession=true&referrer=TARGET%3Dhttps%253A%252F%252Fwww.webofscience.com%252Fwos%253FIsProductCode%253DYes%2526Init%253DYes%2526DestParams%253D%25252Fwos%25252Fwoscc%25252Ffull-record%25252FWOS%25253A000410630000003%25253F%2526DestApp%253DWOSNX%2526Func%253DFrame%2526DestFail%253Dhttp%25253A%25252F%25252Fwww.webofknowledge.com%25253FDestApp%25253DCEL%252526DestParams%25253DUT%2525253DWOS%252525253A000410630000003%25252526customersID%2525253DInCites%25252526smartRedirect%2525253Dyes%25252526action%2525253Dretrieve%25252526mode%2525253DFullRecord%25252526product%2525253DCEL%252526SrcAuth%25253DInCites%252526SrcApp%25253DTSM_TEST%252526e%25253D8%2525252FPrbyXWRFoTI35TOGo%2525252BQaGUnjSJd5AwHznMqXaJD4e1vWQLpM0EBw%2525253D%2525253D%2526SrcApp%253DCR%2526SID%253D8BpveVXfUipGJ9goxbD%26SID%3D8BpveVXfUipGJ9goxbD%26detectSessionComplete%3Dtrue'''

'''https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=5&SID=5FO2l1lRX6Qk4DW2hMY&page=1&doc=1'''
'''https://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=17&SID=5FO2l1lRX6Qk4DW2hMY&page=1&doc=1'''

'''https://access.clarivate.com/login?app=wos&detectSession=true&referrer=TARGET%3Dhttps%253A%252F%252Fwww.webofscience.com%252Fwos%253FIsProductCode%253DYes%2526Init%253DYes%2526DestParams%253D%25252Fwos%25252Fwoscc%25252Ffull-record%25252FWOS%25253A000347715900024%25253F%2526DestApp%253DWOSNX%2526Func%253DFrame%2526DestFail%253Dhttp%25253A%25252F%25252Fwww.webofknowledge.com%25253FDestApp%25253DCEL%252526DestParams%25253DUT%2525253DWOS%252525253A000347715900024%25252526customersID%2525253DInCites%25252526smartRedirect%2525253Dyes%25252526action%2525253Dretrieve%25252526mode%2525253DFullRecord%25252526product%2525253DCEL%252526SrcAuth%25253DInCites%252526SrcApp%25253DTSM_TEST%252526e%25253D8%2525252FPrbyXWRFrSaB1Nt6XpLbHJvyxa5wGoLpoW%2525252Fo9L8XL2aniiZHw7gw%2525253D%2525253D%2526SrcApp%253DCR%2526SID%253D5FO2l1lRX6Qk4DW2hMY%26SID%3D5FO2l1lRX6Qk4DW2hMY%26detectSessionComplete%3Dtrue'''

''''http://apps.webofknowledge.com/InboundService.do?product=WOS&Func=Frame&DestFail=http%3A%2F%2Fwww.webofknowledge.com%3FDestParams%3DUT%253DWOS%25253A000359216600008%2526customersID%253DInCites%2526smartRedirect%253Dyes%2526action%253Dretrieve%2526mode%253DFullRecord%2526product%253DCEL%26SrcAuth%3DInCites%26SrcApp%3DTSM_TEST%26DestApp%3DCEL%26e%3DvwtjxiLuDPrhqkxGzMeEeDiukRHn%252FfEx%252FpT5qofj3%252Boj8KOdkGQGQA%253D%253D&SrcApp=TSM_TEST&SrcAuth=InCites&SID='+SID+'&customersID=InCites&smartRedirect=yes&mode=FullRecord&IsProductCode=Yes&Init=Yes&action=retrieve&UT=WOS%3A'+id'''

# new
'''https://www.webofscience.com/wos/woscc/full-record/WOS:000385285000008?SID=8BpveVXfUipGJ9goxbD'''
'''https://www.webofscience.com/wos/woscc/full-record/WOS:000304783300017?SID=8BpveVXfUipGJ9goxbD'''


# search DOI
'''https://apps.webofknowledge.com/Search.do?product=UA&SID=5FO2l1lRX6Qk4DW2hMY&search_mode=GeneralSearch&prID=5d5db8d9-3cc1-4c23-a494-9481c0c40470'''












def download(chrome, temp_fold, urls, dst_file):
    while True:
        try:
            log_console('访问此链接下载:{}'.format(urls))
            clean_fold(temp_fold)
            chrome.get(urls)
        except Exception:
            log_console("网络错误（下载失败）\n")
            time.sleep(60)
            continue

        try:
            # 等待下载完成 确保中间文件(.tmp .crdownload)完全转好
            while (len(os.listdir(temp_fold)) == 0
                   or os.listdir(temp_fold)[0].split('.')[-1] == 'tmp'
                   or os.listdir(temp_fold)[0].split('.')[-1] == 'crdownload'): time.sleep(0.1)

            movefile(temp_fold + '\\' + sort_fold(temp_fold), dst_file)
            time.sleep(0.1)  # 稍微控制时间，防止反爬
            break
        except:
            log_console('文件移动转换错误... 重新下载...\n')

# 用chrome.exe将本地html转pdf
# src_file, dst_file 须为绝对路径
def html2pdf(chrome_path, src_file, dst_file):
    chrome_path_filted = chrome_path.replace('(', '^(')\
        .replace(')', '^)')

    # 文件名里会有空格(cmd不能识别)，需要""
    src_file = r'"' + src_file + r'"'
    dst_file = r'"' + dst_file + r'"'

    cmd_str = chrome_path_filted + ' ' + '--headless --disable-gpu --print-to-pdf=' + dst_file + ' ' + src_file
    cmd_str = cmd_str.replace('/', '\\')
    os.system(cmd_str)
    log_console(cmd_str)

first_enter = True
def save_pdf(chrome, urls, dst_path, title, chrome_path=chrome_path):
    while True:
        try:
            log_console('访问此链接下载html:{}'.format(urls))
            chrome.get(urls)

            # 如果是第一次打开 web of science 链接 网页有些不必要的提示信息
            global first_enter
            if first_enter == True:
                time.sleep(0.5)
                chrome.get(urls)
                first_enter = False

            # chrome.execute_script('document.title = "test"; window.print()')

            text = chrome.page_source
            break
        except Exception:
            log_console("网络错误（下载失败）\n")
            time.sleep(60)
            continue
    title = title[:30]  # 防止文件名过长，就30够了
    with open(dst_path + title + '.html', 'w', encoding='utf-8') as f:
        log_console(dst_path + title + '.html')
        f.write('<head><meta charset="UTF-8"></head>' + text)
    time.sleep(0.5)     # 防反爬

    html2pdf(chrome_path, dst_path + title + '.html', dst_path + title + '.pdf')
