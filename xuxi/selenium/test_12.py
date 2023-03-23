import time

from selenium import webdriver
import js2py


class Douyu(object):
    def __init__(self):
        self.url = 'https://www.douyu.com/directory/all'
        self.driver = webdriver.Chrome()

    def parse_data(self):
        room_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li/div')
        print(room_list)
        for room in room_list:
            temp = {}
            # time.sleep(3)
            temp['title'] = room.find_element_by_xpath('./a/div[2]/div[1]/h3').text
            temp['type'] = room.find_element_by_xpath('./a/div[2]/div[1]/span').text
            temp['owner'] = room.find_element_by_xpath('./a/div[2]/div[2]/h2').text
            temp['num'] = room.find_element_by_xpath('./a/div[2]/div[2]/span').text
            print(temp)


    def run(self):
        # url
        # driver
        # get
        self.driver.get(self.url)
        time.sleep(2)
        while True:
            #parse
            self.parse_data()
            try:
                el_next = self.driver.find_element_by_xpath('//*[@id="listAll"]/section[2]/div[2]/div/ul/li[9]/span')
                self.driver.execute_script('scrollTo(0,10000000)')
                el_next.click()
            except:
                break


if __name__ == '__main__':
    douyu = Douyu()
    douyu.run()
