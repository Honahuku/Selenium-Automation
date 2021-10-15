import pytest
import time
import json
import subprocess
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_profile = webdriver.FirefoxProfile() #firefox用のSelenium webdriver
firefox_profile.set_preference("browser.privatebrowsing.autostart", True) #シークレットブラウザ用プロファイル、chromeの場合は方法が異なる

driver = webdriver.Firefox(firefox_profile=firefox_profile) #webdriverの指定

# 1 | open | 該当ページを開く
driver.get("https://example.com/")
# 2 | setWindowSize | 550x692 | ブラウザの解像度を指定
driver.set_window_size(550, 692)
# 3 | waitForElementVisible | id=i0116 | 30000 | メールアドレス入力フォームがアクティブになるまで待機
WebDriverWait(driver, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "i0116")))
# 4 | click | id=i0116 | メールアドレス入力フォームをクリック
driver.find_element(By.ID, "i0116").click()
# 5 | type | id=i0116 | hoge@piyo.co.jp　メールアドレスを入力
driver.find_element(By.ID, "i0116").send_keys("hoge@piyo.co.jp")
# 6 | click | id=idSIButton9 | 次へを押下
driver.find_element(By.ID, "idSIButton9").click()
# 7 | waitForElementVisible | id=i0118 | 30000 パスワードが入力できるようになるまで待機
WebDriverWait(driver, 30000).until(expected_conditions.visibility_of_element_located((By.ID, "i0118")))
# 8 | click | id=i0118 | パスワード入力フォームをクリックしてカーソルを合わせる
driver.find_element(By.ID, "i0118").click()
# 9 | type | id=i0118 | passwd | パスワードを入力
driver.find_element(By.ID, "i0118").send_keys("passwd")
# 10 | click | id=idSIButton9 | "サインイン"をクリック
driver.find_element(By.ID, "idSIButton9").click()
# 11 | waitForElementVisible | id=idTxtBx_SAOTCC_OTC | 300000 | 
WebDriverWait(driver, 300000).until(expected_conditions.visibility_of_element_located((By.ID, "idTxtBx_SAOTCC_OTC")))
# 12 | click | id=idTxtBx_SAOTCC_OTC | 2FAコードの入力画面への遷移待ち
driver.find_element(By.ID, "idTxtBx_SAOTCC_OTC").click()
#subprocessコマンドでホストOSのコマンドを実行する
#ここではoathtoolコマンドで2FAの秘密鍵からコードを生成し、変数resultへ格納する
result = subprocess.run(["oathtool", "--totp", "private_key", "--base32"],stdout=subprocess.PIPE)
print(result.stdout.decode("utf-8"))
#生成した値に文字列操作し入力可能な形にし、変数numberへ格納する
number = result.stdout.decode("utf-8")
# 13 | type | id=idTxtBx_SAOTCC_OTC | 2FAコードの入力
driver.find_element(By.ID, "idTxtBx_SAOTCC_OTC").send_keys(number)
# 14 | waitForElementVisible | id=idSubmit_SAOTCC_Continue | 300000 | ボタンがアクティブになるまで待機
WebDriverWait(driver, 300000).until(expected_conditions.visibility_of_element_located((By.ID, "idSubmit_SAOTCC_Continue")))
# 15 | click | id=idSubmit_SAOTCC_Continue | "検証"ボタンをクリック
driver.find_element(By.ID, "idSubmit_SAOTCC_Continue").click()
# 16 | waitForElementVisible | id=idSIButton9 | 300000 | "サインインの状態を維持しますか?"への遷移待ち
WebDriverWait(driver, 300000).until(expected_conditions.visibility_of_element_located((By.ID, "idSIButton9")))
# 17 | click | id=idSIButton9 | "いいえ"をクリックする。今回はシークレットウィンドウで開いているためこのログイン画面は毎回表示される。よって"はい"を選択した場合でも問題ない。
driver.find_element(By.ID, "idSIButton9").click()
#ログイン処理ここまで
# 18 | waitForElementVisible | id=SelectId_0_placeholder | 300000 | ページが読み込まれ次の要素が有効になるまで待機
WebDriverWait(driver, 300000).until(expected_conditions.visibility_of_element_located((By.ID, "SelectId_0_placeholder")))
# 19 | click | id=SelectId_0_placeholder | 体温をクリックし一覧表示にする
driver.find_element(By.ID, "SelectId_0_placeholder").click()
# 20 | waitForElementVisible | css=.select-option-nocheck:nth-child(15) | 300000 | ボタンがアクティブになるまで待機
WebDriverWait(driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".select-option-nocheck:nth-child(15)")))

#ランダム化処理。pythonのrandom関数を用いて毎回異なる値を入力する
i=random.randint(356,366) #変数iに356から366の間で乱数を生成した結果を格納する
print(i) #コンソールにiを表示
if i == 356:
    #変数iが356の場合、対応する要素"35.6"を選択する。以下36.6まで同様
    #356
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(7)").click()
elif i == 357:
    #357
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(8)").click()
elif i == 358:
    #358
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(9)").click()
elif i == 359:
    #359
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(10)").click()
elif i == 360:
    #360
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(11)").click()
elif i == 361:
    #361
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(12)").click()
elif i == 362:
    #362
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(13)").click()
elif i == 363:
    #363
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(14)").click()
elif i == 364:
    # 21 | click | css=.select-option-nocheck:nth-child(15) | 
    #364
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(15)").click()
elif i == 365:
    #365
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(16)").click()
elif i == 366:
    #366
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(17)").click()
else:
    #363
    driver.find_element(By.CSS_SELECTOR, ".select-option-nocheck:nth-child(14)").click()

# 22 | waitForElementVisible | css=.office-form-bottom-button > .button-content | 300000 | ボタンがアクティブになるまで待機
WebDriverWait(driver, 300000).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".office-form-bottom-button > .button-content")))
# 23 | click | css=.office-form-bottom-button > .button-content | "送信"をクリック
driver.find_element(By.CSS_SELECTOR, ".office-form-bottom-button > .button-content").click()
#pythonのtime関数を用いて2秒待機
time.sleep(2)
# 25 | close |  | ブラウザを終了
driver.close()
command = ["sudo", "shutdown", "-h", "now"] #subprocess.callで利用するため変数commandに実行したいコマンドを格納する
#subprocess.call(command) #シャットダウンコマンド。AWSの設定でシャットダウン後に自動で終了する設定ならば追加の課金を抑えることができる
