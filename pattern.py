
pattern  = {
    'BOOK' : {
        'Name' : r"([^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'editor' : r'(?:.*บรรณาธิการ+.*)',
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)" ,
        'Book' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'Pim' : r"(?:(?:พิมพ์ครั้งที่[ ][0-9]+)?)",
        'translatefrom' : r'(?:แปลจาก+.*)',
        'translateby' : r'(?:ทรงแปลโดย+.*)',
        'Location' : r"",
        'SamNakPim' : r"(?:[ก-์]{0,20}(:)+.*)",
        },
    'ARTICLE' : {
        'Name' : r"([^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)",
        'article' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'editor' : r'(?:.*บรรณาธิการ+.*)',
        'Book' : r"",
        'Pim' : r"(?:(?:พิมพ์ครั้งที่[ ][0-9]+)?)",
        'NumPage' : r"(?:(?:[(]น\.\s[0-9]+\-[0-9]+[)]))",
        'Location' : r"",
        'SamNakPim' : r"(?:[ก-์]{0,20}(:)+.*)",
    },
    'JOURNAL' : {
        'Name' : r"([^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)",
        'article' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'magazine' : r"(?:[ก-์]+,+)",
        'numyear' : r"(?:[0-9]+[(][0-9]+[)])",
        'page' : r"(?:[0-9]+\-[0-9]+)"
    },
    'THESES':{
        'Name' : r"([^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)",
        'thesis' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'univer' : r"(?:[(](?:[ก-์]+\,\s[ก-์]+)*[)])"
    },
    'ELECTRONICS' : {
        'Name' : r"([^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'Year' : r"(?:(?:[(]\b\d{4}[)])?)",
        'article' : r'(?:([ก-์]|[A-Za-z])+\s?(?:(?:([ก-์]|[A-Za-z])+(?::)?(?:\s([ก-์]|[A-Za-z])+)?)|(?:\.\s([ก-์]|[A-Za-z])+(?:\s[a-zA-z]+)*\.(?:\s([ก-์]|[A-Za-z])+)*))(?:(?:\s\[([ก-์]|[A-Za-z])+\])|(?:\s\[[a-z A-Z]+\])))',
        'magazine' : r"(?:[ก-์]+)",
        'numyear' : r"(?:[0-9]+[(][0-9]+[)])",
        'page' : r"(?:[0-9]+\-[0-9]+)"
    },
    'WIKI' : {
        'subject' : r'^(?:[ก-์]+)',
        'Name' : r"([^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'day' : r"(?:สืบค้นเมื่อ\s[0-9]+\s[ก-์]+\s[0-9]+)",
        'article' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:([ก-์]|[A-Za-z])[^ ]+)",
        'web' : r"(?:\[[ก-์]+\])",
        'url' : r"(?:(?:สืบค้นจาก|จากวิกิพีเดีย)\s(?:https?:\/\/)?(?:[\w\-])+\.{1}(?:[a-zA-Z]{2,63})(?:[\/\w-]*)*\/?\??(?:[^#\n\r]*)?#?(?:[^\n\r]*)[^ ])"
    },
    'PERIODICAL' : {
        'Name' : r"([^ทรงแปลโดย])((?:[ก-์]{0,30}(,|)+\s+[ก-๙]*(?:(?:\.|,|และ)?(?:\s[ก-์]+|\s[(][ก-์]+[)]))*)(?:,\s.\s[ก-์]+\s[ก-์]+)?(?:\s[1-9]+\s(?:[ก-์]+\.)*\s(?:[0-9]+\-[0-9]+))?)",
        'article' : r"(?:\“[ก-์]+)",
        'magazine' : r"(?:([ก-์]|[A-Za-z])+\s([ก-์]|[A-Za-z])+\:\s([ก-์]|[A-Za-z])+)|(?:[ก-์]{30,100}(:)+.*)|(?:([ก-์]|[A-Za-z]){30,100}.*)|(?:(?:(?:\“)?[ก-์]|[A-Za-z])[^ ]+)",
        'numyear' : r"(?:ปีที่\s[0-9]+)",
        'numissue' : r"(?:ฉบับที่\s[0-9]+)",
        'page' : r"(?:หน้า\s[0-9]+\-[0-9]+)",
        'year' : r"(?:(?:\b\d{4}))"
    }
}