import scrapy

class jdihSpider(scrapy.Spider):
    name = 'jdih'
    start_urls = ['https://jdih.bkn.go.id/dokumen/peraturan']

    def parse_item(self, response):
        doklink = "https://jdih.bkn.go.id"
        item = {
            'link': response.url,
            'judul': response.css('h5::text').get(),
            "Tempat Terbit": response.css('.text-extra-dark-gray.font-weight-600::text')[0].get(),
            "Tanggal Penetapan": response.css('.text-extra-dark-gray.font-weight-600::text')[1].get(),
            "Tanggal Pengundangan": response.css('.text-extra-dark-gray.font-weight-600::text')[2].get(),
            "Sumber": response.css('.text-extra-dark-gray.font-weight-600::text')[3].get(),
            "Urusan Pemerintahan": response.css('.text-extra-dark-gray.font-weight-600::text')[4].get(),
            "Bidang Hukum": response.css('.text-extra-dark-gray.font-weight-600::text')[5].get(),
            "Bahasa": response.css('.text-extra-dark-gray.font-weight-600::text')[6].get(),
            "Pemrakarsa": response.css('.text-extra-dark-gray.font-weight-600::text')[7].get(),
            "Penandatanganan": response.css('.text-extra-dark-gray.font-weight-600::text')[8].get(),
            "Peraturan Terkait": response.css('.text-extra-dark-gray.font-weight-600::text')[10].get(),
            "Dokument Terkait": response.css('.text-extra-dark-gray.font-weight-600::text')[12].get(),
            "Hasil Uji Materi": response.css('.text-extra-dark-gray.font-weight-600::text')[14].get(),
            "Nama Pengarang": response.css('td::text')[0].get(),
            "Tipe Pengarang": response.css('td::text')[1].get(),
            "Jenis Pengarang": response.css('td::text')[2].get(),
            "Jenis Dokumen": response.css('strong::text')[0].get(),
            "Status": response.css('strong::text')[1].get(),
            "Lampiran": doklink+response.css('.widget-list a::attr(href)').get()
        }
        yield item

    def parse(self, response):
        for post in response.css('.card-body.no-padding-tb'):
            dict_url = {
                'url': post.css('p a::attr(href)')[1].get()
            }
            link = "https://jdih.bkn.go.id/" + dict_url.get('url')
            if link is not None:
                yield scrapy.Request(url=link, callback=self.parse_item)

        next_page = response.css('.next a::attr(href)').get()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)