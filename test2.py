import urllib2
from bs4 import BeautifulSoup


def getSearchUrls(company_name="innoscripta"):
    '''
    Search for particular company name and get set of urls related to that company
    :param company_name: company name that needed to be searched
    :return: set of urls from the result
    '''

    search_url = 'https://www.bundesanzeiger.de/ebanzwww/wexsservlet?global_data.designmode=eb&genericsearch_param.fulltext=' \
           + company_name + '&genericsearch_param.part_id=&%28page.navid%3Dto_quicksearchlist%29=Suchen'

    page = urllib2.urlopen(search_url)
    soup = BeautifulSoup(page, "lxml")
    table_result = soup.findAll("table", {"summary" :"Trefferliste"})
    td_results = [a.find_all("td", {"class": "info"}) for a in table_result]

    if len(td_results) == 0:
        return

    available_links = []
    for p in td_results:
        for t in p:
            for a in t:
                result_url = 'https://www.bundesanzeiger.de/' + a['href']
                available_links.append(result_url)

    return available_links


def getCaptchaSource(url):
    '''
    Get URL of captcha image
    :param url: url for the page where captcha is located
    :return: image url for the captcha image
    '''

    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    captcha_result = soup.find_all("img", {"alt": "Captcha"})


links = getSearchUrls()
for link in links:
    getCaptchaSource(link)



