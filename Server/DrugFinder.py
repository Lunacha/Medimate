from selenium import webdriver

class DrugFinder:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.chrome_options.add_argument('headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('lang=ko_KR')
        self.wait = None

    def FinderExecute(self):
        self.driver.get('http://www.health.kr/searchIdentity/search.asp')
        self.driver.implicitly_wait(3)

    def InsertText(self, front, back):
        self.driver.find_element_by_id('drug_print_front').send_keys('')
        self.driver.find_element_by_id('drug_print_back').send_keys('')
        self.driver.find_element_by_id('btn_idfysearch').click()
        self.driver.implicitly_wait(20)
        self.driver.execute_script('''line_selectBoxToggle('100','100줄 보기')''')
        self.driver.implicitly_wait(20)

    def CrawlInfo(self,page,row_size):
        table = self.driver.find_element_by_id("idfytotal0")
        tbody = table.find_element_by_tag_name("tbody")
        rows = tbody.find_elements_by_tag_name("tr")
        for i in range(3,3+row_size):
            tableRow = table.find_element_by_xpath('''//*[@id="idfytotal0"]/tbody/tr['''+str(i)+"]")
            mark = tableRow.find_element_by_xpath('''//*[@id="idfytotal0"]/tbody/tr['''+str(i)+"]/td[2]")
            name = tableRow.find_element_by_xpath('''//*[@id="idfytotal0"]/tbody/tr[''' + str(i) + "]/td[7]")
            print(mark.text)
        if row_size == 100:
            self.driver.execute_script('''changePage('''+str(page)+")")
            self.driver.implicitly_wait(30)




drugFinder = DrugFinder()
drugFinder.FinderExecute()
drugFinder.InsertText('','')
for i in range(2,237):
    if i == 236:
        drugFinder.CrawlInfo(i, 97)
    else
        drugFinder.CrawlInfo(i, 100)

