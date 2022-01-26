from urllib import request
import re


class Spider:
    url = ""
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = "</i>([\s\S]*?)</span>"
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()  # byte
        htmls = str(htmls, encoding="utf-8")
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {"name": name, "number": number}
            anchors.append(anchor)
        return anchors

    def __refine(self, anchors):
        l = lambda anchor: {
            "name": anchor["name"][0].strip(),
            "number": anchor["number"][0],
        }
        return map(l, anchors)

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed(), reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        r = re.findall("[1-9]\d*\.?\d*", anchor["number"])
        number = float(r[0])
        if "万" in anchor["number"]:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in (0, len(anchors)):
            print(
                "rank"
                + str(rank + 1)
                + ": "
                + anchors[rank]["name"]
                + "  "
                + anchors[rank]["name"]
            )

    def go(self):
        htmls = self.__fetch()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)


spider = Spider()
spider.go()
