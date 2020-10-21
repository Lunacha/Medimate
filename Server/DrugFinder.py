from selenium import webdriver
import json
import re


class DrugFinder:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.chrome_options.add_argument('headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('lang=ko_KR')
        self.wait = None
        self.drug_index = 1

    def finder_execute(self):
        self.driver.get('http://www.health.kr/searchIdentity/search.asp')
        self.driver.implicitly_wait(3)

    def insert_text(self, front, back):
        self.driver.find_element_by_id('drug_print_front').send_keys('')
        self.driver.find_element_by_id('drug_print_back').send_keys('')
        self.driver.find_element_by_id('btn_idfysearch').click()
        self.driver.implicitly_wait(20)
        self.driver.execute_script('''line_selectBoxToggle('100','100줄 보기')''')
        self.driver.implicitly_wait(20)

    def crawl_info(self, page, row_size, drugs):
        table = self.driver.find_element_by_id("idfytotal0")

        for i in range(3,3+row_size):
            drug = dict()
            tableRow = table.find_element_by_xpath('''//*[@id="idfytotal0"]/tbody/tr['''+str(i)+"]")
            mark = tableRow.find_element_by_xpath('''//*[@id="idfytotal0"]/tbody/tr['''+str(i)+"]/td[2]")
            name = tableRow.find_element_by_xpath('''//*[@id="idfytotal0"]/tbody/tr[''' + str(i) + "]/td[7]")
            drug['mark'] = re.split(' / | /|/ ', mark.text)
            drug['name'] = re.split('\n', name.text.replace('\u3000', ' '))
            print(drug['name'])
            drug['id'] = self.drug_index
            drugs.append(drug)
            self.drug_index += 1
        if row_size == 100:
            self.driver.execute_script('''changePage('''+str(page)+")")
            self.driver.implicitly_wait(30)


if __name__ == '__main__':
    drugFinder = DrugFinder()
    drugFinder.finder_execute()
    drugFinder.insert_text('', '')
    drugDB = dict()
    drugInfo = list()
    for i in range(2, 237):
        if i == 236:
            drugFinder.crawl_info(i, 97, drugInfo)
        else:
            drugFinder.crawl_info(i, 100, drugInfo)

    drugDB['drugs'] = drugInfo

    with open('drugDB.json', 'w', encoding='UTF-8-sig') as outfile:
        outfile.write(json.dumps(drugDB,ensure_ascii=False))

