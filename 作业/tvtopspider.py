info = response.css('#asyncRatingRegion>li')
rank = info[0].css('.number>em::text')
tv_name = info[0].css('.mov_con>h2>a::text').extract()
link = info[0].css('.mov_con>h2>a')
link[0].xpath('@href')
director = info[0].css('.mov_con>p>a::text').extract_first()
arctor = info[0].css('.mov_con>p>a::text').extract()[1:]
synopsis = info[0].css('.mt3::text').extract_first()
point = ''.join(info[0].css('.mov_point>b>span::text').extract())
