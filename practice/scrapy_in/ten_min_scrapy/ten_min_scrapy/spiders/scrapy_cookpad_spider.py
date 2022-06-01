import scrapy
from ten_min_scrapy.items import Post

class ScrapyCookpadSpiderSpider(scrapy.Spider):
    name = 'scrapy_cookpad_spider'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com']
    print(1111111111111111111111111111111111111111111111111111111)

    def parse(self, response):
        print(2222222222222222222222222222222222222222222222)
        """
        レスポンスに対するパース処理
        """
        #response.css で scrapyデフォルトのcssセレクタを利用する
        for post in response.css('.post-listing .post-item'):
            print(111111111111111111111111111111111111111)
            print(post)
            # items に定義した Post のオブジェクトを生成して次の処理へ渡す
            yield Post(
                url=post.css('div.post-header a::attr(href)').extract_first().strip(),
                title=post.css('div.post-header a::text').extract_first().strip(),
                date=post.css('div.post-header span.date a::text').extract_first().strip(),
            )

        # 再帰的にページングを辿るための処理
        older_post_link = response.css('.blog-pagination a.next-posts-link::attr(href)').extract_first()
        if older_post_link is None:
            # リンクが取得できなかった場合は最後のページなので処理を終了
            return

        # URLが相対パスだった場合に絶対パスに変換する
        older_post_link = response.urljoin(older_post_link)
        # 次のページをのリクエストを実行する
        yield scrapy.Request(older_post_link, callback=self.parse)
