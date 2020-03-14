# -*- coding: utf-8 -*-
import scrapy
from ..items import FbmarketItem
from urllib.parse import urlencode
from urllib.parse import quote
from helper import functions


class FmarketSpider(scrapy.Spider):
    name = 'fmarket'
    allowed_domains = ['facebook.com']
    start_urls = ['https://m.facebook.com/marketplace']

    location = 'delhi'
    search_query = 'new girls jacket'
    radius_km = 1
    category = ''

    form_data = ''

    # query_parameter = {'query': search_query, 'radius_in_km': radius_km}

    def start_requests(self):
        if self.f_data:
            self.form_data = self.f_data
            self.form_data = self.form_data.split(',')
            self.location = self.form_data[0]
            self.category = self.form_data[1]
            self.search_query = self.form_data[2]
            self.radius_km = self.form_data[3]

        query_parameter = {'query': self.form_data[2], 'radius_in_km': self.form_data[3]}
        # ab_url = self.absolute_url(self.location, self.category, self.queryParameter)
        ab_url = self.absolute_url(self.form_data[0], self.form_data[1], query_parameter)
        print(self.form_data)

        yield scrapy.Request(url=ab_url, callback=self.parse)

    def parse(self, response):
        # print(response.body)
        # filename = response.url.split("/")[-1] + '.html'
        items = FbmarketItem()
        filename = 'fbwebpage1' + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        for product in response.css('div._a5o'):
            product_url = product.css("a::attr(href)").get()
            product_name = product.css('div:last-child::text').extract()
            product_price = product.css('a div:last-child span::text').extract()

            if product_price:
                product_price = self.rm_whilespace(product_price)

            if product_name:
                product_name = self.rm_whilespace(product_name)

            if product_url:
                product_url = response.urljoin(product_url)
                product_url = product_url.split('?')[0]
                product_url = product_url.replace('m.', '')

            if self.category:
                search_category = self.category.strip()
            else:
                search_category = 'NA'

            if self.location:
                search_loc = self.location.strip()
            else:
                search_loc = 'NA'

            if self.search_query:
                search_term = self.search_query.strip()
            else:
                search_term = 'NA'

            if product_price is None or product_url is None or product_name is None:
                pass

            if '/item/' not in product_url:
                pass

            item_tem_img = 'https://5.imimg.com/data5/PJ/DI/MY-3877854/round-neck-plain-tshirt-with-multi-color-design-500x500.png'

            items['name'] = product_name
            items['price'] = product_price
            items['category'] = search_category
            items['location'] = search_loc
            items['search_term'] = search_term
            items['img_url'] = item_tem_img
            items['item_url'] = product_url
            # items['current_date'] = product_name
            # items['slot_number'] = product_name

            yield items

    @staticmethod
    def rm_whilespace(query_term):
        if query_term:
            None_ = [nn_.replace('\n', '') for nn_ in query_term]
            None_ = [nn_.strip() for nn_ in None_]
            None_ = filter(None, None_)
            None_ = ' '.join(None_)
            ret_value = None_
            return ret_value
        # query_term = query_term.encode('ascii', 'xmlcharrefreplace').decode('utf8')
        return query_term

    def absolute_url(self, location, category, query_parameter):
        url = self.start_urls[0]
        fb_query = urlencode(query_parameter)
        if location:
            url = url + '/' + quote(location)
        if category:
            url = url + '/' + quote(category)
        url = url + '/?' + fb_query
        return url
