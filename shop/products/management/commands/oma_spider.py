import requests
from products.models import Product
from products.spiders import OmaSpider
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):
        def crawler_results(signal, sender, item, response, spider):
            response = requests.get(item["image_name"])
            filename = "media/products/" + item["image_name"].split("/")[-1]
            short_name = "products/" + item["image_name"].split("/")[-1]
            if response.status_code == 200:
                with open(filename, "wb") as imgfile:
                    imgfile.write(response.content)

            Product.objects.update_or_create(
                external_id=item["external_id"],
                title=item["name"],
                price=item["price"],
                category=item["category"],
                description=item["link"],
                image=short_name,
            )

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(OmaSpider)
        process.start()
