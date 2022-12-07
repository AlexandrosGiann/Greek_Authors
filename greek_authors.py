import tkinter as tk
import webbrowser

wn = tk.Tk()
wn.title('Greek Authors by Alexandros Giannakis') # Πρόγραμμα από τον Αλέξανδρο Γιαννάκη
wn.geometry("500x200")
search_textbox = tk.Entry(wn, width=50)
search_textbox.grid(row=0, column=1, sticky=tk.W+tk.E)
run_tlg = tk.IntVar()

def make_clear(word):
    word = word.replace('ΰ', 'υ')
    word = word.replace('ΐ', 'ι')
    word = word.replace('ς', 'σ')
    word = word.upper()
    word = word.replace('Ά', 'Α')
    word = word.replace('Έ', 'Ε')
    word = word.replace('Ή', 'Η')
    word = word.replace('Ί', 'Ι')
    word = word.replace('Ό', 'Ο')
    word = word.replace('Ύ', 'Υ')
    word = word.replace('Ώ', 'Ω')
    word = word.replace('Ϊ', 'Ι')
    word = word.replace('Ϋ', 'Υ')
    return word

authors = [['ΟΜΗΡΟΣ'], ['ΗΣΙΟΔΟΣ'], ['ΗΡΟΔΟΤΟΣ'], ['ΘΟΥΚΥΔΙΔΗΣ'], ['ΞΕΝΟΦΩΝ', 'ΞΕΝΟΦΩΝΤΑΣ'], ['ΠΛΑΤΩΝ', 'ΠΛΑΤΩΝΑΣ'], ['ΑΡΙΣΤΟΤΕΛΗΣ'], ['ΛΥΣΙΑΣ'], ['ΔΗΜΟΣΘΕΝΗΣ'], ['ΑΙΣΧΥΛΟΣ'], ['ΣΟΦΟΚΛΗΣ'], ['ΕΥΡΙΠΙΔΗΣ']]
greek_language_urls = ['https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=194',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=156',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=153',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=160',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=191',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=199',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=122',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=181',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=133',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=102',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=214',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=150'
]
perseus_urls = ['http://www.perseus.tufts.edu/hopper/searchresults?q=Homer',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Hesiod',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Herodotus',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Thucydides',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Xenophon',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Plato',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Aristotle',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Lysias',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Demosthenes',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Aeschylus',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Sophocles',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Euripides'
]
tlg_urls = ['http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0012&wid=&q=HOMERUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0020&wid=&q=HESIODUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0016&wid=&q=HERODOTUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=3&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0003&wid=&q=THUCYDIDES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=4&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0032&wid=&q=XENOPHON&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=5&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0059&wid=&q=PLATO&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=4&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=&wid=&q=ARISTOTELES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=5&acp=&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0540&wid=&q=LYSIAS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=3&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0014&wid=&q=DEMOSTHENES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0085&wid=&q=AESCHYLUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=3&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0011&wid=&q=SOPHOCLES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0006&wid=&q=EURIPIDES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid='
]

def get_search():
    author = search_textbox.get()
    for i in range(len(authors)):
        if make_clear(author) in authors[i]:
            webbrowser.open(greek_language_urls[i])
            webbrowser.open(perseus_urls[i])
            if run_tlg.get() == 1:
                webbrowser.open(tlg_urls[i])

search_button = tk.Button(wn, text="Αναζήτηση", command=get_search)
search_button.grid(row=0, column=2, sticky=tk.W+tk.E)
tlg_checkbox = tk.Checkbutton(wn, text='TLG',variable=run_tlg, onvalue=1, offvalue=0)
tlg_checkbox.grid(row=1, column=0)
wn.mainloop()
